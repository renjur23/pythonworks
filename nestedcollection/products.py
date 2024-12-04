products=[
    
    {"id":1,"name":"s23ultra","brand":"samsung","price":80000},
    {"id":2,"name":"iPhone16","brand":"apple","price":80000},
    {"id":3,"name":"NordCE2","brand":"OnePlus","price":24000},
    {"id":4,"name":"nothing2","brand":"nothing","price":18000},
    {"id":5,"name":"nothing2","brand":"nothing","price":1000},
    {"id":6,"name":"nothing2","brand":"nothing","price":19000},
    {"id":7,"name":"nothing2","brand":"nothing","price":20000},

   
]

print(len(products))

title=[t.get("name") for t in products]

print(title)

name_sam=[n.get("brand") for n in products if n.get("brand")=="samsung"]

print(name_sam)


print(max(products,key= lambda p:p.get("price")))

print(min(products,key=lambda p:p.get("price")))

costly_mobile=max(products,key=lambda p:p.get("price"))

max_price=costly_mobile.get("price")

costly_mobiles=[p.get("name") for p in products if p.get("price")==max_price]

print(costly_mobiles)

all_brand=[b.get("brand") for b in products]

print(all_brand)

brand_count={b:all_brand.count(b) for b in all_brand}

print(brand_count)


