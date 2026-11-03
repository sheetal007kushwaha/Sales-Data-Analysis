import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
data = pd.read_csv("sales_data.csv")

# Calculate total sales
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Display the sales data
print("Sales Data:")
print(data)

# Calculate total revenue
total_revenue = data["Total_Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# Find product-wise sales
product_sales = data.groupby("Product")["Total_Sales"].sum()

print("\nProduct Wise Sales:")
print(product_sales)

# Find the best-selling product
best_product = product_sales.idxmax()
print("\nBest Selling Product:", best_product)

# Create a bar chart
product_sales.plot(kind="bar", title="Product Wise Sales")

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
