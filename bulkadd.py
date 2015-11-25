import os, os.path, re, json
import auth, utils
import csv
import sys
from mailconfig import get_mail_users, get_mail_users_ex, get_admins, add_mail_user, set_mail_password, remove_mail_user
from mailconfig import get_mail_user_privileges, add_remove_mail_user_privilege
from mailconfig import get_mail_aliases, get_mail_aliases_ex, get_mail_domains, add_mail_alias, remove_mail_alias

userfile = sys.argv[1]

env = utils.load_environment()
#print(userfile)
#print(env)

with open(userfile) as usercsv:
 rows = csv.reader(usercsv,delimiter=',')
 for row in rows:
  try:
   out = add_mail_user(row[0],row[1] , '', env)
   print(row[0]+" -> "+out[0])
  except Exception as e:
   print(e)
