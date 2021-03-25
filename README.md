# JsontoTsv

pokedex.json contains 801 Pokémons.
The data is in JSON format.
Differnt features:
Pokémon ID, unique string (3 digits).
Pokémon type(s). Order-sensitive.
Pokémon abilities. Order-insensitive.
Pokémon numeric characteristics. Nested.
Pokémon evolution family. Order-sensitive.

The above JSON contains hierarchy (example: stats → hp).
The data concatenating nested field names with a dot (stats.hp).

Fields that contains arrays are flatten in a similar way (using zero-based element index as "field name", i.e. type.0, type.1).
