from odoo import models, fields, api

class Student(models.Model):
    _inherit = 'res.partner'

    # Campo para la carrera del estudiante
    career = fields.Char(string='Carrera')

    # Indica si es estudiante
    is_student = fields.Boolean(string="Es Estudiante", default=False)

     # ID del estudiante, debe ser único
    student_id = fields.Char(string='ID_Estudiante')

    # Campo de sede, relación con el modelo uniacme.campus
    campus = fields.Many2one('uniacme.campus', string='Sede', required=True)

    _sql_constraints = [
        ('unique_student_id', 'unique(student_id)', 'El número de identificación debe ser único para cada estudiante.')
    ]

    