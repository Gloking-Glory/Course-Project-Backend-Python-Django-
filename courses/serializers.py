from rest_framework import serializers
from .models import Course
from rest_framework.exceptions import ValidationError

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'course_title', 'university', 'duration', 
            'location', 'fees', 'created_at', 'updated_at'
        ]

    def validate(self, attrs):
        course_title = attrs.get('course_title')
        university = attrs.get('university')

        # only check .id if self.instance exists (update), otherwise None (create)
        course_id = self.instance.id if self.instance else None

        if Course.objects.filter(
            course_title__iexact=course_title.strip(),
            university__iexact=university.strip()
        ).exclude(id=course_id).exists():
            raise ValidationError({
                'error': 'A course with the title already exists in the same university'
            })

        return attrs

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'course_title', 'university', 'duration', 
            'location', 'fees', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'course_title', 'university', 'duration', 
            'location', 'fees'
        ]
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'course_title': {'required': True},
            'university': {'required': True},
            'duration': {'required': True},
            'location': {'required': True},
            'fees': {'required': False},
        }

    def validate(self, attrs):
        course_title = attrs.get('course_title')
        university = attrs.get('university')

        course_id = self.instance.id if self.instance else None

        if Course.objects.filter(
            course_title__iexact=course_title.strip(),
            university__iexact=university.strip()
        ).exclude(id=course_id).exists():
            raise ValidationError({
                'error': 'A course with the title already exists in the same university'
            })

        return attrs
