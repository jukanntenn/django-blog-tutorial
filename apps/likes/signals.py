from django import dispatch

object_liked = dispatch.Signal(providing_args=['like', 'request'])
