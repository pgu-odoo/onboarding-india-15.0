1. models :
Odoo models are created by inheriting one of the following:

Model: for regular database-persisted models

TransientModel: for temporary data, stored in the database but automatically vacuumed every so often

AbstractModel: for abstract super classes meant to be shared by multiple inheriting models