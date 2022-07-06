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
								'sal.order','check_access_rights',
								['write'], {'raise_exception':False})
print(models_access)

draft_quotes=models.execute_kw(db, uid, password,
								'sale.order','search',
								[[['state','=','draft']]])
print(draft_quotes)

if_confirmed=models.execute_kw(db, uid, password,
								'sale.order','action_confirm',
								[draft_quotes])
print(if_confirmed)
