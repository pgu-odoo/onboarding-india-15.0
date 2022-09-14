from xmlrpc import client

url = 'http://localhost:8069'
db = 'test131'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
								'library.rental', 'check_access_rights',
								['write'], {'raise_exception': False})
print(model_access)

rentals = models.execute_kw(db, uid, password, 
							'library.rental' , 'search_read' ,
							[[['write_date' ,'<' , '2022-09-14 07:28:26.871528']]])
print(rentals)		

fetch_book = models.execute_kw(db, uid, password,
									'library.rental', 'search' ,
									[[['name' , '=', 'Client Server Computing']]])
print(fetch_book)

fetch_customer = models.execute_kw(db, uid, password,
									'library.rental', 'search' ,
									[[['customer_id' , '=', 'Deco Addict']]])
print(fetch_customer)

update_rental = models.execute_kw(db, uid, password,
 								  'library.rental' , 'write',
								  [[1],{'customer_id':fetch_customer[0],
								  		'intref' : 7 ,}])	
print(update_rental)