from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Kitoblar dokoni API',
        default_version='v1',
        description='List Api Test BOOK',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='anonymousbycreated@gmail.com'),
        license=openapi.License(name='Demo License TEST')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')   
]
