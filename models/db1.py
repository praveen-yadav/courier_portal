# -*- coding: utf-8 -*-
db.define_table('courier',
                Field('student', 'reference auth_user'),
                Field('type_of_courier'),
                Field('arrival_date', 'datetime'),
                Field('last_email_sent', 'datetime'),
                Field('phone', 'integer', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty), label=T('Mobile')),
                Field('address', requires=IS_IN_SET(('Bakul', 'Parul', 'Parijaat', 'OBH', 'NBH')), label=T('Hostel')),
                Field('room', 'integer', requires=IS_NOT_EMPTY(error_message=auth.messages.is_empty), label=T('Room No')),
                Field('taken', 'boolean', default='false')
                )


db.define_table('feedbacks',
                Field('courier_id', 'reference courier'),
                Field('body', 'text', requires=IS_NOT_EMPTY(), label='What is your Feedback?'),
                auth.signature,
                primarykey=['courier_id'],
                migrate=False
                )  # created_on, created_by,modified_on,modified_by

User = db.auth_user
alphabetical = User.first_name | User.last_name


def name_of(user): return '%(first_name)s %(last_name)s' % user
