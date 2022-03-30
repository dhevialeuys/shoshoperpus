from email.policy import default
from odoo import api, fields, models


class Partner(models.Model):
    _name_ = 'shosho.partner'
    _inherit = 'res.partner'
    
    peminjamnya = fields.Boolean(string='Peminjam', default = False)
