
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

Breast_Cancer_model = pickle.load(open(f'{working_dir}/saved_models/Breast_Cancer.sav', 'rb'))

Kidney_disease_model = pickle.load(open(f'{working_dir}/saved_models/Chronic Kdney Disease.sav', 'rb'))

Covid_19_disease_model = pickle.load(open(f'{working_dir}/saved_models/Covid_19 prediction.sav', 'rb'))

Liver_disease_model = pickle.load(open(f'{working_dir}/saved_models/Liver Disease.sav', 'rb'))

Strok_disease_model = pickle.load(open(f'{working_dir}/saved_models/Stroke prediction.sav', 'rb'))

Mental_health_disease_model = pickle.load(open(f'{working_dir}/saved_models/Mental health prediction.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction',
                            'Kidney Diseases Prediction',
                            'Covid_19 Prediction',
                            'Liver Diseases Prediction',
                            'Stroke Prediction',
                            'Mental Health Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)




# Breast Cancer Prediction page

if selected == "Breast Cancer Prediction":

    # page title
    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        radius = st.text_input('mean radius')

    with col2:
        texture = st.text_input('mean texture')

    with col3:
        perimeter = st.text_input('mean perimeter)')

    with col4:
        area = st.text_input('mean area')

    with col5:
        mean_smoothness = st.text_input('mean smoothness')

    with col1:
        RAP = st.text_input('mean compactness')

    with col2:
        mean_concavity = st.text_input('mean concavity')

    with col3:
        concave_points = st.text_input('mean concave points')

    with col4:
        symmetry = st.text_input('mean symmetry')

    with col5:
        fractal_dimension = st.text_input('mean fractal dimension')

    with col1:
        radius_error = st.text_input('radius error')

    with col2:
        texture_error = st.text_input('texture error')

    with col3:
        perimeter_error = st.text_input('perimeter error')

    with col4:
        area_error = st.text_input('area error')

    with col5:
        smoothness_error = st.text_input('smoothness error')

    with col1:
        compactness = st.text_input('compactness error')

    with col2:
        RPDE = st.text_input('concavity error')

    with col3:
        concave_points_error = st.text_input('concave points error')

    with col4:
        symmetry_error = st.text_input('symmetry error')

    with col5:
        dimension_error = st.text_input('fractal dimension error')

    with col1:
        D2 = st.text_input('worst radius')

    with col2:
        worst_radius = st.text_input('worst texture')
        
    with col3:
        perimeter = st.text_input('worst perimeter')
        
    with col4:
        area = st.text_input('worst area')
        
    with col5:
        smoothness = st.text_input('worst smoothness')
        
        
    with col1:
        concavity = st.text_input('worst concavity')
    with col2:
        points = st.text_input('worst concave points')
    with col3:
        worst_symmetry = st.text_input('worst symmetry')
    with col4:
        dimension = st.text_input('worst fractal dimension')
    with col5:
        worst_compactness = st.text_input('worst compactness')
    

    # code for Prediction
    Breast_cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):

        user_input = [ radius,texture,perimeter,area,mean_smoothness, RAP,mean_concavity, concave_points ,
                         symmetry, fractal_dimension, radius_error,texture_error, perimeter_error,area_error, smoothness_error,compactness,RPDE, concave_points_error, symmetry_error,dimension_error,  D2, worst_radius, perimeter, area, smoothness,concavity, points,worst_symmetry,dimension,worst_compactness]

        user_input = [float(x) for x in user_input]
        # user_input = [x for x in user_input if x.strip().replace('.', '', 1).isdigit()]
        # user_input = [float(x) for x in user_input]


        Breast_cancer_prediction = Breast_Cancer_model.predict([user_input])

        if Breast_cancer_prediction[0] == 0:
            Breast_cancer_diagnosis = "The Breast cancer is Malignant"
        else:
            Breast_cancer_diagnosis = "The Breast Cancer is Benign"

    st.success(Breast_cancer_diagnosis)
    

# Kidney disease Page

if selected == "Kidney Diseases Prediction":

    # page title
    st.title("Kidney Diseases Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        a1 = st.text_input('age')

    with col2:
        a2 = st.text_input('bp')

    with col3:
        a3 = st.text_input('sg)')

    with col4:
        a4 = st.text_input('al')

    with col5:
        a5 = st.text_input('su')

    with col1:
        a6 = st.text_input('rbc')

    with col2:
        a7 = st.text_input('pc')

    with col3:
        a8 = st.text_input('pcc')

    with col4:
        a9 = st.text_input('ba')

    with col5:
        a10 = st.text_input('bgr')

    with col1:
        a11 = st.text_input('bu')

    with col2:
        a12 = st.text_input('sc')

    with col3:
        a13 = st.text_input('sod')

    with col4:
        a14 = st.text_input('pot')

    with col5:
        a15 = st.text_input('hemo')

    with col1:
        a16 = st.text_input('pcv')

    with col2:
        a17 = st.text_input('wc')

    with col3:
        a18 = st.text_input('rc')

    with col4:
        a19 = st.text_input('htn')

    with col5:
        a20 = st.text_input('dm')

    with col1:
        a21 = st.text_input('cad')

    with col2:
        a22 = st.text_input('appet')
        
    with col3:
        a23 = st.text_input('pe')
        
    with col4:
        a24 = st.text_input('ane')
        
   
    

    # code for Prediction
    Kidney_diseases_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Chronic Kidney Diseases Test Result"):

        user_input = [ a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24]

        user_input = [float(x) for x in user_input]

        Kidney_diseases_prediction = Kidney_disease_model.predict([user_input])

        if Kidney_diseases_prediction[0] == 'ckd':
            Kidney_diseases_diagnosis = "The person is chronic kidney disease"
        else:
            Kidney_diseases_diagnosis = "The person is not chronic kidney disease"

    st.success(Kidney_diseases_diagnosis)


# Covid_19 Prediction Page
if selected == "Covid_19 Prediction":

    # page title
    st.title("Covid_19 Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        b1 = st.text_input('Fever')

    with col2:
        b2 = st.text_input('Tiredness')

    with col3:
        b3 = st.text_input('Dry-Cough')

    with col4:
        b4 = st.text_input('Difficulty-in-Breathing')

    with col5:
        b5 = st.text_input('Sore-Throat')

    with col1:
        b6 = st.text_input('None_Sympton')

    with col2:
        b7 = st.text_input('Pains')

    with col3:
        b8 = st.text_input('Nasal-Congestion')

    with col4:
        b9 = st.text_input('Runny-Nose')

    with col5:
        b10 = st.text_input('Diarrhea')

    with col1:
        b11 = st.text_input('None_Experiencing')

    with col2:
        b12 = st.text_input('Age_0-9')

    with col3:
        b13 = st.text_input('Age_10-19')

    with col4:
        b14 = st.text_input('Age_20-24')

    with col5:
        b15 = st.text_input('Age_25-59')

    with col1:
        b16 = st.text_input('Age_60+')

    with col2:
        b17 = st.text_input('Gender_Female')

    with col3:
        b18 = st.text_input('Gender_Male')

    with col4:
        b19 = st.text_input('Gender_Transgender')

    with col5:
        b20 = st.text_input('Severity_Mild')

    with col1:
        b21 = st.text_input('Severity_Moderate')

    with col2:
        b22 = st.text_input('Severity_None')
        
    with col3:
        b23 = st.text_input('Contact_Dont-Know')
        
    with col4:
        b24 = st.text_input('Contact_No')
        
    with col5:
        b25 = st.text_input('Contact_Yes')

    # code for Prediction
    Covid_19_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Cocid_19 Test Result"):

        user_input = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]

        user_input = [float(x) for x in user_input]

        Covid_19_prediction = Covid_19_disease_model.predict([user_input])

        if Covid_19_prediction[0] == 1:
            Covid_19_diagnosis = "The person is affected by Covid_19"
        else:
            Covid_19_diagnosis = "The person is not affected by Covid_19"

    st.success(Covid_19_diagnosis)



# Liver diseases Prediction Page
if selected == 'Liver Diseases Prediction':

    # page title
    st.title('Liver Diseases Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        c1 = st.text_input('age')

    with col2:
        c2 = st.text_input('gender')

    with col3:
        c3 = st.text_input('tot_bilirubin')

    with col1:
        c4 = st.text_input('direct_bilirubin')

    with col2:
        c5 = st.text_input('tot_proteins')

    with col3:
        c6 = st.text_input('albumin')

    with col1:
        c7 = st.text_input('ag_ratio')

    with col2:
        c8 = st.text_input('sgpt')
    with col3:
        c9 = st.text_input('sgot')
    with col1:
        c10 = st.text_input('alkphos')


    # code for Prediction
    Liver_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [c1,c2,c3.c4,c5,c6,c7,c8,c9,c10]

        user_input = [float(x) for x in user_input]

        Liver_prediction = Liver_disease_model.predict([user_input])

        if Liver_prediction[0] == 1:
            Liver_diagnosis = 'The person Liver Diseases'
        else:
            Liver_diagnosis = 'The person is not Liver Diseases'

    st.success(Liver_diagnosis)




# Mental Health Prediction Page
if selected == 'Mental Health Prediction':

    # page title
    st.title('Mental Health Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        d1 = st.text_input('Gender')

    with col2:
        d2 = st.text_input('Occupation')

    with col3:
        d3 = st.text_input('self_employed')

    with col1:
        d4 = st.text_input('family_history')

    with col2:
        d5 = st.text_input('Days_Indoors')

    with col3:
        d6 = st.text_input('Growing_Stress')

    with col1:
        d7 = st.text_input('Changes_Habits')

    with col2:
        d8 = st.text_input('Mental_Health_History')

    with col3:
        d9 = st.text_input('Mood_Swings')

    with col1:
        d10 = st.text_input('Coping_Struggles')

    with col2:
        d11 = st.text_input('Work_Interest')

    with col3:
        d12 = st.text_input('Social_Weakness')

    with col1:
        d13 = st.text_input('mental_health_interview')
        
    with col2:
        d14 = st.text_input('care_options')

    # code for Prediction
    mental_health_diagnosis = ''

    # creating a button for Prediction

    if st.button('Mental Health Diseases Test Result'):

        user_input = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]

        user_input = [float(x) for x in user_input]

        mental_health_prediction = Mental_health_disease_model.predict([user_input])

        if mental_health_prediction[0] == 1:
            mental_health_diagnosis = 'The person is Mental Health'
        else:
            mental_health_diagnosis = 'The person is Mental Health'

    st.success(mental_health_diagnosis)
    
    
    
    
# Stroke Prediction Page
if selected == 'Stroke Prediction':

    # page title
    st.title('Stroke Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        e1 = st.text_input('gender')

    with col2:
        e2 = st.text_input('age')

    with col3:
        e3 = st.text_input('hypertension')

    with col1:
        e4 = st.text_input('heart_disease')

    with col2:
        e5 = st.text_input('ever_married')

    with col3:
        e6 = st.text_input('work_type')

    with col1:
        e7 = st.text_input('Residence_type')

    with col2:
        e8 = st.text_input('avg_glucose_level')

    with col3:
        e9 = st.text_input('bmi')

    with col1:
        e10 = st.text_input('smoking_status')

    

    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Stroke Diseases Test Result'):

        user_input = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]

        user_input = [float(x) for x in user_input]

        stroke_prediction = Strok_disease_model.predict([user_input])

        if stroke_prediction[0] == 1:
            stroke_diagnosis = 'The person stroked'
        else:
            stroke_diagnosis = 'The person not stroked'

    st.success(stroke_diagnosis)
    
    
    
# streamlit run app.py 

