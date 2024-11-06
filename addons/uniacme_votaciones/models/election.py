from odoo import models, fields

class Election(models.Model):
    _name = 'uniacme.election'
    _description = 'Proceso de Votación'

    # Campo para la descripcion de la votación
    description = fields.Char(string="Descripción de la Votación", required=True)

    # Campo para la fecha de inicio de votaciones
    start_date = fields.Datetime(string="Inicio de Votación", required=True)

    # Campo para la fecha de finalizavión de votaciones
    end_date = fields.Datetime(string="Fin de Votación", required=True)

    # Campo para la zona horaria
    #timezone = fields.Char(string="Zona Horaria", required=True)

    # Campo para elegir los candidatos
    candidate_ids = fields.Many2many('res.partner', string="Candidatos", domain=[('is_candidate', '=', True)])

    # Campo para el estado de la votación
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('ongoing', 'En Proceso'),
        ('closed', 'Cerrada')
    ], string="Estado", default='draft')
