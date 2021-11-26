# -*- coding: utf-8 -*- 

from odoo import models, fields, api 

class ResPartner(models.Model):
    
    _inherit = 'res.partner' 
    
    partner_type_custom = fields.Selection([('PND', 'PND'),('PJD','PJD')], string='partner custom', store=True, compute="_type")
    
    @api.onchange('is_company')
    def _partner_type(self):
        for partner in self:
            if partner.is_company:
                self.partner_type_custom = 'PJD'
            else:
                self.partner_type_custom = 'PND'
                
    
    @api.model
    def _type(self):
        partners = self.env['res.partner'].search_read([], ['is_company'])
        for partner in partners:
            if partner.is_company:
                return 'PJD'
            else:
                return 'PND'