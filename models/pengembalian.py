from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'shosho.pengembalian'
    _description = 'Pengembalian Buku yang Telah Dipinjam'

    name = fields.Char(compute='_compute_nama_peminjam', string='Nama Peminjam')
    id_buku = fields.Many2one('shosho.buku', string='ID Buku')
    
    @api.depends('name')
    def _compute_nama_peminjam(self):
        for record in self:
            record.name = self.env['shosho.buku'].search([('id', '=', record.name.id)]).name

    tgl_pengembalian = fields.Date(string='', default=fields.Date.today())
    
    @api.model
    def create(self, vals):
        record = super(Pengembalian, self).create(vals)
        if record.tgl_pengembalian:
            self.env['shosho.peminjaman'].search([('id', '=', record.id_buku.id)]).write({'sudah_kembali':True})
            return record
    
    def unlink(self):
        for devi in self:
            self.env['shosho.peminjaman'].search([('id', '=', devi.id_buku.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()