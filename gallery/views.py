import shortuuid
import base64

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404

from io import BytesIO

from florists.models import Client
from products.models import Bouquet
from gallery.models import FImage

# Create your views here.
@login_required
def all_gallery(request, uuid=None):
    if uuid:
        florist_id = get_object_or_404(Client, uuid=uuid).id
    else:
        florist_id = request.user.fprofile.cli_id

    images = FImage.objects.filter(client_id=florist_id)

    template = 'all_gallery.html'
    template_vars = {'images':images}
    return render(request, template, template_vars)

@login_required
def upload(request):
    florist_id = request.user.fprofile.cli_id

    if request.method == 'POST':
        img_src = request.POST.get('image').split(',')[1]
        img_output = BytesIO()
        img_output.write(base64.b64decode(img_src))  # write the decoded image to buffer
        img_output.seek(0)  # seek the beginning of the image string
        img_file_name = shortuuid.uuid() + '.png'
        img_file = SimpleUploadedFile(img_file_name, img_output.getvalue(), content_type='image/png')
        img = FImage.objects.create(uuid=shortuuid.uuid(), client_id=florist_id, image=img_file, img_main=img_file)
        pos = request.POST.get('pos')

        if 'bouquet' in pos:
            fimg = request.build_absolute_uri(img.img_main.url)
            if '/products/edit' in request.META['HTTP_REFERER']:
                bouquet = Bouquet.objects.get(id=int(pos.split('-')[1]))
            
                try:
                    bouquet.images[int(pos.split('-')[2]) - 1] = fimg
                except:
                    bouquet.images.append(fimg)
                bouquet.save()
            else:
                ilist = request.session.get('new-bouquet-list', [])
                try:
                    ilist[int(pos.split('-')[2]) - 1] = fimg
                except:
                    ilist.append(fimg)
                request.session['new-bouquet-list'] = ilist


        messages.success(request, 'Image Added!')
        return JsonResponse({'success': True})