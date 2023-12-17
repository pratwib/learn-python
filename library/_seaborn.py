import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(tips["total_bill"], kde=True)
plt.title("Histogram Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()
