# -*- coding: utf-8 -*-

from socialoauth.sites.base import OAuth2


class Weibo(OAuth2):
    AUTHORIZE_URL = 'https://api.weibo.com/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://api.weibo.com/oauth2/access_token'

    def build_api_url(self, url):
        return url

    def build_api_data(self, **kwargs):
        data = {
            'access_token': self.access_token
        }
        data.update(kwargs)
        return data

    def parse_token_response(self, res):
        self.uid = res['uid']
        self.access_token = res['access_token']
        self.expires_in = res['expires_in']
        self.refresh_token = None

        res = self.api_call_get(
            'https://api.weibo.com/2/users/show.json',
            uid=self.uid
        )

        self.name = res['name']
        self.avatar = res['profile_image_url']  # 50*50
        self.avatar_large = res['avatar_large']  # 180*180

    def post_status(self, text):
        """
        How to deal this with py3 ?

        if isinstance(text, unicode):
            text = text.encode('utf-8')
        """

        url = 'https://api.weibo.com/2/statuses/update.json'
        res = self.api_call_post(url, status=text)
