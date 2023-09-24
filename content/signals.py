from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .views import UserReaction, AnnounceCreate


@receiver(post_save, sender=UserReaction)
def my_handler(sender, instance, created, **kwargs):
	if instance.status:
		mail = instance.author.email
		send_mail(
			'Subject here',
			'New React',
			'example@yandex.ru',
			[mail],
			fail_silently=False,
		)
	mail = instance.announce.author.email
	send_mail(
		'Subject here',
		'New React',
		'example@yandex.ru',
		[mail],
		fail_silently=False,
	)


