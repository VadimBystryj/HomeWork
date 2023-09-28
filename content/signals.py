from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .views import UserReaction, AnnounceCreate


@receiver(post_save, sender=UserReaction)
def my_handler(sender, instance, created, **kwargs):
	if created:
		email = instance.author.email
		send_mail(
			'Subject here',
			'New React',
			'example@yandex.ru',
			[email],
			fail_silently=False,
		)
	email = instance.announce.author.email
	send_mail(
		'Subject here',
		'New React',
		'example@yandex.ru',
		[email],
		fail_silently=False,
	)
