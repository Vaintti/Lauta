from django.shortcuts import render, get_object_or_404

from .models import Thread


def thread(request, url, uuid):
    item = get_object_or_404(Thread, uuid=uuid)
    messages = item.message_set.order_by('created_at')
    return render(request, 'threads/thread.html', {'messages': messages})
