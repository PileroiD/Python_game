import random
import urllib.request

res = input('Введите url картинки: ')

try:
	def download_image(url):
		name = random.randrange(100)
		name = str(name) + '.jpg'
		urllib.request.urlretrieve(url, name)

	download_image(res)

except:
	pass