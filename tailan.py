import pandas as pd

df = pd.read_excel("Бүтээгдэхүүний_тайлан.xlsx")

total_patties = 0
total_buns = 0
total_cheese = 0

for _, row in df.iterrows():
    item = row['Бүтээгдэхүүний нэр'].lower()
    qty = row['Гаралтын тоо']
    if "combo" in item:
        continue
    if "burger" in item:
        total_buns += qty
        if "(xl)" in item:
            total_cheese += 2 * qty
            if "chicken" not in item:
                total_patties += 2 * qty
        elif "(l)" in item:
            total_cheese += 1 * qty
            if "chicken" not in item:
                total_patties += 1 * qty
    if "cheddar cheese" in item:
        total_cheese += qty
print("Mah ", total_patties)
print("Talh ", total_buns)
print("Cheese ", total_cheese)


