import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\91740\\Desktop\\tasks\\RTA Dataset.csv')
     
print("Dataset Columns:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())

plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Road_surface_type', order=df['Road_surface_type'].value_counts().index, palette='viridis')
plt.title('Accidents by Road Surface Type')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Surface Type')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Weather_conditions', order=df['Weather_conditions'].value_counts().index, palette='coolwarm')
plt.title('Accidents by Weather Conditions')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Conditions')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Time', order=df['Time'].value_counts().index[:10], palette='magma')
plt.title('Top 10 Accident Occurrence Times')
plt.xlabel('Number of Accidents')
plt.ylabel('Time of Day')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df, y='Area_accident_occured', order=df['Area_accident_occured'].value_counts().index[:10], palette='cubehelix')
plt.title('Top 10 Accident Hotspots')
plt.xlabel('Number of Accidents')
plt.ylabel('Location')
plt.show()

factors = ['Road_surface_type', 'Weather_conditions', 'Time', 'Area_accident_occured']
for factor in factors:
    print(f"\nTop Categories in {factor}:")
    print(df[factor].value_counts().head())