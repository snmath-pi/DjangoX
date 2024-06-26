from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# All logical things done here

def home(request):
    peoples = [
        {'name': 'Abhijeet', 'age': 25},
        {'name': 'Rohan', 'age': 24},
        {'name': 'Vicky', 'age':16},
        {'name': 'Depanshu', 'age': 25},
        {'name': 'Sandeep', 'age': 17},
    ]
    
    # text = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit, molestias! Consequatur amet quod sit debitis ipsum. Itaque magni eaque optio nostrum architecto voluptates laborum commodi nihil doloremque, ipsum expedita aut consequatur? Architecto, repellendus maxime nostrum eius magnam corporis ullam voluptate eligendi cum, accusantium quas debitis asperiores animi mollitia blanditiis tempora enim. Dolore quo ut nemo corrupti dolorum, necessitatibus et totam? Blanditiis nihil placeat repellat exercitationem architecto vitae sint nostrum! Dolorem, beatae accusantium excepturi possimus non, nisi ipsam, quas cumque impedit deserunt dolores culpa? Saepe enim ipsa maiores? Adipisci et expedita dignissimos! Dolorum ipsa quia voluptate asperiores, distinctio non consectetur ex."""
    
    vegetables = ['Pumpking', 'Tomato', 'Potato']
    
    return render(request, "index.html",context={'page': 'Home', 'peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'page':'About'}
    return render(request, "about.html", context)
def contact(request):
    context = {'page': 'Contact'}
    return render(request, "contact.html", context)


# def success_page(request):
#     print("*"*10)
#     return HttpResponse("<h1>Hey This is a success page</h1>")

