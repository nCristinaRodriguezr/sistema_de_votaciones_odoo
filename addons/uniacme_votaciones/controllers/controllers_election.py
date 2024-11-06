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
        """ return {
            'candidates': [{
                'id': candidate.id,
                'name': candidate.name,
                'image': candidate.image_1920.decode('utf-8') if candidate.image_1920 else ''
            } for candidate in candidates]
        } """
        candidates_data = [{
            'id': candidate.id,
            'name': candidate.name,
            'image': candidate.image_1920.decode('utf-8') if candidate.image_1920 else ''
        } for candidate in candidates]

        return request.make_response(
            json.dumps(candidates_data),
            headers={'Content-Type': 'application/json'}
        )
