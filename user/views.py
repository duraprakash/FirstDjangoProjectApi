from django.shortcuts import HttpResponse, render
from django.http import JsonResponse

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

# retrieve all user list
def list_user(request):
    return JsonResponse(users, safe=False)

# retrieve user by id
def retrieve_user(request, userId):
    user = None
    for i in users:
        if i["id"] == userId:
            user = i
            break
    return JsonResponse(user, safe=False)

# update user by id
def update_user(request, userId):
    user = None
    for i in users:
        if i["id"] == userId:
            user = i
            users.remove(user)
            break

    if user:
        if user["marital_status"] == False:
            user["marital_status"] = True
        else:
            user["marital_status"] = False

        users.append(user)
        return JsonResponse(user, safe=False)
    else:
        return JsonResponse({"message": "User Not Found"}, safe=False)

# delete user by id
def delete_user(request, userId):
    user = None
    for i in users:
        if i["id"] == userId:
            user = i
            users.remove(user)
    
    if user:
        return JsonResponse({"message":"User deleted successfully"}, safe=False)
    else:
        return JsonResponse({"message":"User Not Found"}, safe=False)
    
# work with database and ORM
from .models import User

def list_db_user(request):
    try:
        db_users = User.objects.all()
        response_user = []
        for i in db_users:
            response_user.append(
                {
                    "id": i.pk,
                    "name": i.name,
                    "age": i.age,
                    "matital_status": i.marital_status,
                }
            )

        return JsonResponse(response_user, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"message":"User Not Found"}, safe=False)
    
def retrieve_db_user(request, userId):
    try:
        user = User.objects.get(id=userId)
        return JsonResponse(
            {
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "marital_status": user.marital_status,
            },
            safe=False
        )
    except User.DoesNotExist:
        return JsonResponse({"message":"User Not Found"}, safe=False)
    
def update_db_user(request, userId):
    try:
        user = User.objects.get(id=userId)
        
        # if user.marital_status == True:
        #     user.marital_status = False
        # else:
        #     user.marital_status = True

        user.marital_status = not user.marital_status
        
        user.save()
        return JsonResponse(
            {
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "marital_status": user.marital_status,
            },
            safe=False
        )
    except User.DoesNotExist:
        return JsonResponse({"message": "User Not Found"}, safe=False)
    

def delete_db_user(request, userId):
    try:
        user = User.objects.get(id=userId)

        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, safe=False)
    except User.DoesNotExist:
        return JsonResponse({"message":"User Not Found"}, safe=False)