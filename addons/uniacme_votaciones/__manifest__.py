{
    'name': 'Gestión de Votaciones UNIACME',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Gestión de procesos de votación para estudiantes y candidatos en UNIACME',
    'author': 'Nataly Cristina Rodriguez',
    'website': 'https://www.uniacme.edu',
    'depends': ['base', 'web', 'website'],
    'license': 'LGPL-3',
    'data': [
        'views/university_campus_views.xml',
        'security/ir.model.access.csv',
        'views/students_view.xml',
        'views/candidate_view.xml',
        'views/election_view.xml',
        'views/templates.xml',
        'views/pages.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'uniacme_votaciones/static/src/js/voting_page.js',
        ],
    },
    'installable': True,
    'application': True,
}