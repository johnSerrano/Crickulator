from unit import Unit

"""
Each unit is an instance of the Unit class. See unit.py for details.
For a quick overview, the structure of the entries is:

    "$arg_to_match": Unit(
        "$Name",
        "$category",
        $function_to_convert_to_base_units,
        $function_to_convert_from_base_units,
    ),

$arg_to_match is the name of the unit as it should be referred to in the
arguments. This should never be capitalized, but abbreviations might be
appropriate in some cases.

$Name is the actual name of the unit. This should follow all applicable English
grammar rules for capitalization.

$category is the conversion group of the unit. For example, all units of energy,
like joules or calories, should have the "energy" category. Units can only be
converted to other units of the same category, so spelling and consistent
capitalization are critical. All categories have a "base unit" which they can
be converted to and from. The list of all categories and their base unit can be
found in the table below.

$function_to_convert_to_base_units and $function_to_convert_from_base_units are,
as you might have guessed, function which convert to and from their category's
base unit. For style's sake these should be lambdas, unless there is a real need
for more complicated logic.

Category    | Base unit
------------------------
temperature | fahrenheit
energy      | joule
"""

conversions = {
    "celsius": Unit(
        "Celsius",
        "temperature",
        lambda temp: 1.8*temp + 32,
        lambda temp: (temp - 32) / 1.8,
    ),
    "fahrenheit": Unit(
        "Fahrenheit",
        "temperature",
        lambda temp: temp,
        lambda temp: temp,
    ),
    "kelvin": Unit(
        "Kelvin",
        "temperature",
        lambda temp: 1.8*(temp - 273.15) + 32,
        lambda temp: ((temp - 32) / 1.8) + 273.15,
    ),
    "chirps": Unit(
        "Cricket Chirps",
        "temperature",
        lambda temp: temp/4 + 40,
        lambda temp: (temp - 40) * 4,
    ),
    "joules": Unit(
        "Joules",
        "energy",
        lambda energy: energy,
        lambda energy: energy,
    ),
    "calories": Unit(
        "Calories",
        "energy",
        lambda energy: energy * 4.1868,
        lambda energy: energy / 4.1868,
    ),
    "kilocalories": Unit(
        "Kilocalories",
        "energy",
        lambda energy: energy * 4186.8,
        lambda energy: energy / 4186.8,
    ),
    "watt hours": Unit(
        "Watt hours",
        "energy",
        lambda energy: energy * 3600,
        lambda energy: energy / 3600,
    )
}
