import urllib.request

image_url = "https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png"
response = urllib.request.urlopen(image_url)
image = response.read()

with open("image.png", "wb") as file:
    file.write(image)