'''
Google Colab is an online platform:
Write Python code
Run NumPy / Pandas / AI code
Create charts
Save notebooks
Share with students
No need to install Python on computer
It runs in web browser.
https://colab.research.google.com
Login with Google account.
Students do not need installation
Works on low-spec laptops
Good for data science teaching
Supports visualization
Supports file upload
Free GPU (for AI later)
Login with Gmail
Click New Notebook
Each box = code cell
Shift + Enter = run code
e,g.
import pandas as pd
df = pd.DataFrame({
    "Name": ["Aung","Mya","Kyaw","Su","Hla"],
    "Marks": [80, 60, 95, 70, 85]
})
df

import matplotlib.pyplot as plt
df.plot(x="Name", y="Marks", kind="bar")
plt.title("Student Marks Chart")
plt.show()
'''






