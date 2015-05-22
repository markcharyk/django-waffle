from __future__ import unicode_literals
from django.core.cache.backends.base import DEFAULT_TIMEOUT


COOKIE = 'dwf_%s'
TEST_COOKIE = 'dwft_%s'
SECURE = True
MAX_AGE = 2592000  # 1 month in seconds

CACHE_PREFIX = 'waffle:'
FLAG_CACHE_KEY = 'flag:%s'
FLAG_USERS_CACHE_KEY = 'flag:%s:users'
FLAG_GROUPS_CACHE_KEY = 'flag:%s:groups'
ALL_FLAGS_CACHE_KEY = 'flags:all'
SAMPLE_CACHE_KEY = 'sample:%s'
ALL_SAMPLES_CACHE_KEY = 'samples:all'
SWITCH_CACHE_KEY = 'switch:%s'
ALL_SWITCHES_CACHE_KEY = 'switches:all'
CACHE_TIMEOUT = DEFAULT_TIMEOUT

FLAG_DEFAULT = False
SAMPLE_DEFAULT = False
SWITCH_DEFAULT = False

OVERRIDE = False
