from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from requests.auth import HTTPBasicAuth
import uuid

# Create your views here.


def task_page (request):
    if request.method == "POST":
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']

        auth=HTTPBasicAuth('NetMaster', 'Ylhio65v39aZifol_01')
        uuid_number=uuid.uuid4()

        # auth = {
        #     'user_name': "Netmaster",
        #     'user_password': 'Ylhio65v39aZifol_01'
        # }

        #prints out
        task = {
        "uuid": str(uuid_number),
        "request": 
        [{
            "type": "openShift",
            "operator": 
            {
                "name": "Иванов",
                "vatin": "123654789507"
            }
        }]
        }
        #prints out
        task1 = {
        "uuid": str(uuid_number),
        "request": 
        [{
            "type": "closeShift",
            "operator": 
            {
                "name": "Иванов",
                "vatin": "123654789507"
            }
        }]
        }

        #prints out (X-report)
        task2 = {
        "uuid": str(uuid_number),
        "request": 
        {
            "type": "reportX",  
        }
        }

  
        #sell operation
        task3 = {
            "uuid": str(uuid_number),
            "request": [   
            {
                "type": "sell",
                "items": [ 
                    {
                    "type": "position",
                    "name": "Бананы",
                    "price": 73.15,
                    "quantity": 1,
                    "amount": 73.15,
                    "tax": {
                        "type": "vat20"
                    }
                    },
                    {
                    "type": "text"
                    }

                ],
                "payments":[
                    {
                        "type": "cash",
                        "sum": 73.15
                    }
                ]
            }
        ]
        }
    


        #prints out (cashIn)
        task4 = { 
            "uuid": str(uuid_number),
            "request": {

            "type": "cashIn",

            "operator": {
                "name": "Иванов",
                "vatin": "123654789507"
            },

            "cashSum": 1.0
            }}


        #prints out (X-report)
        task5 = {
            "uuid": str(uuid_number),
            "request": 
            {
                "type": "ismExchangeStatus",  
            }
            }


        try:
            #response=request.post('http://127.0.0.1:16732/api/v2/activateDevice?deviceID=00106109661742')
            response=requests.post('http://127.0.0.1:16732/api/v2/requests', auth=auth, json=task3)

            #response=request.post('http://127.0.0.1:16732/api/v2/operations/queryDeviceInfo?deviceID=00106109661742', auth)


            status_code=response.status_code
            text=response.text
            url=response.url
            json=response.json()

            context = {
                    "status_code" : status_code,
                    "text": text,
                    "url": url,
                    "uuid_number": uuid_number,
                    "json": json
                }

        except:
            messages.error(request, "Сообщение не было отослано.")
            return redirect ('task_page')

        
        return render(request, 'task_page.html', context)
       
    else:
        status_code = '100'
        text = '100'

        context = {
            "status_code" : status_code,
            "text": text,
        }

        return render(request, 'task_page.html', context)

