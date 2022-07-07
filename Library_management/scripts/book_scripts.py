#-*- coding: utf-8 -*-

from xmlrpc import clients

url='http://localhost:8069/'
db='test_65'
username='admin'
password='admin'

comman=client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(comman.version())

uid=comman.authenticate(db, username, password, {})
print(uid)

models=client.ServerProxy("{}/xmlrpc/2/object".format(url))