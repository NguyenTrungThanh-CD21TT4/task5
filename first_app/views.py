from django.shortcuts import render,redirect
from first_app.models import AccessRecord,Topic,Webpage, UserModel
from . import forms
# Create your views here.
#def index(request):
#    my_dict = {'insert_me':'Hello I am from views.py'}
#    return render(request,'index.html',context=my_dict)
#Create your views here.
# def index(request):
#     webpage_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records':webpage_list}
#     return render(request,'index.html',context=date_dict)
def index(request):
    return render(request,'basic_app/index.html')
def form_name_view(request):
    form = forms.ForName() 
    if request.method == 'POST':
        form = forms.ForName(request.POST)
        if form.is_valid():
            print('Validation success!')
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])
            UserModel.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                text = form.cleaned_data['text'],
            )
    return render(request,'basic_app/form.html',{'form':form})
             