# project/tests/test_users.py

import json
from project.tests.base import BaseTestCase
from project.api.models import User 
from project import db
from project.tests.utils import add_user



class TestUserService(BaseTestCase):
    """ Test for users service """
    def test_users(self):
        """ Ensure the /ping route behaves perfectly """
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertTrue(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn("success", data["status"])

    def test_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='michael',
                    email='michael@realpython.com'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('paulampurire@gmail.com was added!', data['message'])
            self.assertIn('success', data['status'])


    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
            '/users',
            data=json.dumps(dict()),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid payload.', data['message'])
        self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key."""
        with self.client:
            response = self.client.post(
            '/users',
            data=json.dumps(dict(email='petertahinduka@gmail.com')),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid payload.', data['message'])
        self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        """ Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
            '/users',
            data=json.dumps(dict(
                username='peter',
                email='petertahinduka@gmail.com'
            )),
            content_type='application/json',
        )
            response = self.client.post(
            '/users',
            data=json.dumps(dict(
                username='peter',
                email='petertahinduka@gmail.com'
            )),
            content_type='application/json',
        )
        
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Sorry. That email already exists.', data['message'])
        self.assertIn('fail', data['status'])

    def test_single_user(self):
        """ Ensure that the get user route behaves correctly """
        user = add_user('michael', 'michael@realpython.com')
        db.session.add(user)
        db.session.commit()

        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data'])
            self.assertIn('michael', data['data']['username'])
            self.assertIn('michael@realpython.com', data['data']['email'])
            self.assertIn('success', data['status'])         
    
    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])
    
    def test_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user('michael', 'michael@realpython.com')
        add_user('fletcher', 'fletcher@realpython.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertTrue('created_at' in data['data']['users'][0])
            self.assertTrue('created_at' in data['data']['users'][1])
            self.assertIn('michael', data['data']['users'][0]['username'])
            self.assertIn(
            'michael@realpython.com', data['data']['users'][0]['email'])
            self.assertIn('fletcher', data['data']['users'][1]['username'])
            self.assertIn(
            'fletcher@realpython.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        """Ensure the main route behaves correctly when no users have been added to the database."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>All Users</h1>', response.data)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_users(self):
        """Ensure the main route behaves correctly when users have been added to the database."""
        add_user('peter', 'petertahinduka@gmail.com')
        add_user('paul', 'paulampurire@gmail.com')
        add_user('jean', 'jeantahinduka@gmail.com')
        add_user('moses', 'mosesampurire@gmail.com')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>All Users</h1>', response.data)
        self.assertNotIn(b'<p>No users!</p>', response.data)
        self.assertIn(b'<strong>peter</strong>', response.data)
        self.assertIn(b'<strong>paul</strong>', response.data)

    def test_main_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username='peter', email='petertahinduka@gmai..com'),
                follow_redirects=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>All Users</h1>', response.data)
        self.assertNotIn(b'<p>No users!</p>', response.data)
        self.assertIn(b'<strong>peter</strong>', response.data)



