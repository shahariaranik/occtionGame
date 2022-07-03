

travel_log = [
 {
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
 },
 {
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
 },
]


def add_new_country(country, time, place):
  new_dec = {}
  new_dec["country"] = country
  new_dec["visits"] = time
  new_dec["cities"] = place

  travel_log.append(new_dec)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
