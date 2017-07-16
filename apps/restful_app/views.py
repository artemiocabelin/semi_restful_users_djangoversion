from django.shortcuts import render, redirect, HttpResponse
from .models import User


# Create your views here.
# a GET request to /users - calls the index method to display all the users. This will need a template.
def users(request):
    all_users = User.objects.values()
    context = {
        'all_users' : all_users
    }
    return render(request, 'restful_app/index.html', context)

# GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
def show(request,user_id):
    user = User.objects.get(id=user_id)
    full_name = str(user.first_name)+' '+str(user.last_name)
    context = {
        'user_id'   : user_id,
        'full_name' : full_name,
        'email'     : user.email,
        'created_at': user.created_at
    }
    return render(request, 'restful_app/show_user.html', context)

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
def destroy_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/users')

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
def new(request):
    return render(request, 'restful_app/add_user.html')

# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
def create_process(request):
    if request.method == 'POST':
        new_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        new_user.save()
        new_id = new_user.id  
    return redirect('/users/'+str(new_id))

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user_id'   : user_id,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email'     : user.email
    }
    return render(request, 'restful_app/edit_user.html', context)

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
def edit_process(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user_id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        show_id = user.id  
    return redirect('/users/'+str(show_id))


