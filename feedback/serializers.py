from rest_framework import serializers
from .models import Feedback


class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id','phone_number', 'info_text', 'created_at')

