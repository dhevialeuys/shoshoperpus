# -*- coding: utf-8 -*-
# from odoo import http


# class Shoshoperpus(http.Controller):
#     @http.route('/shoshoperpus/shoshoperpus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shoshoperpus/shoshoperpus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shoshoperpus.listing', {
#             'root': '/shoshoperpus/shoshoperpus',
#             'objects': http.request.env['shoshoperpus.shoshoperpus'].search([]),
#         })

#     @http.route('/shoshoperpus/shoshoperpus/objects/<model("shoshoperpus.shoshoperpus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shoshoperpus.object', {
#             'object': obj
#         })
