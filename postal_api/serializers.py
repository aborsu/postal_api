from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(required=True, min_length=3)

    def create(self, validated_data):
        raise NotImplementedError("This is never persisted to DB")

    def update(self, instance, validated_data):
        raise NotImplementedError("This is never persisted to DB")


class ParsedAddressSerializer(serializers.Serializer):
    house = serializers.CharField(
        required=False,
        help_text='venue name e.g. "Brooklyn Academy of Music", '
        'and building names e.g. "Empire State Building"',
    )
    category = serializers.CharField(
        required=False, help_text='for category queries like "restaurants", etc.'
    )
    near = serializers.CharField(
        required=False,
        help_text='phrases like "in", "near", etc. used after a category '
        'phrase to help with parsing queries like "restaurants in Brooklyn"',
    )
    house_number = serializers.CharField(
        required=False,
        help_text="usually refers to the external (street-facing) building number. "
        "In some countries this may be a compount, hyphenated number which "
        "also includes an apartment number, or a block number (a la Japan), "
        "but libpostal will just call it the house_number for simplicity.",
    )
    road = serializers.CharField(required=False, help_text="street name(s)")
    unit = serializers.CharField(
        required=False,
        help_text="an apartment, unit, office, lot, or other secondary unit designator",
    )
    level = serializers.CharField(
        required=False,
        help_text="expressions indicating a floor number "
        'e.g. "3rd Floor", "Ground Floor", etc.',
    )
    staircase = serializers.CharField(
        required=False, help_text="numbered/lettered staircase"
    )
    entrance = serializers.CharField(
        required=False, help_text="numbered/lettered entrance"
    )
    po_box = serializers.CharField(
        required=False,
        help_text="post office box: typically found in non-physical (mail-only) "
        "addresses",
    )
    postcode = serializers.CharField(
        required=False, help_text="postal codes used for mail sorting"
    )
    suburb = serializers.CharField(
        required=False,
        help_text='Usually an unofficial neighborhood name like "Harlem", '
        '"South Bronx", or "Crown Heights"',
    )
    city_district = serializers.CharField(
        required=False,
        help_text="these are usually boroughs or districts within a city that serve "
        'some official purpose e.g. "Brooklyn" or "Hackney" or "Bratislava '
        'IV"',
    )
    city = serializers.CharField(
        required=False,
        help_text="any human settlement including cities, towns, villages, hamlets, "
        "localities, etc.",
    )
    island = serializers.CharField(
        required=False, help_text='named islands e.g. "Maui"'
    )
    state_district = serializers.CharField(
        required=False,
        help_text="usually a second-level administrative division or county.",
    )
    state = serializers.CharField(
        required=False,
        help_text="first-level administrative division. Scotland, Northern Ireland, "
        'Wales, and England in the UK are mapped to "state" as well ('
        "convention used in OSM, GeoPlanet, etc.)",
    )
    country_region = serializers.CharField(
        required=False,
        help_text="informal subdivision of a country without any political status",
    )
    country = serializers.CharField(
        required=False,
        help_text="sovereign nations and their dependent territories, anything with "
        "an ISO-3166 code.",
    )
    world_region = serializers.CharField(
        required=False,
        help_text="currently only used for appending “West Indies” after the country "
        "name, a pattern frequently used in the English-speaking Caribbean "
        "e.g. “Jamaica, West Indies”",
    )

    def create(self, validated_data):
        raise NotImplementedError("This is never persisted to DB")

    def update(self, instance, validated_data):
        raise NotImplementedError("This is never persisted to DB")
