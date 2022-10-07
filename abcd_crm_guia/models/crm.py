# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning, UserError
import time
from datetime import datetime, date, time, timedelta

class ProductCategory(models.Model):
    _inherit = "product.category"

    categorias = fields.Many2many(
        "crm.team",
        "categoria_marca_rel",
        "categoria_id",
        "team_id",
        readonly=False,
        string="Marcas")

class AbcdGuia(models.Model):
    
    _name = "abcd.guia"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char('Descripcion', required=True)
    proyecto = fields.Many2one(
        'res.partner', 'Proyecto', required=True, ondelete='cascade', 
        domain="[('is_company', '=', True)]"
    )
    visitante = fields.Many2one(
        'res.partner', 'Vistante', required=True, ondelete='cascade',
        domain="[('is_company', '=', False)]"
    )
    fecha_visita = fields.Datetime('Fecha Visita')
    marcas = fields.Many2many(
        "crm.team",
        "guia_marca_rel",
        "guia_id",
        "marca_id",
        readonly=False,
        string="Marcas")
    categorias = fields.Many2many(
        "product.category",
        "guia_categoria_rel",
        "guia_id",
        "categoria_id",
        readonly=False,
        string="Categoria de Productos")
    direccion = fields.Char(related='proyecto.street', string='Dirección Proyecto', store=True)
    comentarios = fields.Text('Comentarios')
    
    def generate_leads(self):
        marcas = []
        for guia in self:
            for marca in guia.marcas:
                marcas.append(marca.id)
            for categoria in guia.categorias:
                for marca in categoria.categorias:
                    if not marca.id in marcas:
                        marcas.append(marca.id)
            for team in marcas:
                vals = {
                    'name': guia.name,    
                    'partner_id': guia.proyecto.id,
                    'team_id': team,
                    'description': guia.comentarios,
                    }
                self.env['crm.lead'].create(vals)
