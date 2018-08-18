from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Q
from django.shortcuts import render, redirect, get_object_or_404

from collections import OrderedDict

from ..models import Bouquet, Filters

def bouquet_shop(request):
    adata = Bouquet.objects.aggregate(Max('price'), Min('price'))

    fdict = OrderedDict()
    for fts in Filters.objects.exclude(parent=None).order_by('parent__text', 'text').prefetch_related('parent'):
        fdict.setdefault(fts.parent.text, []).append([fts.id, fts.text])

    template = 'bouquet_shop.html'
    template_vars = {'adata':adata, 'fdict':fdict}
    return render(request, template, template_vars)

def view_bouquet(request, slug, bid):
    bouquet = get_object_or_404(Bouquet, id=bid)

    mqlist = range(1, bouquet.max_qty + 1)

    template = 'view_bouquet.html'
    template_vars = {'bouquet':bouquet, 'mqlist':mqlist}
    return render(request, template, template_vars)

def ajax_load_bouquets(request):
    if request.method == 'POST':
        rp = request.POST
        try:
            plist = list(map(int, rp.get('price', '').split(',')))
        except:
            plist = [0, 0]

        bfilter = Q(price__gte=plist[0], price__lte=plist[1])

        if rp.getlist('days'):
            bfilter &=Q(cli__days__overlap=rp.getlist('days'))
        
        for k, v in rp.items():
            if 'filters' in k:
                bfilter &= Q(filters__in=list(map(int,rp.getlist(k))))
        
        bouquets = Bouquet.pub_objects.filter(bfilter)

        template = '__ajax_load_bouquets.html'
        template_vars = {'bouquets':bouquets}
        return render(request, template, template_vars)

def ajax_manage_cart(request):
    if request.method == 'POST':
        import pdb; pdb.set_trace()