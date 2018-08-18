from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from collections import OrderedDict

from ..forms import BouquetForm
from ..models import Bouquet, Filters

# Create your views here.
@login_required
def all_products(request):
    if request.user.groups.first().name == 'ADMIN':
        prods = []
    else:
        florist_id = request.user.fprofile.cli_id
        prods = Bouquet.objects.filter(cli_id=florist_id)
        
    template = 'all_products.html'
    template_vars = {'prods':prods}
    return render(request, template, template_vars)

@login_required
def edit_bouquet(request, uuid=None):
    if uuid:    
        bouquet = get_object_or_404(Bouquet, uuid=uuid)
    else:
        bouquet = Bouquet()

    form = BouquetForm(instance=bouquet)

    fdict = OrderedDict()
    for fts in Filters.objects.exclude(parent=None).order_by('parent__text', 'text').prefetch_related('parent'):
        fdict.setdefault(fts.parent.text, []).append([fts.id, fts.text])

    flist = list(bouquet.filters.all().values_list('id', flat=True))

    if request.method == "POST":
        rp = request.POST
        if not uuid:
            bouquet.cli_id = request.user.fprofile.cli_id

        bouquet.max_qty = rp.get('max_qty')
        bouquet.name = rp.get('name')
        bouquet.price = rp.get('price')
        bouquet.upprice = rp.get('upprice')
        bouquet.size = rp.get('size') 
        bouquet.upsize = rp.get('upsize')
        bouquet.description = rp.get('description')
        bouquet.save()

        filters = list(map(int, rp.getlist('filters')))
        print(filters)

        bouquet.filters.add(*filters)
        bouquet.filters.remove(*bouquet.filters.exclude(id__in=filters))

        messages.success(request, 'Bouquet Updated!')
        return redirect('edit-bouquet', bouquet.uuid)

    template = 'edit_bouquet.html'
    template_vars = {'bouquet':bouquet, 'form':form, 'fdict':fdict, 'flist':flist}
    return render(request, template, template_vars)