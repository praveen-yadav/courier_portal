# -*- coding: utf-8 -*-
db.define_table('courier',
	Field('roll',requires=IS_NOT_EMPTY()),
	Field('type_of_courier'),
	Field('arrival_date','datetime'),
	Field('last_email_sent','datetime'),
	Field('address','text',requires=IS_NOT_EMPTY()),
	Field('taken'))