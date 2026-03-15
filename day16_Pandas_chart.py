#Pandas supports visualization (charts) by using Matplotlib.
#pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Coffee", "Cake", "Tea"],
    "Sales": [120, 80, 100]
}

df = pd.DataFrame(data)
df.plot(x="Product", y="Sales", kind="bar") #kind="line"
plt.title("Product Sales")
plt.show()
#kind="bar" ဆိုတာ Pandas plot function ထဲမှာ chart အမျိုးအစားကို bar chart
#Categories ကို compare လုပ်ဖို့ သုံး

df.plot(kind="pie", y="Sales", autopct="%1.1f%%")
plt.show()
#autopct- percentage labels on the pie chart.
# % formatting symbol, 1.1- 1 decimal place, f- float number, %% show % sign

df["Sales"].plot(kind="hist")
plt.show()
#Histogram shows how many values fall into ranges.