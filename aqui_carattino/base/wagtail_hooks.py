from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from aqui_carattino.base.models import FooterAboutUs


class FooterAboutUsAdmin(ModelAdmin):
    model = FooterAboutUs
    search_fields = ('title', )

modeladmin_register(FooterAboutUsAdmin)
