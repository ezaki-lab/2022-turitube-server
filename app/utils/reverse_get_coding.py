import requests

def reverse_geo_coding(lat, lng):
  url = "https://mreversegeocoder.gsi.go.jp/reverse-geocoder/LonLatToAddress?lat=" + str('{:.6f}'.format(lat)) + "&lon=" + str('{:.6f}'.format(lng))
  resp = requests.get(url,timeout=10)
  data = resp.json()
  return data["results"]["lv01Nm"]