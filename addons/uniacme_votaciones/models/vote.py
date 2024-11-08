from odoo import models, fields, api

# Aqui estoy definiendo el modelo de los votos de los estudiantes, que tiene el campo de eleccion,
# estudiante y camdidato. Estas relaciones se hacen con los primaryKey de cada modelo.

class Vote(models.Model):
    _name = 'uniacme.vote'

    election = fields.Many2one('uniacme.election', string='Proceso de votación', required=True)

    student = fields.Many2one('res.partner', string='Estudiante', required=True)

    candidate = fields.Many2one('res.partner', string='Candidato', required=True)

    vote_count = fields.Integer(string="Voto", default=1)

    _sql_contraints = [
        ('unique_student_vote', 'UNIQUE(student, election)', 'Cada estudiante puede votar solo una vez en cada elección.')
    ]