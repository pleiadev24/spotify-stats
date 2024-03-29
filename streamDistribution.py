plt.figure(figsize=(8, 6))
plt.hist(df['Streams (Billions)'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Streams (Billions)')
plt.ylabel('Frequency')
plt.title('Distribution of Streams')
plt.tight_layout()
plt.show()
