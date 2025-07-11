🏡 House Price Prediction Web Application

This project is a machine learning-powered web application that predicts house prices based on user input features like area, number of bedrooms, bathrooms, etc. It uses a trained ML model integrated with a Flask backend and a simple, interactive frontend.

## 📌 Features

- ✅ Predict house prices using a trained ML model
- 🌐 Frontend created with HTML, CSS, and JavaScript
- ⚙ Backend built using Python Flask
- 📈 Machine learning model trained on Google Colab
- 🧠 Model saved as model.pkl and used in real-time for predictions
- 💡 Clean and user-friendly interface

---

## 🛠 Tech Stack Used

| Component        | Technology                                             |
|------------------|--------------------------------------------------------|
| Machine Learning | Python, scikit-learn, pandas (Google Colab)            |
| Backend          | Flask (Python)                                         |
| Frontend         | HTML, CSS, JavaScript                                  |
| IDEs Used        | Google Colab (ML), Visual Studio Code (App UI & Flask) |

## 🚀 How to Run the Project Locally

Follow these steps to run the project on your local machine:

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

🧪 Step 2: Create Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

📦 Step 3: Install Required Libraries

Make sure the following libraries are installed:

pip install flask pandas scikit-learn joblib

> You can also create a requirements.txt using:

pip freeze > requirements.txt

▶ Step 4: Run the Flask App

python app.py

🌐 Step 5: Open in Browser

Open your browser and go to:

http://127.0.0.1:5000/

You should see your house price prediction web interface!


💡 How It Works

1. You trained a regression model in Google Colab using historical house data.

2. The trained model is saved as model.pkl using joblib.

3. In app.py, the model is loaded and a Flask route (/predict) is defined to take user input from the HTML form and return the predicted price.

4. HTML form sends data to Flask via POST request.

5. Flask backend processes the input and returns the prediction to the frontend to be displayed.

📸 Screenshots of output
(https://github.com/user-attachments/assets/01349f78-e39b-490e-99e7-484f989be310)


📈 Model Training Summary

Platform: Google Colab

Libraries Used: pandas, numpy, scikit-learn

Model Type: Linear Regression / Decision Tree / Random Forest (mention your model)

Export Method: joblib.dump(model, 'model.pkl')

🔮 Future Scope

Deploy on cloud platforms like Render, Heroku, or AWS

Add more features to improve model accuracy

Improve UI with Bootstrap or Tailwind CSS

Add a database for storing prediction history


🤝 Contributions

Feel free to contribute by:

Opening issues

Forking the repo and submitting pull requests

Suggesting UI or model improvements
