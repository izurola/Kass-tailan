import pandas as pd

df = pd.read_excel("sales.xlsx")

total_patties = 0
total_buns = 0
total_cheese = 0

for _, row in df.iterrows():
    item = row['Item Name'].lower()
        qty = row['Quantity']
            if "burger" in item:
                total_buns += qty
                if "chicken" not in item:
                    if "(xl)" in item:
                        total_patties += 2 * qty
                    elif "(l)" in item:
                        total_patties += 1 * qty
            if "cheddar" in item or "chedar" in item:
                total_cheese += qty
print("Mah:", total_patties)
print("Talh:", total_buns)
print("Cheese:", total_cheese)
