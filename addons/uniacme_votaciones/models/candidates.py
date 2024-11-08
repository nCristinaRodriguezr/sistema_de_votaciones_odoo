from odoo import models, fields

class Candidate(models.Model):
    _inherit = 'res.partner'
    _description = 'Candidato'

     # Campo para el ID del candidato
    candidate_id = fields.Char(string='ID_Candidato')

    # indica si es candidato
    is_candidate = fields.Boolean(string="Es Candidato", default=False)
    
    #election_ids = fields.Many2many('uniacme.election', string="Procesos de Votación")
    
    _sql_constraints = [
        ('unique_candidate_id', 'unique(candidate_id)', 'El número de identificación debe ser único para cada candidato.')
    ]

    