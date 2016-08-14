# -*- coding: utf-8 -*-

from socialoauth.utils import import_oauth_class

from socialoauth.exception import SocialSitesConfigError

version_info = (0, 3, 3)
VERSION = __version__ = '.'.join(map(str, version_info))


def singleton(cls):
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class SocialSites(object):
    """This class holds the sites settings."""

    def __init__(self, settings=None, force_config=False):
        self._configed = False
        if settings:
            if not self._configed or force_config:
                self.config(settings)

    def __getitem__(self, name):
        """Get OAuth2 Class by it's setting name"""
        if not self._configed:
            raise SocialSitesConfigError("No configure")

        try:
            return self._sites_name_class_table[name]
        except KeyError:
            raise SocialSitesConfigError("No settings for site: %s" % name)

    def config(self, settings):
        self._sites_name_class_table = {}
        # {'renren': 'socialoauth.sites.renren.RenRen',...}
        self._sites_class_config_table = {}
        # {'socialoauth.sites.renren.RenRen': {...}, ...}
        self._sites_name_list = []
        self._sites_class_list = []

        for _site_name, _site_class, _site_name_zh, _site_config in settings:
            self._sites_name_class_table[_site_name] = _site_class
            self._sites_class_config_table[_site_class] = {
                'site_name': _site_name,
                'site_name_zh': _site_name_zh,
            }

            # ** iteritems in py3 are deprecated, placed with items **
            # ** We support py3 first and py2 in future **
            try:
                for _k, _v in _site_config.items():
                    self._sites_class_config_table[_site_class][_k.upper()] = _v
            except:
                for _k, _v in _site_config.iteritems():
                    self._sites_class_config_table[_site_class][_k.upper()] = _v

            self._sites_name_list.append(_site_name)
            self._sites_class_list.append(_site_class)

        self._configed = True

    def load_config(self, module_class_name):
        """
        OAuth2 Class get it's settings at here.
        Example:
            from socialoauth import socialsites
            class_key_name = Class.__module__ + Class.__name__
            settings = socialsites.load_config(class_key_name)
        """
        return self._sites_class_config_table[module_class_name]

    def list_sites_class(self):
        return self._sites_class_list

    def list_sites_name(self):
        return self._sites_name_list

    def get_site_object_by_name(self, site_name):
        site_class = self.__getitem__(site_name)
        return import_oauth_class(site_class)()

    def get_site_object_by_class(self, site_class):
        return import_oauth_class(site_class)()
