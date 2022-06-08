{
    "name":"Odoo Academy",

    "summary": """Acadeny app to manage Training""",
    "sequence":-100,
    "description":"""
        Academy Module to manage Training:
          -Courses
          -Sessions
          -Attendees
    """,      
    "author":"Odoo",
    "website":"https://www.odoo.com",
    "license":"LGPL-3",

    "category":"Training",
    "version":"1.1.0",

    "depends":["base","sale"],

    "data":[
         'security/academy_security.xml',
         'security/ir.model.access.csv',
         'views/course_view.xml',
         'views/session_view.xml',
         'views/academy_menuitems.xml',
         'views/sale_views_inherit.xml',
    ],

    "demo": [
        "demo/academy_demo.xml",
    ],

    'application':True,
    'auto_install':False,
    'installable':True,
}   
