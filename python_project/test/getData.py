import requests

source = requests.get("https://datachart.500.com/ssq/").content.decode('GBK')
print(source)