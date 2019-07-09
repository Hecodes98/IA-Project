#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ya que no tenemos una base del conocimiento tuvimos que tener las posibles maneras de decir
# palabras y guardar las entidades con las que el usuario podria interactuar

patterns = [{"label": "Colombia", "pattern": 'colombia'},  # Aqui tenemos las entidades
            {"label": "Risaralda", "pattern": 'risaralda'},
            {"label": "Antioquia", "pattern": 'antioquia'},
            {"label": "Cundinamarca", "pattern": 'cundinamarca'},
            {"label": "Amazonas", "pattern": 'amazonas'},
            {"label": "Cesar", "pattern": 'cesar'},
            {"label": "Quindío", "pattern": 'quindío'},
            {"label": "Cauca", "pattern": 'cauca'},
            {"label": "Meta", "pattern": 'meta'},
            {"label": "Arauca", "pattern": 'arauca'},
            {"label": "Atlántico", "pattern": 'atlántico'},
            {"label": "Bolívar", "pattern": 'bolívar'},
            {"label": "Boyacá", "pattern": 'boyacá'},
            {"label": "Caldas", "pattern": 'caldas'},
            {"label": "Caquetá", "pattern": 'caquetá'},
            {"label": "chocó", "pattern": 'chocó'},
            {"label": "Córdoba", "pattern": 'córdoba'},
            {"label": "Cundinamarca", "pattern": 'cundinamarca'},
            {"label": "Guanía", "pattern": 'guanía'},
            {"label": "Guaviare", "pattern": 'guaviare'},
            {"label": "Huila", "pattern": 'huila'},
            {"label": "La Guajira", "pattern": [
                {"lower": "la"}, {"lower": "guajira"}]},
            {"label": "Magdalena", "pattern": 'magdalena'},
            {"label": "Nariño", "pattern": 'nariño'},
            {"label": "Huila", "pattern": 'huila'},
            {"label": "Norte De Santander", "pattern": [{"lower": "norte"}, {
                "lower": "de"}, {"lower": "santander"}]},
            {"label": "Putumayo", "pattern": 'putumayo'},
            {"label": "Nariño", "pattern": 'nariño'},
            {"label": "San Andrés y Providencia", "pattern": [{"lower": "san"}, {
                "lower": "andres"}, {"lower": "y"}, {"lower": "providencia"}]}
            ]

how_many = 'cuántos'
Tables = {  # Las posibles tablas
    'departamentos': [
        'departamentos',
        'departamento',
        'estados',
        'estado'
    ]
}

Fields = {  # los campos
    'departamentos': {
        'nombreDepto': [
            'nombre',
            'nombres'
        ],
        'poblacionDepto': [
            'población',
            'poblacion',
            'personas',
            'habitantes',
            'persona',
            'habitante'
        ],
        'regionDepto': [
            'región',
            'region',
            'regional',
            'regiones',
            'territorio',
            'territorio'
        ],
        'superficieDepto': [
            'area',
            'superficie',
            'superficies',
            'tamaño',
        ],
        'gentilicioDepto': [
            'gentilicio',
        ],
        'municipioDepto': [
            'municipio',
            'municipios'
        ],
        'capitalDepto': [
            'capital',
            'capitales',
            'ciudad principal',
            'municipio principal',
            'estados',
            'estado'
        ],
        'fundacionDepto': [
            'fundacion',
            'fundación',
            'creacion',
            'fundada',
            'fundo',
            'fundó',
            'fundamento'
        ]
    }

}

consulta = {  # Diccionario para consultas de prueba antes de realizar la consulta con la base de datos
    'departamentos': {
        'Risaralda': {
            'capitalDepto': 'Pereira',
            'regionDepto': 'Andina',
            'municipioDepto': ['Dosquebradas', 'Pereira']
        },
        'Huila': {
            'capitalDepto': 'Ibague',
            'regionDepto': 'Andinas',
            'municipioDepto': ['Caqueta', 'otra vaina']
        }
    }
}
