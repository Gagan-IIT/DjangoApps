from django.shortcuts import render

from .models import Login
from .forms import LoginForm

# Create your views here.
def login_page_view(request):
    form = LoginForm()
    logins = Login.objects.all()
    if(request.method=="POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            form = LoginForm()
        user = request.POST.get("username")
        present = False
        res = ''
        for i in range(len(logins)):
            if(user == logins[i].username):
                present = True
                break
        #print(present)
        if present==True:
            pass_word = request.POST.get("password")
            if pass_word==logins[i].password:
                res ='Correct!'
            else:
                res = "Username/password is invalid."
        else:
                res = "Username/password is invalid."
        #print(res)
        my_context = {
            'res' : res,
            'form': form,
        }
    else:
        my_context = {
            'form' :form
        }
    return render(request, 'login/login_page.html', my_context)