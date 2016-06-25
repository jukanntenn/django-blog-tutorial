from django.dispatch import Signal

notify = Signal(providing_args=['recipient', 'actor', 'verb', 'description', 'action_object', 'created_time'])
