from odoo import api, fields, models


class Buku(models.Model):
    _name = 'shosho.buku'
    _description = 'Daftar Buku yang Tersedia'

    name = fields.Char(string='Kode Buku', required=True)
    judul = fields.Char(string='Judul Buku')
    penulis = fields.Char(string='Penulis Buku')
    penerbit = fields.Char(string='Penerbit Buku')
    tahun = fields.Char(string='Tahun Terbit')
    jenis_buku = fields.Selection(string='Jenis Buku', selection=[('novel', 'Novel'), ('buku cerita', 'Buku Cerita'), ('komik', 'Komik')])
    stok = fields.Integer(string='Stok Buku Tersedia')
    deskripsi = fields.Char(string='Deskripsi Buku')
    
    
