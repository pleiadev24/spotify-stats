plt.figure(figsize=(10, 6))
plt.scatter(df['Release Date'], df['Streams (Billions)'], color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Release Date')
plt.ylabel('Streams (Billions)')
plt.title('Streams vs. Release Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()