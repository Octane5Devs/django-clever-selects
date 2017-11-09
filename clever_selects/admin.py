
from django.contrib.admin import ModelAdmin

class ChainedSelectAdminMixin(ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super(ChainedSelectAdminMixin, self).get_form(request, obj, **kwargs)
        if request.user:
            form.user = request.user
        return form
