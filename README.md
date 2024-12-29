# Multiple Disease Prediction - Machine Learning Project

## Overview
This project aims to build a **Multiple Disease Prediction System** using machine learning models. The system predicts the likelihood of diseases such as **Parkinson's Disease**, **Kidney Disease**, **Liver Disease**, and others based on relevant input parameters. This work integrates data preprocessing, feature engineering, machine learning model building, and deployment to provide accurate and efficient disease predictions.

## Motivation
Health is a critical aspect of human life, and early diagnosis of diseases can save lives and reduce medical expenses. The objective of this project is to utilize machine learning techniques to create a reliable and scalable system for disease prediction, which could assist medical practitioners and individuals in early detection.

## Key Features
- **Disease Prediction Models**:
  - Parkinson's Disease
  - Kidney Disease
  - Liver Disease
- **Input Parameter Validation**: Ensures that all input fields are correctly filled and validated before prediction.
- **User Interface**: Built using **Streamlit** for an interactive and user-friendly dashboard.
- **Data Processing**: Includes handling missing values, data scaling, and feature encoding.

## Workflow
1. **Data Collection**:
   - Datasets for various diseases were sourced from reliable online platforms and repositories (e.g., Kaggle).
2. **Data Preprocessing**:
   - Handled missing values and invalid entries.
   - Applied scaling and normalization to numerical features.
   - Encoded categorical features using mapping techniques.
3. **Model Building**:
   - Selected appropriate machine learning algorithms for each disease prediction task.
   - Trained and validated models using performance metrics like accuracy, precision, and recall.
4. **Deployment**:
   - Created a web interface using **Streamlit** for users to input data and get predictions.
   - Integrated trained models into the application.

## Technologies Used
- **Programming Language**: Python
- **Libraries and Tools**:
  - Machine Learning: Scikit-learn, NumPy, Pandas
  - Data Visualization: Matplotlib, Seaborn
  - Deployment: Streamlit
  - Collaboration: Google Colab for model training
- **Platform**:
  - GitHub: [Project Repository](https://github.com/harivign/Multiple-Disease-Prediction-ml-project-1)
  - Google Colab: [Notebook Link](https://colab.research.google.com/drive/10ii_e21OdUqL-VNOr6Cl6haZlDa-FLSu#scrollTo=hsASkiBLwKhI)

## Highlights of Work Done
1. **Parkinson's Disease Prediction**:
   - Built a model using features like MDVP parameters and vocal measures.
   - Developed a Streamlit-based dashboard for user-friendly prediction.

2. **Kidney Disease Prediction**:
   - Processed categorical and numerical features using mapping and scaling.
   - Ensured input validation to avoid invalid data submissions.

3. **Liver Disease Prediction**:
   - Trained a machine learning model using biochemical parameters.
   - Built an interactive UI for real-time predictions.

4. **Streamlit Deployment**:
   - Integrated multiple disease models into a single dashboard.
   - Ensured smooth user navigation and input validation.

5. **Collaborative Work**:
   - Leveraged Google Colab for efficient model training and testing.
   - Hosted project code and documentation on GitHub for collaboration and version control.

## Project Files
- **Machine Learning Models**: Trained models for each disease.
- **Streamlit App**: Python scripts to build and deploy the user interface.
- **Jupyter Notebooks**: Google Colab notebooks for data exploration, model training, and testing.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/harivign/Multiple-Disease-Prediction-ml-project-1.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Input relevant data in the provided fields to get disease predictions.

## Future Scope
- Extend the system to include more diseases.
- Integrate advanced machine learning models such as ensemble learning and deep learning for improved accuracy.
- Develop a mobile-friendly version of the application.

## Conclusion
This project demonstrates the potential of machine learning in healthcare by providing accurate and early predictions for multiple diseases. By integrating efficient models with an intuitive interface, this system serves as a valuable tool for both medical practitioners and individuals.

---
**Links**:
- [GitHub Repository](https://github.com/harivign/Multiple-Disease-Prediction-ml-project-1)
- [Google Colab Notebook](https://colab.research.google.com/drive/10ii_e21OdUqL-VNOr6Cl6haZlDa-FLSu#scrollTo=hsASkiBLwKhI)

