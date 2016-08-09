# -*- coding:utf-8 -*-

from django.utils.functional import empty, SimpleLazyObject


class LazyList(SimpleLazyObject):
    def __iter__(self):
        if self._wrapped is empty:
            self._setup()

        for i in self._wrapped:
            yield i

    def __len__(self):
        if self._wrapped is empty:
            self._setup()

        return len(self._wrapped)
