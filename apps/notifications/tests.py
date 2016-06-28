from django.test import TestCase
from apps.usera.models import CommunityUser
from apps.community.models import Post
from .models import Notifications


# Create your tests here.

class NotificationsModelTest(TestCase):
    """
    第一个测试，代码模仿自《Python web 开发之测试驱动方法》
    目前只看到前几章的介绍，因此作者也坦言目前测试的代码有点啰嗦，
    当看到后面的章节后会逐步优化测试。
    无论如何，至少有测试了，所以，先这样！
    """

    def test_saving_and_retrieving_notifications(self):
        user1 = CommunityUser.objects.create_user('yangxueguang', 'zmrenwu@163.com', 'yxg19940330')
        user2 = CommunityUser.objects.create_user('xujian', 'xujian@163.com', 'yxg19940330')

        post1 = Post.objects.create(title='test post1', body='test post1', author=user1)
        post2 = Post.objects.create(title='test post2', body='test post2', author=user2)

        create_data1 = {
            'recipient': user1,
            'actor': user2,
            'verb': '回复了',
            'description': '用户 {user} 在你发表的帖子 {post} 中回复了你。'.format(user=user2, post=post1.title),
            'action_object': post1,
        }

        create_data2 = {
            'recipient': user2,
            'actor': user1,
            'verb': '回复了',
            'description': '用户 {user} 在你发表的帖子 {post} 中回复了你。'.format(user=user1, post=post2.title),
            'action_object': post1,
        }
        Notifications.objects.create(**create_data1)
        Notifications.objects.create(**create_data2)

        saved_notifications = Notifications.objects.all()
        self.assertEqual(saved_notifications.count(), 2)

        first_saved_notification = saved_notifications[0]
        second_saved_notification = saved_notifications[1]

        self.assertEqual(first_saved_notification.description, '用户 xujian 在你发表的帖子 test post1 中回复了你。')
        self.assertEqual(second_saved_notification.description, '用户 yangxueguang 在你发表的帖子 test post2 中回复了你。')
