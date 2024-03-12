from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
# for post method csrf token
from django.views.decorators.csrf import csrf_exempt
import json

# list
users = [
    {
        "id": 1,
        "name": "Ganesh Thapa",
        "age": 24,
        "marital_status": False
    },
    {
        "id": 2,
        "name": "Hari Bdr Gurung",
        "age": 18,
        "marital_status": False
    },
    {
        "id": 3,
        "name": "James Bond",
        "age": 28,
        "marital_status": True
    },
    {
        "id": 4,
        "name": "Jennifer Lopez",
        "age": 26,
        "marital_status": True
    },
]

def list_user(request):
    return JsonResponse(users, safe=False)

def retrieve_user(request, userId):
    user = None # empty list
    for i in users: # looping
        if i["id"] == userId: # match the given id
            user = i # store if matched
            break
    return JsonResponse(user, safe=False) # return the result

def update_user(request, userId):
    user = None # empty list
    for i in users: # looping
        if i["id"] == userId: # match the given id
            user = i # store if matched
            users.remove(user) # remove the data from actual data list
            break

    if user is not None: # user list not null
        # True if user["marital_status"] == False else False
        # change their marital_status reversly
        if user["marital_status"] == False:
            user["marital_status"] == True
        else:
            user["marital_status"] = False

        users.append(user) # replace the original data with edited data
        return JsonResponse(user, safe=False) # return the result

def delete_user(request, userId):
    user = None # emply list
    for i in users: # looping
        if i["id"] == userId: # match the given id
            user = i # store if matched
            users.remove(user) # remove the data from the actual data list
            break

    if user: # if user is found
        return JsonResponse({"message":f"User with id {userId} is deleted."} , safe=False)
    else:
        return JsonResponse({"message":f"Record Not Found"}, safe=False)