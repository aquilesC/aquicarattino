from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    name = "aqui_carattino.blog"
    verbose_name = _("Blog")
    #
    # def ready(self):
    #     try:
    #         import aqui_carattino.blog.signals  # noqa F401
    #     except ImportError:
    #         pass
