from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('show-all-teachers/', views.show_all_teachers, name='show-all-teachers'),
    path('add-teacher/', views.add_teacher, name='add-teacher'),
    path('filter-teachers/', views.filter_teachers, name='filter-teachers'),
    path('search-teacher/', views.search_teacher, name='search-teacher'),
    path('update-teacher/', views.update_teacher, name='update-teacher'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete-teacher/', views.delete_teacher, name='delete-teacher'),
    path('calculate-avg/', views.calculate_avg, name='calculate-avg'),
    path('download-json', views.download_json, name='download-json'),
    path('import-json', views.import_json, name='import-json')
]
