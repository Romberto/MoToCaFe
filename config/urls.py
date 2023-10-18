
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from category.views import CategoryViewSet
from product.views import ProductViewSet

router = SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('api-my_auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('', include('category.urls')),
    path('panel/', include('admin_p.urls'))

]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]


