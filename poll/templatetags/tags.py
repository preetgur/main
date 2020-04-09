
from django import template
from django.contrib.auth.models import Group

register = template.Library()




@register.filter(name="is_admin")    # "is_admin" is a filter name it can be named different form fxn name
def has_group(logged_in_user,arg1):
    print("!!!!!!!!!!!! custom tags :  :",logged_in_user)
    print("### data get from template ###",arg1)  
    #  is_admin:"gurpreet" ,gurpreet store in arg1

    
    
    if logged_in_user.groups.filter(name='admin').exists():

        return True

    else :
        return False
 

# for handling dates

from datetime import datetime ,time,timedelta
import pytz


@register.filter(name="status")
def status(question_created_on):

    # Added 10 minutes on database datetime 
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


""" 
And in your template you would use the following:

{% load custom_tags %}

Django provides the following helper functions that allow you to create your own
template tags in an easy manner:

simple_tag: Processes the data and returns a string
inclusion_tag: Processes the data and returns a rendered template
assignment_tag: Processes the data and sets a variable in the context

"""