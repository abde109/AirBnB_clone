#!/usr/bin/python3

from models.place import Place


place = Place()
original_updated_at = place.updated_at
place.save()
print(place)
