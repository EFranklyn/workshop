from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    def test_get(self):
        self.assertEqual(200,self.response.status_code)
    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/index.html')
    def test_subscription_link(self):
        self.assertContains(self.response,'href="/subscription/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/about/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/contact/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/elements/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/events/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/news/"')
    def test_about_link(self):
        self.assertContains(self.response, 'href="/speakers/"')


class AboutTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/about/')
    def test_get(self):
        self.assertEqual(200,self.response.status_code)
    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'core/about.html')
