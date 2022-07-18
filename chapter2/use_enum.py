from enum import Enum


class User:
    def __init__(self, type=13, points=0) -> None:
        self.type = type
        self.points = points


def add_daily_points(user):
    if user.type == 13:
        return

    if user.type == 3:
        user.points += 120
        return

    user.points += 100
    return


# Use constant
DAILY_POINT_REWARDS = 100
VIP_EXTRA_POINTS = 20
VIP = 3
BANNED = 13


def add_daily_points_v2(user):
    if user.type == BANNED:
        return

    if user.type == VIP:
        user.point = DAILY_POINT_REWARDS + VIP_EXTRA_POINTS
        return

    user.points += 100
    return


# use enum
class UserType(int, Enum):  # E: No base classes are allowed after "enum.Enum"
    # vip 用户
    VIP = 3
    # 黑名单用户
    BANNED = 13


def add_daily_points_v3(user):
    if user.type == UserType.BANNED:
        return

    if user.type == UserType.VIP:
        user.point = DAILY_POINT_REWARDS + VIP_EXTRA_POINTS
        return

    user.points += 100
    return


if __name__ == '__main__':
    foo, bar = User(), User(type=3, points=100)
    add_daily_points(foo)
    add_daily_points(bar)
    print((foo.__dict__), bar.__dict__)
