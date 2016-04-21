import floppyforms.__future__ as forms
from datetime import datetime, timedelta, time
from .models import Missed


class MissedBinForm(forms.ModelForm):

    class Meta:
        model = Missed
        fields = ()

    def clean(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())

        reports = Missed.objects.filter(created__gte=today_start).filter(created__lte=today_end)
        if reports.exists():
            raise forms.ValidationError(
                "You have already created a missed bin report for {today}".format(today=today)
            )
