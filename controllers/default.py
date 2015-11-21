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
    if request.args:
        if request.args(0,cast=int) == 0:
            response.flash="Succesfully udpated"
    rows = db(db.courier).select()
    return locals()


@auth.requires_membership(role='students')
def student_index():

    rows = db(db.courier.student == auth.user_id).select(orderby=~db.courier.arrival_date)
    temp = []
    for row in rows:
        if row.taken == False:
            temp.append(row)
    return locals()


@auth.requires_membership(role='students')
def show_student():
    if request.args:
        db.feedbacks.courier_id.writable = True
        db.feedbacks.courier_id.readable = True
        courier_obj = db.courier(request.args(0, cast=int))
        oldfeedback = db(db.feedbacks.courier_id == request.args(0, cast=int)).select(db.feedbacks.body)
        pass
    else:
        BEAUTIFY("NOTHING TO SHOW")
    return locals()



@auth.requires_membership('students')
def feedback():
    if request.args(0) is None:
        print "hye"
        pass
    else:
        record = db.feedbacks(db.feedbacks.courier_id == request.args(0, cast=int))
        db.feedbacks.courier_id.default = request.args(0, cast=int)
        form = SQLFORM(db.feedbacks, record).process()
        form.vars.courier_id = request.args(0, cast=int)
        if form.accepted:
            redirect(URL('show_student', args=request.args(0, cast=int)))
            pass
        pass
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
    if request.args(0) is None:
        courier_obj= db(db.courier.student == auth.user_id).select()
        print courier_obj
        pass
    else:
        courier_obj = db.courier(request.args(0, cast=int))
    return locals()

@auth.requires_membership(role='security')
def show_security():
     if request.args(0) is None:
         courier_obj= db(db.courier.student == auth.user_id).select()
         print courier_obj
         pass
     else:
         courier_obj = db.courier(request.args(0, cast=int))
     return locals()


@auth.requires_membership(role='security')
def show_update():
    ids = int(request.vars.id)
    if request.vars.taken:
        db(db.courier.id==ids).update(taken=True)
        response.flash="Succesfully update"
        redirect(URL('security_index',args=0))
    else:
        db(db.courier.id==ids).update(taken=False)
        response.flash="Succesfully update"
        redirect(URL('security_index',args=0))


@auth.requires_login()
def search():
    print "search page requested\n"
    people = []
    rows = []
    if request.vars.search == "":
        T("No vars")
        pass
    else:
        form = SQLFORM.factory(Field('name', requires=IS_NOT_EMPTY()))
        if request.vars.category and request.vars.category == "name":
            tokens = request.vars.search.split()
            query = reduce(lambda a, b: a & b,
                           [db.auth_user.first_name.contains(k) | db.auth_user.last_name.contains(k) \
                            for k in tokens])
            people = db(query).select(orderby=alphabetical)
            print people
            pass

        elif request.vars.category and request.vars.category == "roll":
            tokens = int(request.vars.search)
            rows = db(db.courier.student == tokens).select()
            print rows
            pass
    return locals()


def export_csv():
    import gluon.contenttype
    response.headers['Content-Type'] = \
        gluon.contenttype.contenttype('.csv')

    rows = db(db.courier.type_of_courier.contains(request.vars.company)).select()
    allfeedbacks=[]
    s = ""
    for row in rows:
         allfeedbacks.append(db(db.feedbacks.courier_id == row.id).select(db.feedbacks.body))
         for fb in allfeedbacks:
             s = s+str(fb)
    return s


@auth.requires_membership(role='security')
def csv_download():
    return locals()



def user():
    return dict(form=auth())
