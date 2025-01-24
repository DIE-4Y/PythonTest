from django.db import models


class poetry(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    dynasty = models.CharField(max_length=255)
    content = models.TextField()


class similar_words(models.Model):
    main_character = models.CharField(max_length=255)
    related_characters = models.TextField()
