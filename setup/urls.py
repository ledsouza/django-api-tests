from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers, permissions
from aluraflix.views import ProgramaViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

schema_view = get_schema_view(
    openapi.Info(
        title="Aluraflix",
        default_version='v1',
        description="Provedor de filmes e séries local desenvolvido pela Alura",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@alura.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
