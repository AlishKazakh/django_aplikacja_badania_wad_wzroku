from django.db import models


class TestResults(models.Model):
    astigmatism_test_result = models.CharField(max_length=100, default='')
    color_blindness_test_result = models.IntegerField(default=0)
    visual_acuity_test_result = models.IntegerField(default=0)
    macular_degeneration_test_result = models.CharField(max_length=100, default='')
    dry_eye_test_result = models.IntegerField(default=0)
    accommodation_test_result = models.IntegerField(default=0)


class Exercises(models.Model):
    text_exercise = models.TextField(default='', blank=True)
    image_exercise = models.ImageField(upload_to='test_image', default='', blank=True)
    exercise_number = models.IntegerField(default=0)




class Test(models.Model):
    question = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='test_image', default='', blank=True)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True, default='')
    option_four = models.CharField(max_length=100, blank=True, default='')
    answer = models.CharField(max_length=100, default='', blank=True)
    size = models.FloatField(default=0, blank=True)
    test = models.CharField(max_length=50)
    question_number = models.IntegerField(default=0)

    def __str__(self):
        return self.test


class Information(models.Model):
    astigmatism_information = models.TextField()
    astigmatism_symptoms = models.TextField(default='')
    astigmatism_treatment = models.TextField(default='')
    color_blindness_information = models.TextField()
    color_blindness_symptoms = models.TextField(default='')
    color_blindness_treatment = models.TextField(default='')
    macular_degeneration_information = models.TextField()
    macular_degeneration_symptoms = models.TextField(default='')
    macular_degeneration_treatment = models.TextField(default='')
    dry_eye_information = models.TextField()
    dry_eye_symptoms = models.TextField(default='')
    dry_eye_treatment = models.TextField(default='')
    language = models.CharField(max_length=50, default='', blank=True)

class Information1(models.Model):
    disease_information = models.TextField(default='')
    disease_symptoms = models.TextField(default='')
    disease_treatment = models.TextField(default='')
    disease_name = models.CharField(max_length=50, default='')
    disease = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.disease
