{
    'name': "Odoo Local Library ",
    'version': '1.0',
    'summary' : """Manage the books""",
     'description': """
         Library Management for manage the books
      """,

      'author': "odoo",

     'website': 'https://www.odoo.com',

     'category' : 'Management',

     'depends': ['base'],

     'license': 'OEEL-1',

     'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitem.xml',
        'views/book_views.xml',
        'views/rental_views.xml',
     ],
 
     'demo': [
        'demo/library_demo.xml'
       
     ],
    
}