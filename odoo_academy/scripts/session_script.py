#-*- coding: utf-8 -*-

from xmlrpc import client

url='http://localhost:8069'
db='test_50'
username='admin'
password='admin'

comman=client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(comman.version())

uid=comman.authenticate(db, username, password, {})
print(uid)

models=client.ServerProxy("{}/xmlrpc/2/object".format(url))

models_access=models.execute_kw(db, uid, password,
								'acadamy.session','check_access_rights',
								['write'], {'raise_exception':False})
print(models_access)

courses=models.execute_kw(db, uid, password,
						'acadamy.course','search_read',
						[[['level','in',['intermediate','begnner']]]])

print(courses)

course=models.execute_kw(db, uid, password,
						'acadamy.course','search',
						[[['name','=','Accounting_200']]])
print(course)

session_fields=models.execute_kw(db, uid, password,
						'acadamy.session','fields_get',
						[],{'attributes': ['string','type','required']})
print(session_fields)

new_session=models.execute(db, uid, password,
							'acadamy.session','create',
							{
							'course_id': course[0],
							'state':'open',
							'duration':5,
							})
print(new_session)