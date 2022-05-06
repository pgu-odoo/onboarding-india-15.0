# -*- coding: utf-8 -*
# links those folder name who contain .py files (models,controllers, etc)
from . import wizard #put all wizard file first because it doesn't store into DB
from . import models 
from . import report 
from . import controllers   #used for rendering purpose