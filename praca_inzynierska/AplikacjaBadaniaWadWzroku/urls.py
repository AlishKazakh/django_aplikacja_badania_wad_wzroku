from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('tests/', views.tests),
    path('exercises/', views.exercises),
    path('information-diseases/', views.information_diseases),
    path('information-diseases/<value>', views.information_diseases_all, name='information-about-disease'),
    path('tests/astigmatism/', views.test_astigmatism),
    path('tests/color_blindness/', views.test_color_blindness),
    path('tests/macular_degeneration/', views.test_macular_degeneration),
    path('tests/dry_eye/', views.test_dry_eye),
    path('tests/visual_acuity/<eye>/<current_result>', views.test_visual_acuity, name='visual-acuity-test'),
    path('tests/results/<test>/<result>/', views.results, name='results'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)