# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Courier Portal'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://127.0.0.1:8000/courier_portal/default/index",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Praveen <praveen.yadav@students.iiit.ac.in>'
response.meta.description = 'Manages new couriers'
response.meta.keywords = 'web2py, python, iiit,courier, framework'


## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Help'), False, URL('default', 'help'), []),
]
response.menu_student = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Show'), False, URL('default', 'show'), []),
    (T('Feedback'), False, URL('default', 'feedback'), []),
]
response.menu_security = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Create'), False, URL('default', 'create'), []),
    (T('Show'), False, URL('default', 'show'), []),
    (T('Download Feedbacks'), False, URL('default', 'csv_download'), []),
]
DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():

    app = request.application
    ctr = request.controller


if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu() 
