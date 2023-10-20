# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from Apps.TutorApp.models import Course, CustomUser, Admin, Tutor, Student, CustomUser

# Test cases for models
class ModelsTestCase(TestCase):
    
    # Create various users with roles for testing
    def setUp(self):
        self.user = CustomUser.objects.create(email="test@example.com")
        self.admin = Admin.objects.create(user=self.user)
        self.tutor = Tutor.objects.create(user=self.user, minutes_tutored=100)
        self.student = Student.objects.create(user=self.user)


    def test_course_model(self):
        # Test Course model by creating a course object and checking its title
        course = Course.objects.create(coursenum="101", title="Intro to Programming", major="Computer Science")
        self.assertEqual(course.title, "Intro to Programming")

    def test_custom_user_model(self):
        # Test CustomUser model by checking if the created user is a student
        user = CustomUser.objects.get(email="test@example.com")
        self.assertTrue(user.is_student)

    def test_admin_model(self):
        # Test Admin model by checking if the associated admin object exists
        admin = Admin.objects.get(user=self.user)
        self.assertIsNotNone(admin)

    def test_tutor_model(self):
        # Test Tutor model by checking the minutes_tutored attribute
        tutor = Tutor.objects.get(user=self.user)
        self.assertEqual(tutor.minutes_tutored, 100)

    def test_student_model(self):
        # Test Student model by checking the associated student object
        student = Student.objects.get(user=self.user)
        self.assertIsNotNone(student)
        
# Test cases for views
class ViewsTestCase(TestCase):
    
    def setUp(self):
        # Create a test user with various roles for testing
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            password="testpassword",
            is_student=True,
        )

    def test_home_view_authenticated_user_redirects(self):
        # Test home view with an authenticated user, expecting a redirect
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('logged in'))

    def test_home_view_unauthenticated_user(self):
        # Test home view with an unauthenticated user, expecting the login page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_student_view(self):
        # Test student view with an authenticated user
        self.client.force_login(self.user)
        response = self.client.get(reverse('student_view_name'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'studentPage.html')

    def test_register_view(self):
        # Test register view, expecting the registration page
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


