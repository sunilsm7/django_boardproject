from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.

class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def HomeTests(TestCase):
		view = resolve('/')
		self.assertEquals(view.func, home)