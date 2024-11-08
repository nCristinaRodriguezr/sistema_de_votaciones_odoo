from odoo import models, fields
import pytz

# Aqui estoy definiendo el modelo para creacion de sedes, donde los campos seran el nombre de sede,
# el pais y la zona horaria, este modelo es interno.

class UniversityCampus(models.Model):
    _name = 'uniacme.campus'
    _description = 'Sede Universitaria'
    
    # Campo para el nombre de la sede
    name = fields.Char(string='Nombre de la Sede', required=True)

    # Campo para el pais
    country = fields.Many2one('res.country', string='País', required=True)

    # Campo para la zona horaria
    timezone = fields.Selection(
        selection='_get_timezone_selection', 
        string='Zona Horaria', 
        required=True
    )

    # Función para cargar la lista de zonas horarias
    def _get_timezone_selection(self):
        return [(tz, tz) for tz in pytz.all_timezones]