<h2>Laptop Price Prediction </h2>
<h2>Problem Statement</h2>
The aim of this project is to predict the price of a laptop based on various features such as RAM Size, RAM Type, Storage, OS, etc. The problem statement is to build an interface (using streamlit) where users can input the laptop features and get the price prediction.

<h2>Data Preprocessing</h2>
The dataset used for this project is obtained by scraping laptop listings from Flipkart. It is real world data.Initially,The data contains Product,feature, MRP, Rating with 720 rows and 4 columns. By using regular expressions i have extracted features such as OS, storage, RAM size, RAM type, brand, processor, display size.And data is cleaned by removing nullvalues and dropping duplicates or irrelevant featues.

<h2>Feature Engineering</h2>
Before training the model, the data was preprocessed to prepare it for model training.

Categorical features were encoded using one-hot encoding, which converts categorical features into numerical features so that the model can better understand the data. One-hot encoding creates new columns for each category and assigns a value of 0 or 1 to these columns, depending on whether the category is present in the data or not.

Numerical columns were standardized using StandardScaler, which scales the numerical features so that they have a mean of 0 and standard deviation of 1. This helps in making the data less sensitive to the scale of the features, thus improving the performance of the model.

<h2>Exploratory Data Analysis</h2>
In this step,I have visualized the data using various plots to analyze the data and to understand the relationships between different features and the targetnvariable. I have used the Seaborn library to visualize the relationship between MRP (target variable) and different features. 

<h2>Model Training</h2>
In this step, split the preprocessed data into train and test sets with a 80-20 split ratio. Then, I trained a Random Forest Regressor model on the training set using the scikit-learn library. Random Forest Regressor is an ensemble machine learning algorithm that combines multiple decision trees to make predictions. It is a popular choice for regression tasks because it can handle non-linear relationships and does not require much tuning.

<h2>Deployment</h2>
In this step, I deployed the trained model using Streamlit .I have created a web interface where users can input the laptop features and get the price prediction. The interface is user-friendly and easy to use. The application takes input features from the user such as OS, storage, RAM size and type, brand, processor, display size, and predicts the MRP of the laptop.

You can acess the app using this link: 👉: https://b-v-krishna-innomat-flipkart-laptop-price-predictionhome-96rzh0.streamlit.app/price


<h2>How to use this project</h2>
-> Clone the repository<br>
-> Install the required libraries using pip install -r requirements.txt<br>
-> Run the app using streamlit run app.py<br>

<h2>Output screen Images</h2>

<img src='https://github.com/b-v-krishna/INNOMATICS-INTERN-TASKS/blob/master/FLIPKART_LAPTOP_PRICE_PREDICTION/resources/images/Screenshot%202023-04-18%20223523.png'  style="display: block; margin: auto;">
<br>
<img src='https://github.com/b-v-krishna/INNOMATICS-INTERN-TASKS/blob/master/FLIPKART_LAPTOP_PRICE_PREDICTION/resources/images/Screenshot%202023-04-18%20223539.png'  style="display: block; margin: auto;">

