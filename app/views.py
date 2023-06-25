from django.shortcuts import render, redirect
from django.views import View
from .scrapper.download import get_youtube_video, get_video_quality, get_video_title
from .random_generator import random_personal_id


class IndexPage(View):
    def get(self, request):
        return render(request, template_name='app/index.html')

    def post(self, request):
        context = {}
        video_link = request.POST.get("link") #Video-link entered by the user
        user_video_quality = request.POST.get('quality-list') #Video-quality entered by the user
        maximum_video_quality = get_video_quality(video_link) #Max video quality entered by user
        video_personal_ID = random_personal_id() #This is the video_personal id for a unique names of videos

        try:
            if int(maximum_video_quality[0:-1]) >= int(user_video_quality[0:-1]):
                get_youtube_video(video_link, user_video_quality, video_personal_ID=video_personal_ID)
                context = {'video_downloaded': True,
                           'video_personal_ID': video_personal_ID
                           }
            else:
                context['error'] = 'Видео не подерживает такое качество!'

            return render(request, 'app/index.html', context=context)
        except Exception:
            return redirect('index')
