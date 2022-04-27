from django.db import models
from django.db.models import Count

class ThreadManager(models.Manager):
    
    def get_or_create_private_thread(self, user1, user2):
        threads = self.get_queryset().filter(thread_type='private')
        threads = threads.filter(online__in=[user1, user2]).distinct()
        threads = threads.annotate(u_count=Count('online')).filter(u_count=2)
        if threads.exists():
            return threads.first()
        else:
            thread = self.create(thread_type='private')
            thread.online.add(user1)
            thread.online.add(user2)
            return thread

    def by_user(self, user):
        return self.get_queryset().filter(online__in=[user])