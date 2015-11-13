@auth.requires_login()
def index():
    # email = db.auth_user('security').email
    # print email
    # if db.auth_membership.group_id == 10:
    #    redirect(URL('create'))
    #    pass
    # else:
    #    redirect(URL('show/3'))
    #    pass

    #  auth.settings.login_next = URL('show')
    rows = db(db.courier).select()
    return locals()


def security_index():
    pass

    # create can only be called by logged in people



@auth.requires_membership(role='security')
def create():
    # create own form in index.html
    db.courier.arrival_date.default = request.now
    db.courier.arrival_date.writable = False
    db.courier.arrival_date.readable = False
    db.courier.last_email_sent.default = request.now
    db.courier.last_email_sent.writable = False
    db.courier.last_email_sent.readable = False
    form = SQLFORM(db.courier).process()
    if form.accepted: redirect(URL('index'))
    return locals()


@auth.requires_login()
def show():
    courier_obj = db.courier(request.args(0, cast=int))
    return locals()


def user():
    return dict(form=auth())
