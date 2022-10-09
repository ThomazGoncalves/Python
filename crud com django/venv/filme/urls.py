from django.urls import path

# Importando as views 
from .views import Filme_list, Filme_edit, Filme_delete, Filme_new

urlpatterns = [

     path('', Filme_list.as_view(), name='filmelist'), # Vou listar esses registros
     path('filmenew/', Filme_new.as_view(), name='filmenew'), # Vou criar um novo registro
     path('filmeedit/<int:pk>', Filme_edit.as_view(), name='filmeedit'), # Edição feita através da pk (Primary key)
     path('filmedelete/<int:pk>', Filme_delete.as_view(), name='filmedelete'), # Exclusão feita através da pk (Primary key)



]