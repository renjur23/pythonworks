from json import load

f=open("D:\\Pythonworks\\datasets\\countries.json",encoding="utf-8")

data=load(f)

# print number of counrties

# print(f"The number of countries is equal to {len(data)}")

# print name of the country

all_country_name=[country.get("name") for country in data]

# print(all_country_name)

# print all regions

all_regions=[country.get("region") for country in data]

# print(set(all_regions))

# region wise count

region_count={region:all_regions.count(region) for region in all_regions}

# print(region_count)

# most region count

max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count,region_count.get(max_region_count))

# capital of india

Country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

# print(f"capital of India is {Country_capital}")

# countries with most no.of borders

country_border_count={country.get("name"):len(country.get("borders",[])) for country in data}

# print(country_border_count)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

# most populated country

most_populated_country=max(data,key=lambda country:country.get("population",[])).get("name")

# print(most_populated_country)

# names of countries share border with india

alpha_three_code=[country.get("borders")for country in data if country.get("name")=="India"][0]

# print(alpha_three_code)

for code in alpha_three_code:
    
    for country in data:
        
        if country.get("alpha3Code")==code:
            
            print(country.get("name"))





