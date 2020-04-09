from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .models import *


def admin_only(view_func):

    def wrapper_func(request,*args,**kwargs):

        group = None 

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "user":
            messages.info(request,"Only Admin Can Access This Page !!!!.")
            return redirect("total_polls")

        if group == "admin":
            return view_func(request,*args,**kwargs)  
                
        if group == None:
            messages.info(request,"Please Login First !!!!.")
            return redirect("total_polls")
        
             
      

    return wrapper_func    




def voted_already(view_func):

    def wrapper_func(request,*args,**kwargs):
        print("##### >>>",request.user.id)
        print("####### kwargs >>",kwargs['pk'])  # got the question_id as dict

        # get the choices according to the question : using question id 
        # Get the question id from the button on click
        choice = Choice.objects.filter(question = kwargs['pk'])
        logged_in_user = User.objects.get(id=request.user.id) 

        user_list = []  # declaring the empty list
        for i in choice:
            print(i)
            print("$$$#####",i.who_voted) # got the lists of user according to choice

            user_list.append(i.who_voted)
        
        print("### list of list ### ",user_list) # we got list of lists contains [user's list who already voted to that question ]

        ######### converting list of lists into flat list #########

        flat_list = []   # used to store the flaten list values
       
        def remove_nested_list(l): 
            for i in l: 
                if type(i) == list: 
                    remove_nested_list(i)    # using recursion method
                else: 
                    flat_list.append(i)     # if is not a list the append the values

        remove_nested_list(user_list)    # calling the fxn
        print("######## flat list ######",flat_list)    # got the flaten list 

        ############# Now check is the logged_in user is inside the flat_list #######
        if logged_in_user in flat_list :
            messages.info(request,"Your Response Is Already Collected. Please Try Anther Poll Question.")
            return redirect("total_polls")

        if logged_in_user not in flat_list :
            return view_func(request,*args,**kwargs)    

    return wrapper_func   