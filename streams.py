
plt.figure(figsize=(12, 8))
plt.barh(top_songs['Song'], top_songs['Streams (Billions)'], color='skyblue')
plt.xlabel('Streams (Billions)')
plt.title('Top 10 Songs by Streams')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest streams at the top
plt.tight_layout()
plt.show()
