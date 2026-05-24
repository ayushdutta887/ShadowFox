import streamlit as st
import pickle
import numpy as np

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open('loan_model.pkl', 'rb'))

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("💰 Loan Approval Prediction System")

st.write(
    "Fill in the applicant details below to check "
    "whether the loan is likely to be approved."
)

st.divider()

# =========================
# USER INPUTS
# =========================

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Married = st.selectbox(
    "Marital Status",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "Number of Dependents",
    ["0", "1", "2", "3+"]
)

Education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

ApplicantIncome = st.number_input(
    "Applicant Monthly Income",
    min_value=0,
    step=1000
)

CoapplicantIncome = st.number_input(
    "Coapplicant Monthly Income",
    min_value=0,
    step=1000
)

LoanAmount = st.number_input(
    "Loan Amount",
    min_value=0,
    step=10000,
    help="Enter full loan amount (Example: 200000)"
)

loan_term = st.selectbox(
    "Loan Term",
    [
        "5 Years",
        "10 Years",
        "15 Years",
        "20 Years",
        "30 Years"
    ]
)

Credit_History = st.selectbox(
    "Credit History",
    ["Good", "Bad"]
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

st.divider()

# =========================
# ENCODING INPUTS
# =========================

# Gender Encoding
Gender = 1 if Gender == "Male" else 0

# Married Encoding
Married = 1 if Married == "Yes" else 0

# Dependents Encoding
dependents_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}

Dependents = dependents_dict[Dependents]

# Education Encoding
# Graduate = 0
# Not Graduate = 1
Education = 0 if Education == "Graduate" else 1

# Self Employed Encoding
Self_Employed = 1 if Self_Employed == "Yes" else 0

# Convert Loan Amount into thousands
LoanAmount = LoanAmount / 1000

# Loan Term Encoding
loan_term_dict = {
    "5 Years": 60,
    "10 Years": 120,
    "15 Years": 180,
    "20 Years": 240,
    "30 Years": 360
}

Loan_Amount_Term = loan_term_dict[loan_term]

# Credit History Encoding
Credit_History = 1.0 if Credit_History == "Good" else 0.0

# Property Area Encoding
property_area_dict = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}

Property_Area = property_area_dict[Property_Area]

# =========================
# PREDICTION BUTTON
# =========================

if st.button("Predict Loan Status"):

    # Create Input Array
    input_data = np.array([[
        Gender,
        Married,
        Dependents,
        Education,
        Self_Employed,
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        Property_Area
    ]])

    # Make Prediction
    prediction = model.predict(input_data)

    # =========================
    # DISPLAY RESULT
    # =========================

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.success(
            "✅ Congratulations! "
            "The loan is likely to be APPROVED."
        )

    else:

        st.error(
            "❌ Sorry! "
            "The loan is likely to be REJECTED."
        )