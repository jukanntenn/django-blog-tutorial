from socialoauth import SocialSites

SOCIALOAUTH_SITES = (
    ('weibo', 'socialoauth.sites.weibo.Weibo', '新浪微博',
     {
         'redirect_uri': 'zmrenwu.pythonanywhere.com',
         'client_id': '3072222160',
         'client_secret': '9b06ed28d7598a91ee72bc38e4f067b2',
     }
     ),
)

socialsites = SocialSites(SOCIALOAUTH_SITES)
for s in socialsites.list_sites_class():
    site = socialsites.get_site_object_by_class(s)
    authorize_url = site.authorize_url
    print(authorize_url)
