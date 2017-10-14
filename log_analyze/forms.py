from django import forms


class LogMonitorForm(forms.Form):
	TOPIC_CHOICES = (
		('type1','userLog'),
		('type2','payLog'),
	)
	logType = forms.ChoiceField(choices=TOPIC_CHOICES)
	logPath = forms.CharField()
	timing = forms.IntegerField()