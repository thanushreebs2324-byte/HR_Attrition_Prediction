import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model_hr.pkl', 'rb'))

st.title("HR Attrition Prediction")


Age = st.number_input("Age", 18, 60)

BusinessTravel = st.selectbox("Business Travel", [
    "Travel_Rarely", "Travel_Frequently", "Non-Travel"
])

DailyRate = st.number_input("Daily Rate", 100, 2000)

Department = st.selectbox("Department", [
    "Sales", "Research & Development", "Human Resources"
])

DistanceFromHome = st.number_input("Distance From Home", 1, 50)

Education = st.selectbox("Education", [1, 2, 3, 4, 5])

EducationField = st.selectbox("Education Field", [
    "Life Sciences", "Medical", "Marketing", "Technical Degree",
    "Human Resources", "Other"
])


EmployeeCount = 1
EmployeeNumber = st.number_input("Employee Number", 1, 5000)

EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1,2,3,4])

Gender = st.selectbox("Gender", ["Male", "Female"])

HourlyRate = st.number_input("Hourly Rate", 30, 150)

JobInvolvement = st.selectbox("Job Involvement", [1,2,3,4])

JobLevel = st.selectbox("Job Level", [1,2,3,4,5])

JobRole = st.selectbox("Job Role", [
    "Sales Executive", "Research Scientist", "Laboratory Technician",
    "Manufacturing Director", "Healthcare Representative",
    "Manager", "Sales Representative", "Research Director",
    "Human Resources"
])

JobSatisfaction = st.selectbox("Job Satisfaction", [1,2,3,4])

MaritalStatus = st.selectbox("Marital Status", [
    "Single", "Married", "Divorced"
])

MonthlyIncome = st.number_input("Monthly Income", 1000, 20000)

MonthlyRate = st.number_input("Monthly Rate", 2000, 30000)

NumCompaniesWorked = st.number_input("Num Companies Worked", 0, 10)


Over18 = 1  

OverTime = st.selectbox("Over Time", ["Yes", "No"])

PercentSalaryHike = st.number_input("Percent Salary Hike", 10, 30)

PerformanceRating = st.selectbox("Performance Rating", [1,2,3,4])

RelationshipSatisfaction = st.selectbox("Relationship Satisfaction", [1,2,3,4])


StandardHours = 80

StockOptionLevel = st.selectbox("Stock Option Level", [0,1,2,3])

TotalWorkingYears = st.number_input("Total Working Years", 0, 40)

TrainingTimesLastYear = st.number_input("Training Times Last Year", 0, 10)

WorkLifeBalance = st.selectbox("Work Life Balance", [1,2,3,4])

YearsAtCompany = st.number_input("Years At Company", 0, 40)

YearsInCurrentRole = st.number_input("Years In Current Role", 0, 20)

YearsSinceLastPromotion = st.number_input("Years Since Last Promotion", 0, 15)

YearsWithCurrManager = st.number_input("Years With Current Manager", 0, 20)



def encode():
    return [
        Age,
        ["Travel_Rarely","Travel_Frequently","Non-Travel"].index(BusinessTravel),
        DailyRate,
        ["Sales","Research & Development","Human Resources"].index(Department),
        DistanceFromHome,
        Education,
        ["Life Sciences","Medical","Marketing","Technical Degree","Human Resources","Other"].index(EducationField),
        EmployeeCount,
        EmployeeNumber,
        EnvironmentSatisfaction,
        ["Male","Female"].index(Gender),
        HourlyRate,
        JobInvolvement,
        JobLevel,
        ["Sales Executive","Research Scientist","Laboratory Technician","Manufacturing Director",
         "Healthcare Representative","Manager","Sales Representative","Research Director","Human Resources"].index(JobRole),
        JobSatisfaction,
        ["Single","Married","Divorced"].index(MaritalStatus),
        MonthlyIncome,
        MonthlyRate,
        NumCompaniesWorked,
        Over18,
        ["Yes","No"].index(OverTime),
        PercentSalaryHike,
        PerformanceRating,
        RelationshipSatisfaction,
        StandardHours,
        StockOptionLevel,
        TotalWorkingYears,
        TrainingTimesLastYear,
        WorkLifeBalance,
        YearsAtCompany,
        YearsInCurrentRole,
        YearsSinceLastPromotion,
        YearsWithCurrManager
    ]



if st.button("Predict Attrition"):
    try:
        data = np.array(encode()).reshape(1, -1)
        pred = model.predict(data)[0]

        if pred == 1:
            st.error("Employee likely to leave")
        else:
            st.success("Employee likely to stay")

    except Exception as e:
        st.error(str(e))