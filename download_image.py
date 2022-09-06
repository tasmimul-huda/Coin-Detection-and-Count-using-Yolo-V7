from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ['bangladeshi coin 1 taka', 'bangladeshi coin 2 taka', 'bangladeshi coin 5 taka', 'bangladeshi all coins']

for kw in keywords:
    response().download(kw, 100)
