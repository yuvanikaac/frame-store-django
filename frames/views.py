from django.shortcuts import redirect, render

from .models import FrameVariant
from .models import CustomerUpload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def frame_list(request):

    sizes = FrameVariant.objects.values_list(
        'size',
        flat=True
    ).distinct()

    selected_size = request.GET.get('size')

    selected_orientation = request.GET.get(
        'orientation'
    )

    frame_variants = FrameVariant.objects.all()

    if selected_size:

        frame_variants = frame_variants.filter(
            size=selected_size
        )

    if selected_orientation:

        frame_variants = frame_variants.filter(
            orientation=selected_orientation
        )

    context = {

        'frame_variants': frame_variants,

        'sizes': sizes,

        'selected_size': selected_size,

        'selected_orientation': selected_orientation,
    }

    return render(
        request,
        'frames/frame_list.html',
        context
    )

def frame_detail(request, variant_id):

    variant = FrameVariant.objects.get(
        id=variant_id
    )

    context = {
        'variant': variant
    }

    return render(
        request,
        'frames/frame_detail.html',
        context
    )
def upload_photo(request, variant_id):

    variant = FrameVariant.objects.get(
        id=variant_id
    )

    if request.method == 'POST':

        photo = request.FILES.get(
            'photo'
        )

        if photo:

            upload = CustomerUpload.objects.create(

                user=request.user,

                frame_variant=variant,

                photo=photo,

                status='TEMP'
            )

            return redirect(
                'preview_frame',
                upload_id=upload.id
            )

    context = {
        'variant': variant
    }

    return render(
        request,
        'frames/upload_photo.html',
        context
    )

    
def preview_frame(request, upload_id):

    upload = CustomerUpload.objects.get(
        id=upload_id
    )

    context = {
        'upload': upload
    }

    return render(
        request,
        'frames/preview.html',
        context
    )
from django.http import HttpResponse

def wall_preview(request, upload_id):

    upload = CustomerUpload.objects.get(
        id=upload_id
    )

    context = {
        'upload': upload
    }

    return render(
        request,
        'frames/wall_preview.html',
        context
    )
@csrf_exempt
def save_preview(request, upload_id):

    if request.method == 'POST':

        upload = CustomerUpload.objects.get(
            id=upload_id
        )

        upload.position_x = request.POST.get(
            'position_x',
            0
        )

        upload.position_y = request.POST.get(
            'position_y',
            0
        )

        upload.zoom_level = request.POST.get(
            'zoom_level',
            1
        )

        upload.save()

        return JsonResponse({
            'success': True
        })

    return JsonResponse({
        'success': False
    })