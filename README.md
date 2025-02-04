# RECOMMENDATION_SYSTEM_CODSOFT
Recommendation System built using Python, pandas, and scikit-learn. It allows users to input an item from one of three categories (Movies, Books, Products) and receive recommendations based on item descriptions using TF-IDF Vectorization and Cosine Similarity. The system provides the top 3 most similar items based on a given input and displays the corresponding user ratings along with the item description.


 Features
- Enter an item name from the specified category (Movie, Book, or Product).
- Get the top 3 recommended items based on description similarity.
- Display item descriptions along with user ratings.
- User-friendly GUI built with Tkinter.

Requirements

the following Python packages installed:

- pandas (`pip install pandas`)
- scikit-learn (`pip install scikit-learn`)
- Tkinter (usually comes pre-installed with Python)

Install the necessary dependencies by running:

```bash
pip install pandas scikit-learn
```


 How It Works
- TF-IDF Vectorization: The application converts item descriptions into numeric vectors using TF-IDF, which helps capture the importance of terms in the descriptions.
- Cosine Similarity: It calculates cosine similarity between the input item and all other items in the same category to find similar items.
- GUI: The application uses Tkinter to allow users to input data and view results in an interactive interface.

Example
If you input **"Inception"** (Movie) and select the **"Movie"** category, the system will provide recommendations for similar movies like **"Titanic"** and **"The Matrix"** based on their descriptions.



