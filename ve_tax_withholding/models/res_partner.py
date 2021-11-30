# -*- coding: utf-8 -*- 

from odoo import models, fields, api 

class ResPartner(models.Model):
    
    _inherit = 'res.partner' 
    
    partner_type_custom = fields.Selection([('PND', 'PND'),('PJD','PJD')], string='partner custom', store=True)
    
    test = fields.Boolean(string='fuck', default=lambda self: self._type())
    
    @api.onchange('is_company')
    def _partner_type(self):
        for partner in self:
            if partner.is_company:
                self.partner_type_custom = 'PJD'
            else:
                self.partner_type_custom = 'PND'
                
    
    @api.model
    def _type(self):
        partners = self.env['res.partner']
        for partner in partners:
            partner.update({
                'test': partner.is_company
            })             