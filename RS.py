import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Expanded dataset with Movies, Books, and Products
data = {
    'Category': ['Movie', 'Movie', 'Movie', 'Book', 'Book', 'Book', 'Product', 'Product', 'Product'],
    'Item': [
        'Inception', 'Titanic', 'The Matrix', 
        '1984', 'To Kill a Mockingbird', 'Harry Potter', 
        'iPhone', 'MacBook', 'AirPods'
    ],
    'Description': [
        "A thief who enters dreams to steal secrets.", 
        "A tragic love story aboard the Titanic.", 
        "A hacker discovers a hidden reality.",
        "A dystopian novel about a totalitarian regime.",
        "A classic novel about racial injustice.",
        "A fantasy story about a young wizard.",
        "A smartphone with advanced features.",
        "A high-performance laptop for professionals.",
        "Wireless earbuds with noise cancellation."
    ],
    'User_Rating': [4.8, 4.5, 4.7, 4.9, 4.8, 4.7, 4.6, 4.7, 4.5]
}

df = pd.DataFrame(data)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_items(item_name, category):
    category_df = df[df['Category'] == category]
    if item_name not in category_df['Item'].values:
        return ["Item not found in dataset."]
    
    item_index = category_df.index[category_df['Item'] == item_name][0]
    sim_scores = list(enumerate(cosine_sim[item_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar items

    item_indices = [i[0] for i in sim_scores]
    return category_df.iloc[item_indices][['Item', 'User_Rating']].values.tolist()

# GUI Application
def get_recommendations():
    item_name = entry.get()
    selected_category = category_var.get()

    if not item_name:
        messagebox.showerror("Error", "Please enter an item name.")
        return
    
    category_df = df[df['Category'] == selected_category]
    
    if item_name not in category_df['Item'].values:
        messagebox.showerror("Error", f"{selected_category} not found in dataset.")
        return
    
    item_info = category_df[category_df['Item'] == item_name].iloc[0]
    description = item_info['Description']
    rating = item_info['User_Rating']

    recommendations = recommend_items(item_name, selected_category)
    rec_text = "\n".join([f"{item} (Rating: {rating})" for item, rating in recommendations])

    messagebox.showinfo(
        f"{selected_category} Info & Recommendations",
        f"**{item_name}**\n\nDescription: {description}\nUser Rating: {rating}\n\nRecommended {selected_category}s:\n{rec_text}"
    )

# GUI Design
root = tk.Tk()
root.title("Recommendation System")
root.geometry("500x350")
root.configure(bg="#222831")

tk.Label(root, text="Enter Name:", font=("Arial", 12, "bold"), bg="#222831", fg="#eeeeee").pack(pady=5)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Label(root, text="Select Category:", font=("Arial", 12, "bold"), bg="#222831", fg="#eeeeee").pack(pady=5)
category_var = tk.StringVar(value="Movie")
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Movie", "Book", "Product"], font=("Arial", 12))
category_dropdown.pack(pady=5)

button = tk.Button(root, text="Get Recommendations", command=get_recommendations, font=("Arial", 12, "bold"),
                   bg="#00adb5", fg="white", padx=10, pady=5, relief="raised", bd=3)
button.pack(pady=10)

root.mainloop()
