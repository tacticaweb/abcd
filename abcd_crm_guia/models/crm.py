# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning, UserError
from odoo.osv import osv
from odoo.http import request
import time
from datetime import datetime, date, time, timedelta
import sys
import pytz
import json

class AbcdGuia(models.Model):
    
    _name = 'abcd.guia'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char(size=256, string='Descripcion', required=True)
    proyecto = fields.Many2one(
        'res.partner', 'Proyecto', required=True, ondelete='cascade', 
        #domain="[('company_type','=','company')]"
    )
    visitante = fields.Many2one(
        'res.partner', 'Related Partner', required=True, ondelete='cascade',
        #domain="[('company_type','=','individual')]"
    )
    fecha_visita = fields.Datetime('Fecha Visita')
    marcas = fields.Many2many(
        comodel_name="crm.team",
        relation="guia_marca_rel",
        column1="marca_id",
        column2="guia_id",
        readonly=False,
        string="Marcas",)
    categorias = fields.Many2many(
        comodel_name="product.category",
        relation="guia_categoria_rel",
        column1="categoria_id",
        column2="guia_id",
        readonly=False,
        string="Categoria de Productos",)
    direccion = fields.Char(related='proyecto.street', string='Dirección Proyecto', store=True)
    comentarios = fields.Text('Comentarios')
    