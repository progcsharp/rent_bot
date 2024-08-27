from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .forms import ModerForm, AddModerForm, SearchModerForm
from .models import TgUser, Info, Moder, Message


@csrf_exempt
@login_required(login_url='/admin/')
def index(request, f="not"):
    users = TgUser.objects.all()
    form = ModerForm()
    add_form = AddModerForm()
    search = SearchModerForm()
    print(f)
    error = ''
    if request.method == "POST":
        if f == "save":
            try:
                add_form = AddModerForm(request.POST)
                add_form.save()
                add_form = AddModerForm()
            except ValueError as e:
                error = "Нельза создать пользователей с одинаковым паролем"
                add_form = AddModerForm()
        if f == "edit":
            form = ModerForm(request.POST)
            user = TgUser.objects.get(id=form['id'].value())
            form = ModerForm(request.POST, instance=user)
            form.save()
        if f == "search":
            search = SearchModerForm(request.POST)
            if search['name'].value():
                print(search['name'].value())
                name = str(search["name"].value())
                users = TgUser.objects.filter(name_lower__icontains=name)
    return render(request, 'index.html', {"users": users, "form": form, "add_form": add_form, "search": search, "error": error})


@csrf_exempt
@login_required(login_url='/admin/')
def info(request):
    info = Info.objects.get(id=1)
    if request.method == "POST":
        print(dict(request.POST)["article"][0])
        info.title = dict(request.POST)["title"][0]
        info.article = dict(request.POST)["article"][0]
        info.save()
    return render(request, 'info.html', {"info": info})


@csrf_exempt
@login_required(login_url='/admin/')
def setting(request):
    moder = Moder.objects.get(id=1)
    message_reg = Message.objects.get(id=1)
    message_bonus = Message.objects.get(id=2)
    message_info = Message.objects.get(id=3)
    if request.method == "POST":
        form = list(dict(request.POST).keys())[0]
        if form == "moder":
            moder.tg_id = dict(request.POST)["moder"][0]
            moder.save()
        elif form == "message_reg":
            message_reg.message = dict(request.POST)["message_reg"][0]
            message_reg.save()
        elif form == "message_bonus":
            message_bonus.message = dict(request.POST)["message_bonus"][0]
            message_bonus.save()
        elif form == "message_info":
            message_info.message = dict(request.POST)["message_info"][0]
            message_info.save()
        print(list(dict(request.POST).keys())[0])

    return render(request, 'settings.html', {'moder': moder.tg_id, "message_reg": message_reg,
                                             "message_bonus": message_bonus, "message_info": message_info})
