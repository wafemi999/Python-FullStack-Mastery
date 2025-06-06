from rest_framework.throttling import UserRateThrottle

class UserRequestPerMinute(UserRateThrottle):
    scope = 'minute'


class UserRequestPerDay(UserRateThrottle):
    scope = 'day'