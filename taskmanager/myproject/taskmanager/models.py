from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.http import request
from django.urls.base import reverse


# class User(AbstractUser):
#     favourite = models.ManyToManyField('self', blank=True, verbose_name='Избранное')
#     task = models.CharField(max_length=155)
#     is_author = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.username
#

class TaskManager(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория',
                                 blank=True)
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT, null=True, verbose_name='Приоритет',
                                 blank=True)
    completed = models.ForeignKey('Completed', on_delete=models.PROTECT, null=True, verbose_name='Статус задачи',
                                  blank=True)
    favourite = models.ForeignKey('Favourite', on_delete=models.PROTECT, null=True, verbose_name='Избранное',
                                  blank=True)
    completed_at = models.DateField(verbose_name='Дата завершения', auto_now=False, null=True, blank=True)
    # user = models.ManyToManyField(User, verbose_name='Пользователь', related_name='user', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # def save(self, *args, **kwargs):
    #     user = get_current_user()
    #     if user and not user.pk:
    #         user = None
    #     if not self.pk:
    #         self.created_by = user
    #     self.modified_by = user
    #     super(TaskManager, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['completed_at']

    def get_absolute_url(self):
        return reverse('view_task', kwargs={'task_id': self.pk})
        # return reverse('delete', kwargs={'todo_id': self.pk})

    def get_absolute_url_delete(self):
        return reverse('delete', kwargs={'task_id': self.pk})

    def get_absolute_url_finish(self):
        return reverse('finish', kwargs={'task_id': self.pk})

    def get_update_url(self):
        return reverse('update', kwargs={'task_id': self.pk})

    # def get_user(self):
    #     return ",".join([str(p) for p in self.user.all()])

    # def get_absolute_url_favourite(self):
    #     return reverse('favourite', kwargs={'favourite_id': self.pk})

class Favourite(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Избранное')
    mark = models.BooleanField(default=False, verbose_name='Отметить')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_task')
    # favourite_task = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new')

    def get_absolute_url(self):
        return reverse('favourite_task', kwargs={'favourite_id': self.pk})

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        # unique_together = ('user', 'favourite_task')

    def __str__(self):
        return self.mark

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    # slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True, verbose_name='URL')

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Priority(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Приоритет')

    def get_absolute_url(self):
        return reverse('priority', kwargs={'priority_id': self.pk})

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритет'
        ordering = ['title']

    def __str__(self):
        return self.title


class Completed(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Статус задачи')

    def get_absolute_url(self):
        return reverse('completed_task', kwargs={'completed_id': self.pk})



    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'
        ordering = ['title']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('view_news', kwargs={'news_slug': self.slug})
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         # Используем unidecode для преобразования русского текста в ASCII
    #         ascii_title = unidecode(self.title)
    #         self.slug = slugify(ascii_title)
    #     super().save(*args, **kwargs)


# class CompletedAt(models.Model):
#     completed_at = models.DateField(verbose_name='Дата завершения', auto_now=True, blank=True)
#
#     def get_absolute_url(self):
#         return reverse('completed_task', kwargs={'completed_id': self.pk})
#
#     class Meta:
#         verbose_name = 'Дата завершения'
#         verbose_name_plural = 'Даты завершения'
#         ordering = ['completed_at']
#
#     def __str__(self):
#         return self.completed_at
