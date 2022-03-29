from email.policy import default
from odoo.exceptions import ValidationError
from odoo import api, fields, models


class PeminjamanBuku(models.Model):
    _name = 'shosho.peminjaman'
    _description = 'New Description'

    name = fields.Char(string='Nama Peminjam')
    id_buku = fields.Many2one('shosho.buku', string='ID Buku')
    id_pinjam = fields.Char(string='ID Peminjam', required=True)
    tanggal_pinjam = fields.Datetime('Tanggal Peminjaman', default = fields.Datetime.now)
    tanggal_kembali = fields.Date(string='Tanggal Pengembalian', default = fields.Date.today())
    judulbuku = fields.Char(compute='_compute_judulbuku', string='Judul Buku')
    
    @api.depends('id_buku')
    def _compute_judulbuku(self):
        for record in self:
            record.judulbuku = record.id_buku.judul

    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    def buku_kembali(self):
        pass
    
    qty = fields.Integer(string='Jumlah')

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            kertas = self.env['shosho.buku'].search([('stok', '<', record.qty), ('id', '=', record.id)])
            if kertas:
                raise ValidationError("Stok buku habis")
    
    @api.model
    def create(self, vals):
        record = super(PeminjamanBuku, self).create(vals)
        if record.qty:
            self.env['shosho.buku'].search([('id', '=', record.id_buku.id)]).write({'stok':record.id_buku.stok-record.qty})
            return record