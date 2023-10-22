from datetime import datetime, timedelta, timezone
import pandas as pd
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
import models
# import schemas

# Set the timezone as JST
JST = timezone(timedelta(hours=+9), 'JST')

'''
User table:
Functions used to manipulate the user table which is used maily in login,
but it also will be used for other purposes too; such as registering the creators or approvers
to the GL data or summarizing GL based on attributes associted with each employee.
'''
# TODO: Implement later on
def get_user_by_username():
    pass

'''
GL table:
Functions used to manipulate the GL table which is absolutely the fundatametals for every operation with in this service.
'''
# query GL data based on provided conditions, such as period, account, creator/approver, etc...
def get_gl_data():
    pass

# create journal entries
def create_journal_entries():
    pass

# approve journal entries
def post_journal():
    pass

'''
Account table:
Functions used to manipulate the account table. This is imperative to flexibly visualize or aggregate the GL data.
'''
def get_acc_data():
    pass