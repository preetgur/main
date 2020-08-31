
from django import template
from django.contrib.auth.models import Group

register = template.Library()




@register.filter(name="is_admin")    # "is_admin" is a filter name it can be named different form fxn name
def has_group(logged_in_user,arg1):
    print("!!!!!!!!!!!! custom tags :  :",logged_in_user)
<<<<<<< HEAD
    # print("### data get from template ###",arg1)  
=======
    print("### data get from template ###",arg1)  
>>>>>>> 55fe3e4c34ff151a9c3852917123362152c84fc7
    #  is_admin:"gurpreet" ,gurpreet store in arg1

    
    
    if logged_in_user.groups.filter(name='admin').exists():

        return True

    else :
        return False
 

# for handling dates

from datetime import datetime ,time,timedelta
import pytz
<<<<<<< HEAD
from dateutil.tz import *

local = tzlocal()
=======

>>>>>>> 55fe3e4c34ff151a9c3852917123362152c84fc7

@register.filter(name="status")
def status(question_created_on):

    # Added 10 minutes on database datetime 
<<<<<<< HEAD
    # print(" ##### Created On #####   ",question_created_on)
    add_datetime = question_created_on + timedelta(hours = 60) # difference bw time is 6 hrs : valid for 24 hrs
    current_datetime = datetime.now()
    # print("#### Valid Till ### ",add_datetime)
    # Replace the timezon in both time  

    expired_on = add_datetime.replace(tzinfo = local)
    # print("#### Valid Till ### ",expired_on)

    checked_on = current_datetime.replace(tzinfo = local)
    # print("#### Current Time ####",checked_on)
    print()

    if expired_on < checked_on:
        # print("Time Out")
        return False

    else :
        # print("Time Not Crossed")
        return True

# how to send dict to html file
@register.simple_tag
def remaining_cost(qid,question_created_on):

# difference bw time is 6 hrs : valid for 24 hrs
    add_datetime = question_created_on + timedelta(hours = 10) 
    expired_on = add_datetime.replace(tzinfo = local)
 
    cost = { "ab":qid,"expired_time":expired_on}
    return cost 


"""
How to use below template tag in html
    {% load tags %}

    {% with i.content|split:"\n" as list %}
    {# Iterate the list #}

        {% for li in list  %}

        {{ li}} <p class="mt-1 text-danger"></p>
        {% endfor %}
    {% endwith %}
"""

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)
    
"""
            Configure in html page 
    {% remaining_cost i.id i.created_on  as l %}
    {{l.ab}}  {# accessing key value pair  #}
    {{l.expired_time}}


"""
=======
    print(" 000000000000000000000   ",question_created_on)
    add_datetime = question_created_on + timedelta(hours = 2)
    current_datetime = datetime.now()
    print("333",add_datetime)
    # Replace the timezon in both time

    expired_on = add_datetime.replace(tzinfo = pytz.utc)
    checked_on = current_datetime.replace(tzinfo = pytz.utc)


    if expired_on < checked_on:
        print("Time Out")
        return False

    else :
        print("Time Not Crossed")
        return True

>>>>>>> 55fe3e4c34ff151a9c3852917123362152c84fc7

""" 
And in your template you would use the following:

{% load custom_tags %}

Django provides the following helper functions that allow you to create your own
template tags in an easy manner:

simple_tag: Processes the data and returns a string
inclusion_tag: Processes the data and returns a rendered template
assignment_tag: Processes the data and sets a variable in the context

"""