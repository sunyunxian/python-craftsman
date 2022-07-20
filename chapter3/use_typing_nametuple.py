from typing import NamedTuple


class Address(NamedTuple):
    country: str
    province: str
    city: str


def latlon_to_address(lat, lon):
    country = 'foo'
    province = 'bar'
    city = 'foobar'
    return Address(country=country, province=province, city=city)


if __name__ == '__main__':
    address = latlon_to_address('foo', 'bar')
    country, province, city = address.country, address.province, address.city
    print(country, province, city)
