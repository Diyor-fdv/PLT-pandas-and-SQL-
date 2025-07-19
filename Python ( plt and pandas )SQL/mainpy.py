import pandas as pd 
import matplotlib.pyplot as plt
df =  pd.read_csv('ecommerce_sales_sample.csv')
# nan mavjud emas false 
print("NaN mavjudmi:", df.isna().values.any())

# umumiy savdo 
total_revenue = df['Revenue'].sum()
print("Umumiy savdo (Total Revenue):", total_revenue)

#top 5 davlat
top_countries = df['Country'].value_counts().head(5)
print("Eng faol 5 davlat:", top_countries)

#top 5 sotilgan productlar
top_products = df['Product'].value_counts().head(5)
print("Eng ko‘p sotilgan 5 mahsulot:", top_products)

#category boyicha avg narx
avg_price_by_category = df.groupby('Category')['Price'].mean()
print("Kategoriya bo‘yicha o‘rtacha narx:\n", avg_price_by_category)

# oylik daromadlarni yil bilan birga korsatish 
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
monthly_revenue = df.groupby(df['OrderDate'].dt.to_period("M"))['Revenue'].sum()
print("Oyma-oy daromad:\n", monthly_revenue)

# matplotlib graphics
# top_countries = df['Country'].value_counts().head(5)

top_countries.plot(kind='bar', color='orange', figsize=(6, 4))
plt.title("Eng faol 5 davlat")
plt.xlabel("Davlat")
plt.ylabel("Buyurtmalar soni")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# top 5 products
top_products = df['Product'].value_counts().head(5)

top_products.plot(kind='bar', color='green', figsize=(6, 4))
plt.title("Eng ko‘p sotilgan 5 mahsulot")
plt.xlabel("Mahsulot")
plt.ylabel("Soni")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# avg price
avg_price_by_category = df.groupby('Category')['Price'].mean()

avg_price_by_category.plot(kind='bar', color='purple', figsize=(6, 4))
plt.title("Kategoriya bo‘yicha o‘rtacha narx")
plt.xlabel("Kategoriya")
plt.ylabel("O‘rtacha narx")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#oylik daromad

monthly_revenue = df.groupby(df['OrderDate'].dt.to_period("M"))['Revenue'].sum()

monthly_revenue.plot(kind='bar', figsize=(8, 5), color='skyblue')
plt.title("Oyma-oy daromad")
plt.xlabel("Oy")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

# countries income
revenue_by_country = df.groupby('Country')['Revenue'].sum()

revenue_by_country.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), startangle=90)
plt.title("Davlatlar bo‘yicha daromad ulushi")
plt.ylabel("")  # o‘chirib tashlaymiz
plt.tight_layout()

plt.show()

# Diyorbek 