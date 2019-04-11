from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm

class SubscriptionTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/subscription/')
    def test_get(self):
        self.assertEqual(200,self.response.status_code)
    def test_template_used(self):
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')

    def test_html_form(self):
        tags = (('form',10),
                ('<input',6),
                ('type="text',11),
                ('type="email"',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response,text, count)

    def test_csrf_token(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):

        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)