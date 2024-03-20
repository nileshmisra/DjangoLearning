from django.shortcuts import render
from django.http import HttpResponse

#1
# returning simple string
def home1(request):
    return HttpResponse("home page of project")


#2
#returning html response
#but this is not a clean code so we prefer template to write html in it
def home2(request):
    return HttpResponse("""<h1>home page of project</h1>
                        <hr>
                        <p style="color:red">lets start coding</p>""")


#3
#so to render html here we will return static content of html file present in templates
def home3(request):
    return render(request,"home/home3.html")

#4
# to pass dynamic data i.e from server to template we will use context
def home4(request):
    peoples=[
        {"name":"n1","age":10},
        {"name":"n2","age":11},
        {"name":"n3","age":12},
        {"name":"n4","age":13},
        {"name":"n5","age":14},
        {"name":"n6","age":15},
    ]
    text= """Lorem ipsum dolor, sit amet consectetur adipisicing elit.
            Sapiente debitis consequuntur commodi. Ea explicabo perspiciatis tenetur,
                maxime eligendi qui consectetur illum quam dolores dolore incidunt hic ab 
                quae architecto delectus.
            """
    
    dict1={"peoples":peoples,"text":text}
    return render(request,"home/home4.html",context=dict1)

#5
#home,about,contact page
def home(request):
    context = {"page":"Home"}  ##to display dynamically name of the page in browser tab
    return render(request,"home/index.html",context)

def about(request):
    context = {"page":"About"}
    return render(request,"home/about.html",context)

def contact(request):
    context = {"page":"Contact"}
    return render(request,"home/contact.html",context)