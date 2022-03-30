from email.policy import default
from odoo.exceptions import ValidationError
from odoo import api, fields, models


class PeminjamanBuku(models.Model):
    _name = 'shosho.peminjaman'
    _description = 'New Description'

    name = fields.Char(string='ID Peminjam', required=True)
    peminjamanbukudetail_ids = fields.One2many(
        comodel_name='shosho.peminjamanbukudetail',
        inverse_name='id_pinjam',
        string='Detail Peminjaman Buku')


    
    peminjam = fields.Many2one(
        comodel_name='res.partner',
        string='Peminjam',
        domain=[('peminjamnya', '=', True)], store=True)
    
    tanggal_pinjam = fields.Datetime('Tanggal Peminjaman', default = fields.Datetime.now)
    tanggal_kembali = fields.Date(string='Tanggal Pengembalian', default = fields.Date.today())
    
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    def buku_kembali(self):
        pass

class PeminjamanBukuDetail(models.Model):
    _name = 'shosho.peminjamanbukudetail'
    _description = 'New Description'

    id_pinjam = fields.Many2one(comodel_name='shosho.peminjaman', string='Pinjam')
    buku_id = fields.Many2one(
        comodel_name='shosho.buku',
        string='ID Buku',
        domain=[('stok', '<', '20')])
    name = fields.Char(string='Name')


    qty = fields.Integer(string='Jumlah')

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            kertas = self.env['shosho.buku'].search([('stok', '<', record.qty), ('id', '=', record.id)])
            if kertas:
                raise ValidationError("Stok buku habis")
    
    @api.model
    def create(self, vals):
        record = super(PeminjamanBukuDetail, self).create(vals)
        if record.qty:
            self.env['shosho.buku'].search([('id', '=', record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
            return record