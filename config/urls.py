from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from garagem.views import CategoriaViewSet, EditoraViewSet, LivroViewSet, AutorViewSet
from usuario.router import router as usuario_router
from uploader.router import router as uploader_router

router = DefaultRouter()
router.register("categorias", CategoriaViewSet)
router.register("editoras", EditoraViewSet)
router.register("livro", LivroViewSet)
router.register("autor", AutorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls))
    
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)