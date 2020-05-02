from django.shortcuts import render
from django.contrib import messages
import requests
import json
# Create your views here.

def index(request):
    
    if request.method == "POST":
        try:

            key = "1198d782cf073589af04226432888e4f"
            city = request.POST.get('city')

            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"	)
            data = response.json()
            
            coord = data['coord']
            weather = data['weather']
            base = data['base']
            main = data['main']
      
            name = data['name']
            timezone = data['timezone']
        
            context = {
                    "data":data,
                    "coord":coord,
                    "weather":weather,
                    "base":base,
                    "main":main,
                    "clouds": data['clouds']['all'],
                    "name":name,
                    "timezone":timezone  }
            return render(request,'weather/index.html',context)

        except:

            messages.error(request,"Sorry For Inconvience. Something Went Wrong..! Try Another Loacation..")
            return render(request,'weather/index.html')


    return render(request,'weather/index.html')