import re

from accounts.models import BlogUser


def parse_mention(content):
    pattern = re.compile(r'^@(.+?)[:：\s]')
    m = pattern.match(content.strip())

    if m is not None:
        try:
            user = BlogUser.objects.get(username=m.group(1))
            return user
        except BlogUser.DoesNotExist:
            return None
