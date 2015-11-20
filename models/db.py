# -*- coding: utf-8 -*-

from gluon.contrib.appconfig import AppConfig

myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:

    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:

    db = DAL('google:datastore+ndb')

    session.connect(request, response, db=db)

response.generic_patterns = ['*'] if request.is_local else []

response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

auth.settings.extra_fields['auth_user'] = [
    Field('phone', 'integer', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty), label=T('Mobile')),
    Field('hostel', requires=IS_IN_SET(('Bakul', 'Parul', 'Parijaat', 'OBH', 'NBH')), label=T('Hostel')),
    Field('room', 'integer', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty), label=T('Room No'))
]
auth.define_tables(username=False, signature=False)

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

# configure email


mail = auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'mailmeonlypraveen@gmail.com'
mail.settings.login = 'mailmeonlypraveen@gmail.com:hmdgzvgyoyfkdjgu'

# configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

auth.settings.actions_disabled.append('register')



