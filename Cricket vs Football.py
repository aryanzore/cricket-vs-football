import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Load data & Basic Inspection 
df = pd.read_csv('C:/Users/pride/Videos/cricket vs football.csv')
print(df.head())

print("/nMissing Values")
print(df.isnull().sum())

#Convert columns to categorical
df['State'] = df['State'].astype('category')
df['Age_Group'] = df['Age_Group'].astype('category')

#Histogram and KDE
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Popularity_Score', hue='Sport', kde=True, bins=20)
plt.title('Distribution of Popularity Scores for Football and Cricket')
plt.xlabel('Popularity Score')
plt.ylabel('Frequency')
plt.show()

#Bar Plot:Average Weekly Viewership Hours 
avg_viewership = df.groupby('Sport')['Weekly_Viewership_Hours'].mean()
plt.figure(figsize=(8, 5))
avg_viewership.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Average Weekly Viewership Hours by Sport')
plt.xlabel('Sport')
plt.ylabel('Average Weekly Viewership (Hours)')
plt.xticks(rotation=0)
plt.show()

#Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Popularity_Score', hue='Sport', data=df)
plt.title('Popularity Score by Age Group for Football and Cricket')
plt.xlabel('Age Group')
plt.ylabel('Popularity Score')
plt.show()

#Grouped Bar Chart:Popularity by States & Sports
state_popularity = df.groupby(['State', 'Sport'], observed=False)['Popularity_Score'].mean().unstack()
state_popularity.plot(kind='bar', stacked=False, figsize=(12, 7), color=['skyblue', 'lightgreen'])
plt.title('Popularity Score by State for Football and Cricket')
plt.xlabel('State')
plt.ylabel('Average Popularity Score')
plt.xticks(rotation=45)
plt.show()

#Scatter plot:Popularity vs Viewership 
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Popularity_Score', y='Weekly_Viewership_Hours', hue='Sport', palette='Set1')
plt.title('Correlation Between Popularity Score and Weekly Viewership Hours')
plt.xlabel('Popularity Score')
plt.ylabel('Weekly Viewership Hours')
plt.show()

from scipy import stats

#T-Test:Compare Mean popularity Between Sports
football_scores = df[df['Sport'] == 'Football']['Popularity_Score']
cricket_scores = df[df['Sport'] == 'Cricket']['Popularity_Score']

t_stat, p_value = stats.ttest_ind(football_scores, cricket_scores)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("There is a statistically significant difference between the popularity scores of football and cricket.")
else:
    print("There is no statistically significant difference between the popularity scores of football and cricket.")

#Anova: Popularity Score by Age Group and Sport
anova_result = stats.f_oneway(
    df[df['Age_Group'] == '10-18']['Popularity_Score'],
    df[df['Age_Group'] == '19-25']['Popularity_Score'],
    df[df['Age_Group'] == '26-35']['Popularity_Score'],
    df[df['Age_Group'] == '36-50']['Popularity_Score'],
    df[df['Age_Group'] == '51+']['Popularity_Score'],
    df[(df['Sport'] == 'Football')]['Popularity_Score'],
    df[(df['Sport'] == 'Cricket')]['Popularity_Score']
)

print("\nANOVA Test Result (Popularity Score by Age Group):")
print(f"F-statistic: {anova_result.statistic}")
print(f"P-value: {anova_result.pvalue}")
if anova_result.pvalue < 0.05:
    print("There is a statistically significant difference in popularity scores based on age group.")
else:
    print("There is no statistically significant difference in popularity scores based on age group.")
