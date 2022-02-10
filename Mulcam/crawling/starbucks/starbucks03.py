import folium
import json

# 1. starbucks01.json 파일을 읽어들이자.
with open('starbucks01.json', 'r', encoding='utf-8') as f:
    seoul_gangnam = json.load(f)

print(seoul_gangnam)

# 2. 지도 만들자
gangnamgu_loc = folium.Map(location=[37.51728440687407, 127.04747565811068], zoom_start=18)

# 3. starbucks01.json 파일을 읽어드린 내용(1에서 실행한 결과) 을 가지고
# 반복해서 startbucks 매장의 marker를 만들어 지도에 추가하자
stores = seoul_gangnam['store_list']
for store in stores:
    folium.Marker([store['lat'], store['lot']], popup=folium.Popup(f"스타벅스 {store['s_name']}점", max_width=100)).add_to(
        gangnamgu_loc)



# 4. 지도 저장하자.
gangnamgu_loc.save('starbucks_gangnam.html')