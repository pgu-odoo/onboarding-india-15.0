{
    "name":"Odoo Academy",

    "summary": """Acadeny app to manage Training""",
    "sequence":-1000,
    "description":"""
        Academy Module to manage Training:
          -Courses
          -Sessions
          -Attendees
    """,      
    "author":"Odoo",
    "website":"https://www.odoo.com",


    "category":"Training",
    "version":"0.1",

    "depends":["base"],

    "data":[
         'security/academy_security.xml',
         'security/ir.model.access.csv',
         'views/course_view.xml',
    ],

    "demo": [
    "demo/academy_demo.xml",
    ],

    'application':True,
    'auto_install':False,
    'installable':True,
}   
