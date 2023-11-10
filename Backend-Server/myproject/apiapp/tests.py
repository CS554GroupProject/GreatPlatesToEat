import unittest
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.http import QueryDict
from django.urls import reverse
from .forms import RequestForm  
from .models import UserRequest  
from .views import log_request 

class Request_Unit_Test(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        #self.user = User.objects.create_user(username='JAlsaiari', password='Ja@12345')

    def valid_test_for_logRequest(self):
        data = {'user_name': 'Jawaher Alsaiari', 'log_test': 'This is a valid test', 'recipes_to_receive': 5}
        request = self.factory.post(reverse('apiapp:log_request'), data)
        

        with unittest.mock.patch('apiapp.views.create_user_request') as mock_create_user_request:
            response = log_request(request)

        mock_create_user_request.assert_called_once_with(self.user, data)
        self.assertEqual(response.status_code, 302)

    def invalid_test_for_logRequest(self):
        data = {'user_name': 'Jawaher Alsaiari', 'request_text': 'This is a valid test', 'recipes_to_receive': 'invalid'}
        request = self.factory.post(reverse('apiapp:log_request'), data)
        request.user = self.user

        with unittest.mock.patch('apiapp.views.create_user_request') as mock_create_user_request:
            response = log_request(request)

        mock_create_user_request.assert_not_called()
        self.assertEqual(response.status_code, 200)

    def valid_test_for_logRequest_get(self):
        request = self.factory.get(reverse('apiapp:log_request'))
        request.user = self.user

        response = log_request(request)

        self.assertEqual(response.status_code, 200) 
        self.assertIsInstance(response.context['form'], RequestForm)

    def test_create_user_request(self):
        #user = User.objects.create_user(username='secondUser', password='Pass@123')
        form_data = {'user_name': 'Jawaher Alsaiari','request_text': 'This is a valid test', 'recipes_to_receive': 3}

        create_user_request(form_data)

        self.assertEqual(UserRequest.objects.count(), 1)
        user_request = UserRequest.objects.first()
        self.assertEqual(user_request.request, form_data['user_name'])
        self.assertEqual(user_request.request, form_data['request_text'])
        self.assertEqual(user_request.recipes_to_receive, form_data['recipes_to_receive'])


if __name__ == '__main__':
    unittest.main()
