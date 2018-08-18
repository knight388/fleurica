from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from florists.forms import ClientForm
from florists.models import Client
from userprofiles.models import FProfile

# Create your views here.
def florist_signup(request):
    if request.method == 'POST':
        rp = request.POST
        if not rp.get('honeypot'):
            cli, created = Client.objects.get_or_create(bname = rp.get('bname'), con_name = rp.get('name'),
                                        con_email = rp.get('email'), con_number = rp.get('contact'))

        messages.success(request, "Signup successful!")
        return redirect('florist-signup')


    template = 'florist_signup.html'
    template_vars = {}
    return render(request, template, template_vars)

@login_required
def all_florists(request):

    if 'all' in request.path:
        florists = Client.objects.exclude(status=4)
    else:
        florists = Client.objects.filter(status=4)

    template = 'all_florists.html'
    template_vars = {'florists':florists}
    return render(request, template, template_vars)

@login_required
def edit_florist(request, uuid):
    florist = get_object_or_404(Client, uuid=uuid)
    form = ClientForm(instance=florist)

    wlist = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    olist = [8,9,10,11]
    clist = [5,6,7,8]

    if request.method == 'POST':
        form = ClientForm(request.POST or None, instance=florist)
        if form.is_valid():
            florist = form.save(commit=False)
            florist.days = request.POST.getlist('days')
            florist.hours = request.POST.getlist('hours')
            florist.logo = request.FILES.get('logo')
            florist.banner = request.FILES.get('banner')
            florist.questions = request.POST.getlist('questions')
            florist.save()

            messages.success(request, "Florist updated!")
            return redirect('edit-florist', uuid)


    template = 'edit_florist.html'
    template_vars = {'florist':florist, 'form':form, 'wlist':wlist, 'olist':olist, 'clist':clist}
    return render(request, template, template_vars)

@login_required
def ajax_confirm_f(request):
    if request.method == 'POST':
        fid = request.POST.get('fid')
        florist = Client.objects.get(id=fid)

        user = User.objects.create(email=florist.con_email, first_name=florist.con_name)
        user.set_password('Password@8')
        user.save()
        grp = Group.objects.get(name='FLORIST')
        user.groups.add(grp)
        FProfile.objects.create(user=user,cli=florist)

        florist.status = 3
        florist.save()

        return JsonResponse({'success': True})
