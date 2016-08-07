from django.conf import settings  # noqa

from appconf import AppConf
from collections import defaultdict


class PinaxLikesAppConf(AppConf):

    LIKABLE_MODELS = defaultdict(dict)

    def configure_likable_models(self, value):
        DEFAULT_LIKE_CONFIG = {
            "css_class_on": "icon-heart",
            "css_class_off": "icon-heart-empty",
            "like_text_on": "Unlike",
            "like_text_off": "Like",
            "count_text_singular": "like",
            "count_text_plural": "likes",
        }
        for model in value:
            custom_data = value[model].copy()
            default_data = DEFAULT_LIKE_CONFIG.copy()
            value[model] = default_data
            value[model].update(custom_data)
        return value

    class Meta:
        prefix = "pinax_likes"
