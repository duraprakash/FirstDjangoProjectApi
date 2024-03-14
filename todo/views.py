from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
# for post method csrf token
from django.views.decorators.csrf import csrf_exempt
import json
# for storing in database
from .models import Todo

def hello_view(request):
    user = {
        "name": "Prakash",
        "age": 22
        }
    
    print(type(user))
    return JsonResponse(user)


def yview(request):
    count = 0
    count += 1
    return HttpResponse(f"<h1><marquee>Mail Sent Successfully {count}</marquee></h1>")

def home_view(request):
    return render(request, "index.html")

todos = [
    {
        "userId": 1,
        "id": 1,
        "title": "Buy milk",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "Buy coffee",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "Buy flower",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "Buy pen",
        "completed": True
    },
]  

def list_todo(request):
    db_todos = Todo.objects.all() # returns query sets from database records
    # print(db_todos.query) # show the sql code
    # db_todos = Todo.objects.get() # get only one
    response_todo = [] # empty list
    print(db_todos)
    # convert into dict for simplicity
    for i in db_todos:
        response_todo.append(
            {"id": i.pk, "title": i.title, "completed":i.completed, "created_at":i.created_at}
        )
    # return JsonResponse(todos, safe=False)
    return JsonResponse(response_todo, safe=False)

# def retrieve_todo(request, todoId):
#     # # yesterday
#     # print(f"TodoId:{todoId}")

#     # todo = None

#     # for i in todos:
#     #     if i["id"] == todoId:
#     #         todo = i
#     #         break

#     # print(todo)

#     # return JsonResponse(todo, safe=False)

#     todo = Todo.objects.get(id=todoId)
#     return JsonResponse(
#         {
#             "id": todo.pk,
#             "title": todo.title,
#             "completed": todo.completed,
#             "created_at": create_todo,
#         },
#         safe=False,
#     )

def retrieve_todo(request, todoId):
    try:
        todo = Todo.objects.get(id=todoId)
        return JsonResponse(
            {
                "id": todo.pk,
                "title": todo.title,
                "completed": todo.completed,
                "created_at": todo.created_at,
            },
            safe=False,
        )
    except Todo.DoesNotExist:
        return JsonResponse({"message": "Todo not found"}, status=404)

# def update_todo(request, todoId):
#     print(f"TodoId:{todoId}")

#     # shows in byte
#     print(request.body)

#     todo = None

#     for i in todos:
#         if i["id"] == todoId:
#             todo = i
#             todos.remove(todo)
#             break

#     if todo is not None:
#         # change their state reversly
#         if todo["completed"] == True:
#             todo["completed"] = False
#         else:
#             todo["completed"] = True

#         todos.append(todo)
#         return JsonResponse(todo, safe=False)
#     else:
#         return JsonResponse({"message": "Not Found"}, safe=False)

def update_todo(request, todoId):
    try:
        todo = Todo.objects.get(id=todoId)

        if todo.completed == True:
            todo.completed = False
        else:
            todo.completed = True

        todo.save()
        return JsonResponse(
            {
                "title": todo.title,
                "completed": todo.completed,
                "created_at": todo.created_at,
            },
            safe=False,
        )
    except Todo.DoesNotExist:
        return JsonResponse({"Message": "Todo not found"})
    
def delete_todo(request, todoId):
    try:
        todo = Todo.objects.get(id=todoId)
        todo.delete()
        return JsonResponse(
            {"message":"Todo deleted successfully"},safe=False,
        )
    except Todo.DoesNotExist:
        return JsonResponse({"message": "Todo not found"}, status=404)

# @csrf_exempt
# def create_todo(request):
#     if request.method == "POST":
#         # Extract data from request body
#         data = json.loads(request.body.decode())

#         # # dummy data
#         # new_todo = {
#         #     "userId": 2,
#         #     "id": 5,
#         #     "title": "Buy notebook",
#         #     "completed": False
#         # }

#         # Get values from request body or parameters
#         userId = data.get("userId")
#         title = data.get("title")
#         completed = data.get("completed", False)

#         # Create new todo dictionary
#         new_todo = {
#             "userId": userId,
#             "id": len(todos) + 1,
#             "title": title,
#             "completed": completed
#         }

#         todos.append(new_todo)
#         print(new_todo)
#         print(data)
#         return JsonResponse(new_todo, status=201)
#     else:
#         return JsonResponse({"message":"Method not allowed"}, status=405)
    
## giveing null while inserting data
# @csrf_exempt
# def create_todo(request):
#     if request.method == 'POST':
#         userId = request.POST.get("userId")
#         title = request.POST.get("title")
#         completed = request.POST.get("completed", False)

#         new_todo = {
#             "userId": userId,
#             "id": len(todos) + 1,
#             "title": title,
#             "completed": completed
#         }
#         todos.append(new_todo)
#         return JsonResponse(new_todo, status=201)
#     else:
#         return render(request, "index.html")


# # works with postman
# @csrf_exempt
# def create_todo(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         userId = data.get("userId")
#         title = data.get("title")
#         completed = data.get("completed", False)

#         new_todo = {
#             "userId": userId,
#             "id": len(todos) + 1,
#             "title": title,
#             "completed": completed
#         }
#         todos.append(new_todo)
#         return JsonResponse(new_todo, status=201)
#     else:
#         return JsonResponse({"message":"Method not allowed"}, status=405)


# works with postman
@csrf_exempt
def create_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get("title")
        completed = data.get("completed", False)

        new_todo = Todo.objects.create(title=title, completed=completed)
        new_todo.save()
        return JsonResponse(
            {
                "title" : new_todo.title,
                "completed" : new_todo.completed,
                "created" : new_todo.created_at,
            },
            status=201
        )
    else:
        return JsonResponse({"message":"Method not allowed"}, status=405)

