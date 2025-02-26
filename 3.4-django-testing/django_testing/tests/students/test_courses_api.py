from unittest.mock import MagicMock, patch
import pytest
from rest_framework.test import APIClient 
from students.models import Student, Course
from model_bakery import baker


BASE_URL = '/api/v1/courses/'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    
    return factory

@pytest.mark.django_db
def test_retrive_course(client, course_factory):
    course = course_factory(_quantity=3)
    response = client.get(f'{BASE_URL}{course[1].id}/')
    data = response.json()

    assert response.status_code == 200
    assert course[1].name == data['name']

@pytest.mark.django_db
def test_list_course(client):
    response = client.get(BASE_URL)
    db_count = Course.objects.count()

    assert response.status_code == 200
    assert db_count == len(response.json())

@pytest.mark.django_db
def test_search_id_course(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get(f'{BASE_URL}?id={courses[0].id}')
    data = response.json()
    
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_search_name_course(client, course_factory):
    course = course_factory(_quantity=5)
    response = client.get(f'{BASE_URL}?name={course[3].name}')
    data = response.json()

    assert response.status_code == 200
    assert course[3].name == data[0]['name']

@pytest.mark.django_db
def test_create_course(client, student_factory):
    course_count = Course.objects.count()
    students = student_factory(_quantity=5)
    student_id = [student.id for student in students]
    data = {
        'name': 'Python-разработчик',
        'students': [
            student_id[2],
            student_id[3],
        ]
    }

    response = client.post(BASE_URL, data=data)
    response_get = client.get(f'{BASE_URL}?name=Python-разработчик')
    response_data = response_get.json()

    assert response.status_code == 201
    assert Course.objects.count() == course_count + 1
    assert response_data[0]['students'] == data['students']

@pytest.mark.django_db
def test_remove_course(client, course_factory):
    courses = course_factory(_quantity=5)
    data = {
        'name': 'Java',
    }
    
    response = client.patch(f'{BASE_URL}{courses[2].id}/', data=data)
    response_get = Course.objects.filter(id=courses[2].id).first()

    assert response.status_code == 200
    assert response_get.name == data['name']

@pytest.mark.django_db
def test_destroy_course(client, course_factory):
    courses = course_factory(_quantity=3)
    courses_count = Course.objects.count()
    response = client.delete(f'{BASE_URL}{courses[2].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == courses_count - 1

    