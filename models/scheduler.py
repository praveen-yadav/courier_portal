from gluon.scheduler import Scheduler

scheduler = Scheduler(db)


def send_email():
    # rows = db.courier().select(orderby=~db.courier.arrival_date)
    # temp = []
    # for row in rows:
    #      if row.taken == False:
    #          temp.append(row)
    # print temp[0]
    hisemail = "mailmeonlypraveen@gmail.com"  ###############change it to the mail of user

    sub = "New parcel.IIIT courier portal"
    msg = "You have new Parcels . Collect it form Nilgiri"
    if mail:
        if mail.send(to=[hisemail], subject=sub, message=msg):
            response.flash = 'email sent successfully.'
        else:
            response.flash = 'fail to send email sorry!'
    else:
        response.flash = 'Unable to send the email : email parameters not defined'


scheduler.queue_task(send_email)
