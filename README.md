# 🌸 Iris Species Classification Model

This project is a machine learning-based Iris flower species classifier using KMeans clustering. It uses the popular Iris dataset to group data into clusters and then maps those clusters to actual species using label mapping techniques. The project includes a Jupyter Notebook for analysis and a Flask web app with a responsive frontend.

## 📁 Project Structure

```
IRIES_MODEL/
├── app.py                   # Flask backend to serve the model
├── iris_clustering.ipynb    # Jupyter notebook for data exploration and model training
├── model/                   # Saved clustering model (e.g., model.pkl)
├── static/                  # Static files (CSS/images if used)
├── templates/
│   └── index.html           # Web frontend form for prediction
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🧠 Model Details

- **Dataset Used**: Iris dataset from `sklearn.datasets`
- **Algorithm**: KMeans Clustering (Unsupervised Learning)
- **Features**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **Output**: Cluster (0, 1, 2) mapped to species:
  - 0 → Setosa
  - 1 → Versicolor
  - 2 → Virginica
- **Evaluation Techniques**:
  - Confusion Matrix
  - Cluster Visualization using Seaborn/Matplotlib

## 🚀 How to Run the Project

1. **Clone the repository**  
```bash
git clone https://github.com/Adarsh130/IRIES_MODEL.git
cd IRIES_MODEL
```

2. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the Flask App**  
```bash
python app.py
```

4. **Open in Browser**  
Visit: `http://localhost:5000`

## 🖥️ Frontend

- Simple and clean HTML form
- Fully responsive (works on mobile, tablet, and desktop)
- Allows user to enter Iris flower measurements and get predicted species

## 📊 Output and Visualizations

- Confusion matrix to show how clusters align with true labels
- Pair plots and scatter plots to visualize the clusters
- Cluster-to-species mapping logic is shown in the notebook

## 🔧 Technologies Used

- Python
- Scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn
- Flask (for backend)
- HTML & CSS (for frontend)

## 📓 Notebook Details

The file `iris_clustering.ipynb` contains:
- Data preprocessing
- Clustering with KMeans
- Cluster-to-label mapping
- Evaluation
- Visualization

## 🌐 Deployment


## 🧑‍💻 Author

**Adarsh Paswan**  
🔗 [GitHub Profile](https://github.com/Adarsh130)  
📫 Reach out for suggestions or improvements!

## 📝 License

This project is licensed under the [MIT License](LICENSE).
