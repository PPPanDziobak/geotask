import json

from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from geoapp.views import GeometryView
from .models import GeometryCoordinatesModel


class GeometryViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        client = Client()
        url = reverse('geoapp:geometry')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'geoapp/home.html')

    def test_post_valid_data(self):
        url = reverse('geoapp:geometry')
        data = {
            'coordinates': '{"x1": 10, "x2": 20, "y1": 30, "y2": 40, "z1": 50, "z2": 60}',
            'projection_plane': 'XY',
        }
        request = self.factory.post(url, data)
        response = GeometryView.as_view()(request)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], 'success')
        self.assertIn('svg_path', response_data)

    def test_post_invalid_data(self):
        url = reverse('geoapp:geometry')
        data = {
            'coordinates': '{"x1": 22.4, "x2": xxx, "y1": aaa, "y2": 40, "z1":22, "z2":55.5"}',
            'projection_plane': 'XY',
        }
        request = self.factory.post(url, data)
        response = GeometryView.as_view()(request)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], 'error')
        self.assertEqual(response_data['message'], 'Invalid JSON data')

    def test_post_invalid_json_data(self):
        url = reverse('geoapp:geometry')
        data = {
            'coordinates': 'invalid_json_data',
            'projection_plane': 'XY',
        }
        request = self.factory.post(url, data)
        response = GeometryView.as_view()(request)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], 'error')
        self.assertEqual(response_data['message'], 'Invalid JSON data')


class GeometryCoordinatesModelTestCase(TestCase):
    def setUp(self):
        self.data = {
            'x1': 10,
            'x2': 20,
            'y1': 30,
            'y2': 40,
            'z1': 50,
            'z2': 60,
        }

    def test_geometry_coordinates_model_creation(self):
        geometry = GeometryCoordinatesModel.objects.create(**self.data)

        self.assertEqual(geometry.x1, self.data['x1'])
        self.assertEqual(geometry.x2, self.data['x2'])
        self.assertEqual(geometry.y1, self.data['y1'])
        self.assertEqual(geometry.y2, self.data['y2'])
        self.assertEqual(geometry.z1, self.data['z1'])
        self.assertEqual(geometry.z2, self.data['z2'])
        self.assertIsNotNone(geometry.created)
        self.assertIsNotNone(geometry.updated)
