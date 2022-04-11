# -*- coding: utf-8 -*-
from odoo import http

# class EmployeeMatricule(http.Controller):
#     @http.route('/employee_matricule/employee_matricule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_matricule/employee_matricule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_matricule.listing', {
#             'root': '/employee_matricule/employee_matricule',
#             'objects': http.request.env['employee_matricule.employee_matricule'].search([]),
#         })

#     @http.route('/employee_matricule/employee_matricule/objects/<model("employee_matricule.employee_matricule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_matricule.object', {
#             'object': obj
#         })