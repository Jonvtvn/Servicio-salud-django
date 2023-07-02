from django.urls import path


from . import views


urlpatterns = [
   
    path('index/', views.vistageneral, name='index'),
    path('', views.vistageneral),
    path('lista_cursos_fun/', views.lista_cursos_funcionarios),
    #path('login_operador/', views.user_login,name='login_operador'),
    path('mod_index/',views.modificar_index ,name='mod_index'),
    path('cursos_add/',views.ingresar_cursos),
    path('consultas/',views.lista_consultas_operador),
    path('consultas_cursos/',views.form_consulta),
    path('resgitrar/',views.registrar, name='personal'),
    path('logout/',views.logout_view, name='logout' ),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('<path:route>/', views.pagina_no_encontrada, name='pagina_no_encontrada'),



] 

