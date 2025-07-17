from dis import Positions

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from app_run.models import Run, AthleteInfo, Challenge

User = get_user_model()


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name', ]


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(read_only=True, source='athlete')

    class Meta:
        model = Run
        fields = '__all__'
        read_only_fields = ['status']


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'last_name', 'first_name', 'type', 'runs_finished', ]

    def get_type(self, obj):
        return 'coach' if obj.is_staff else 'athlete'

    def get_runs_finished(self, obj):
        return obj.run_set.filter(status='finished').count()


class AthleteInfoUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class AthleteInfoSerializer(serializers.ModelSerializer):
    athlete = AthleteInfoUser(read_only=True, source='user_id')

    class Meta:
        model = AthleteInfo
        fields = '__all__'

    def validate_weight(self, value):
        if value <= 0 or value >= 900:
            raise serializers.ValidationError('Неправильный вес')
        return value


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'
        read_only_fields = ['athlete']


class PositionsRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ["id"]


# class PositionsSerializer(serializers.ModelSerializer):
#     # run = PositionsRunSerializer()
#
#     class Meta:
#         model = Position
#         fields = '__all__'
#
#     def validate_latitude(self, value):
#         if value < -90.0000 or value > 90.0000:
#             raise serializers.ValidationError("Широта в не допустимом диапазоне")
#         return value
#
#     def validate_longitude(self, value):
#         if value < -180.0000 or value > 180.0000:
#             raise serializers.ValidationError("Долгота в не допустимом диапазоне")
#         elif len(str(value).split('.')[-1]) > 4:
#             raise serializers.ValidationError('Количество знаков после запятой не должно превышать пяти символов.')
#         return value
#
#     def validate_run(self, value):
#         run_obj = get_object_or_404(Run, id=value.id)
#         if run_obj.status != 'in_progress':
#             raise serializers.ValidationError('Забег не должен быть завершенным или запущенным')
#         return value