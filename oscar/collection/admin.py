from django.contrib import admin
from notifications.signals import notify
from .models import Missed


class MissedAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        notify.send(
            request.user,
            recipient=obj.reported_by,
            verb='updated your report',
            action_object=obj,
            description=obj.notes,
            target=obj
        )
        obj.save()

admin.site.register(Missed, MissedAdmin)
