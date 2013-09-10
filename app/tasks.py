from celery import task

@task
def calculo():
    j = 1
    for i in xrange(10):
        if j % 2 and i:
            j *= i
        else:
            j += i
    print j