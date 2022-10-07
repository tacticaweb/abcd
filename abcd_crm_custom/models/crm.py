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

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    negociacion = fields.Float(string='Negociación')
    
class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    origen = fields.Selection([
            ('loc', 'Locación'),
            ('cam', 'Campaña de marketing interna'),
            ('marca', 'Marca'),
            ('arqui', 'Arquitecto'),
            ('cli', 'Cliente Satisfecho'),
        ],
        string='Origen Lead', required=True,
        default='loc')
    
    marcas = fields.Many2one('crm.team', string='Marca')
    arquitecto = fields.Many2one('res.partner', string='Arquitecto', domain="[('arquitecto','=',True)]")
    
class ResPartner(models.Model):
    _inherit = 'res.partner'   
    
    arquitecto = fields.Boolean(string='Es Arquitecto?',default=False)
    quien_refiere = fields.Selection([
            ('marca', 'Marca'),
            ('arqui', 'Arquitecto'),
            ('otro', 'Otro'),
        ],
        string='¿Quién lo refiere?',
        default='marca')
    marcas = fields.Many2one('crm.team', string='Marca')
    otro_cual = fields.Char('Cual?')