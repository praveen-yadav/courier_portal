@auth.requires_login()
def index():
    if auth.has_membership('security'):
        print "security"
        redirect(URL('security_index'))
    else:
        print "student"
        redirect(URL('student_index'))
    return locals()


@auth.requires_membership(role='security')
def security_index():
    rows = db(db.courier).select()
    return locals()


@auth.requires_membership(role='students')
def student_index():
    rows = db(db.courier).select()
    return locals()


@auth.requires_membership(role='students')
def show_student():
    courier_obj=db.courier(request.args(0,cast=int))
    return locals()


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


@auth.requires_login()
def search():
    form = SQLFORM.factory(Field('name',requires=IS_NOT_EMPTY()))
    if form.accepts(request):

        tokens = form.vars.name.split()
        query = reduce(lambda a,b:a&b,
                       [db.auth_user.first_name.contains(k)|db.auth_user.last_name.contains(k) \
                            for k in tokens])
        print query
        people = db(query).select(orderby=alphabetical)
    else:
        people = []
    return locals()


# this is the Ajax callback
# @auth.requires_login()
# def friendship():
#     """AJAX callback!"""
#     if request.env.request_method!='POST': raise HTTP(400)
#     if a0=='request' and not Link(source=a1,target=me):
#         # insert a new friendship request
#         Link.insert(source=me,target=a1)
#     elif a0=='accept':
#         # accept an existing friendship request
#         db(Link.target==me)(Link.source==a1).update(accepted=True)
#         if not db(Link.source==me)(Link.target==a1).count():
#             Link.insert(source=me,target=a1)
#     elif a0=='deny':
#         # deny an existing friendship request
#         db(Link.target==me)(Link.source==a1).delete()
#     elif a0=='remove':
#         # delete a previous friendship request
#         db(Link.source==me)(Link.target==a1).delete()



def user():
    return dict(form=auth())
