store = {}
store['s_menu'] = []
split_menus = ['수원LA왕갈비 (250g)', '25,000원', '수원양념갈비 (230g)', '21,000원', '생안창살 (150g)', '21,000원', '청기와토장찌개', '6,000원', '냉면 (물/비빔)', '6,000원']
for i in range(0, len(split_menus), 2):
    menu = {}
    print(split_menus[i])
    name = split_menus[i]
    price = split_menus[i+1]
    menu[name] = price
    store['s_menu'].append(menu)
    print(i)


print(store)