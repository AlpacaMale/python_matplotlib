import os

print(os.getcwd())


data = {}
with open("food_shop/region.txt", "r", encoding="utf-8") as file:
    region = ""
    for line in file:
        if "행정동" in line:
            if region:
                data[region] = set(data[region])
            region = line.split()[1].split("(")[0]
            if region == "중":
                region = "중구"
        elif "동" in line:
            districts = [
                string.split("(")[0] for string in line.split()[1:] if "동" in string
            ]
            if not data.get(region):
                data[region] = set()
            for district in districts:
                data[region].add(district)


with open("food_shop/region.csv", "w", encoding="utf-8") as file:
    file.write("region,district\n")
    for region, districts in data.items():
        for district in districts:
            file.write(f"{region},{district}\n")

print("[", end="")
for districts in data.values():
    print(f"\"{'","'.join(districts)}\", ", end="")
print("]")
