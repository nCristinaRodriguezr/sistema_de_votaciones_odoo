import json
from odoo import http
from odoo.http import request

class VotingController(http.Controller):
    @http.route('/get_candidates', type='http', auth='public', methods=['GET'], csrf=False)
    def get_candidates(self, votacion_id):
        # Obtener los candidatos de la votación seleccionada
        candidates = request.env['res.partner'].sudo().search([
            ('is_candidate', '=', True),
            ('id', 'in', request.env['uniacme.election'].browse(int(votacion_id)).candidate_ids.ids)
        ])
        candidates_data = [{
            'id': candidate.id,
            'name': candidate.name,
            'image': candidate.image_1920.decode('utf-8') if candidate.image_1920 else ''
        } for candidate in candidates]

        return request.make_response(
            json.dumps(candidates_data),
            headers={'Content-Type': 'application/json'}
        )
    
    @http.route('/submit_vote', type='http', auth='public', methods=['POST'], csrf=False)
    def submit_vote(self, **kwargs):
        student_id = kwargs.get('student_id')
        votacion = kwargs.get('votacion')
        candidato = kwargs.get('candidato')

        # Verificar si el estudiante existe y puede votar
        student = request.env['res.partner'].sudo().search([('student_id', '=', int(student_id)), ('is_student', '=', True)], limit=1)
        if not student:
            return request.make_response("Estudiante no encontrado", status=400)

        # Verificar si el estudiante ya ha votado en esta votación
        existing_vote = request.env['uniacme.vote'].sudo().search([
            ('student', '=', student.id),
            ('election', '=', int(votacion))
        ])
        if existing_vote:
            return request.make_response("Ya has votado en esta elección", status=400)

        # Crear el voto
        request.env['uniacme.vote'].sudo().create({
            'student': student.id,
            'election': int(votacion),
            'candidate': int(candidato)
        })

        return request.make_response("Voto registrado con éxito", status=200)
