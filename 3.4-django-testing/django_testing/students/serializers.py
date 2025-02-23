from rest_framework import serializers

from students.models import Course
from django.shortcuts import get_object_or_404
from django.conf import settings


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def create(self, validated_data):
        count_st = validated_data.get('students')
        if count_st:
            if len(count_st) > settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError("На курсе не может быть больше 20 студентов")
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        course = get_object_or_404(Course, id=instance.id)
        db_st_count = course.students.count()
        vd_st = validated_data.get("students")
        if vd_st:
            if len(vd_st) + db_st_count >= settings.MAX_STUDENTS_PER_COURSE:
                raise serializers.ValidationError("На курсе не может быть больше 20 студентов")
        return super().update(instance, validated_data)
    
