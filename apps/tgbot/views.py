from .models import StatusCode

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def write_time_code(request):

    from django.http import HttpResponse
    from django.contrib import messages
    status_code = request.GET['status_code']


    if request.method == 'POST' :
        StatusCode.objects.create(
            status_code=status_code
        )
    return HttpResponse(status_code)
    #     video = request.FILES['main_video']
    #     if video.content_type != 'video/mp4':
    #         messages.error(request, 'Файл должен быть видео')
    #         return HttpResponseRedirect('../')
    #     if video.size >= 12000000:
    #         messages.error(request, 'Видео слишком большое, загрузите видео меньше 10Мб')
    #         return HttpResponseRedirect('../')

    #     pp = Path(__file__).parents[3] / 'media/main_video/video.mp4'
    #     pp.parent.mkdir(parents=True, exist_ok=True)

    #     with open(pp, 'wb+') as f:
    #         f.write(video.read())
    #     return HttpResponseRedirect('../')