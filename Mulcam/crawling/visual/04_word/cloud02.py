from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json

with open('webtoons.json', encoding='utf-8') as file:
    webtoons = json.load(file)

res = dict()
for webtoon in webtoons['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

masking_img = np.array(Image.open('kakao.png'))
cloud = WordCloud(font_path='Goyang.ttf', max_font_size=40, mask=masking_img, background_color='white').fit_words(res)

cloud.to_file('cloud02.png')

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()