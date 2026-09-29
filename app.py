import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD MODEL AND FEATURE NAMES
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("random_forest_model.pkl")


@st.cache_data
def load_feature_names():
    return joblib.load("feature_names.pkl")


model = load_model()
feature_names = load_feature_names()


# ============================================================
# HEADER
# ============================================================

st.title("👨‍💼 Employee Attrition Prediction")

st.markdown(
    """
    ### Predict whether an employee is likely to leave the organization

    Enter the employee's information below and the trained machine
    learning model will predict the likelihood of employee attrition.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📊 About the Project")

    st.write(
        """
        This application uses a **Random Forest Classifier** trained
        on an HR Employee Attrition dataset.

        The model predicts:

        - **0 → No Attrition**
        - **1 → Attrition**
        """
    )

    st.divider()

    st.subheader("Model Information")

    st.write(
        f"Number of model features: **{len(feature_names)}**"
    )

    st.write(
        "Algorithm: **Random Forest Classifier**"
    )

    st.divider()

    st.info(
        "Enter the employee information and click "
        "**Predict Attrition** to generate a prediction."
    )


# ============================================================
# EMPLOYEE INFORMATION FORM
# ============================================================

with st.form("employee_form"):

    # --------------------------------------------------------
    # DEMOGRAPHICS
    # --------------------------------------------------------

    st.subheader("👤 Employee Demographics")

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.slider(
            "Age",
            min_value=18,
            max_value=60,
            value=36,
            step=1
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

    with col3:

        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Divorced"]
        )


    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    st.subheader("🎓 Education")

    col1, col2 = st.columns(2)

    with col1:

        education = st.selectbox(
            "Education Level",
            [1, 2, 3, 4, 5],
            index=2,
            help=(
                "1 = Below College | "
                "2 = College | "
                "3 = Bachelor | "
                "4 = Master | "
                "5 = Doctor"
            )
        )

    with col2:

        education_field = st.selectbox(
            "Education Field",
            [
                "Human Resources",
                "Life Sciences",
                "Marketing",
                "Medical",
                "Other",
                "Technical Degree"
            ]
        )


    # --------------------------------------------------------
    # JOB INFORMATION
    # --------------------------------------------------------

    st.subheader("💼 Job Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        department = st.selectbox(
            "Department",
            [
                "Human Resources",
                "Research & Development",
                "Sales"
            ]
        )

    with col2:

        job_role = st.selectbox(
            "Job Role",
            [
                "Healthcare Representative",
                "Human Resources",
                "Laboratory Technician",
                "Manager",
                "Manufacturing Director",
                "Research Director",
                "Research Scientist",
                "Sales Executive",
                "Sales Representative"
            ]
        )

    with col3:

        job_level = st.selectbox(
            "Job Level",
            [1, 2, 3, 4, 5],
            index=1
        )


    # --------------------------------------------------------
    # JOB AND ENVIRONMENT SATISFACTION
    # --------------------------------------------------------

    st.subheader("😊 Job & Environment Satisfaction")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        job_involvement = st.selectbox(
            "Job Involvement",
            [1, 2, 3, 4],
            index=2
        )

    with col2:

        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col3:

        environment_satisfaction = st.selectbox(
            "Environment Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col4:

        work_life_balance = st.selectbox(
            "Work-Life Balance",
            [1, 2, 3, 4],
            index=2
        )


    # --------------------------------------------------------
    # SALARY INFORMATION
    # --------------------------------------------------------

    st.subheader("💰 Salary Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        monthly_income = st.slider(
            "Monthly Income",
            min_value=1009,
            max_value=19999,
            value=5000,
            step=10
        )

    with col2:

        monthly_rate = st.slider(
            "Monthly Rate",
            min_value=2094,
            max_value=26999,
            value=14000,
            step=10
        )

    with col3:

        hourly_rate = st.slider(
            "Hourly Rate",
            min_value=30,
            max_value=100,
            value=66,
            step=1
        )

    col1, col2 = st.columns(2)

    with col1:

        daily_rate = st.slider(
            "Daily Rate",
            min_value=102,
            max_value=1499,
            value=802,
            step=1
        )

    with col2:

        percent_salary_hike = st.slider(
            "Percent Salary Hike",
            min_value=11,
            max_value=25,
            value=15,
            step=1
        )


    # --------------------------------------------------------
    # WORK ENVIRONMENT
    # --------------------------------------------------------

    st.subheader("🏢 Work Environment")

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )


    # --------------------------------------------------------
    # CAREER EXPERIENCE
    # --------------------------------------------------------

    st.subheader("📈 Career Experience")

    col1, col2, col3 = st.columns(3)

    with col1:

        total_working_years = st.slider(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=10,
            step=1
        )

    with col2:

        years_at_company = st.slider(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=7,
            step=1
        )

    with col3:

        years_current_role = st.slider(
            "Years in Current Role",
            min_value=0,
            max_value=18,
            value=4,
            step=1
        )

    col1, col2 = st.columns(2)

    with col1:

        years_since_promotion = st.slider(
            "Years Since Last Promotion",
            min_value=0,
            max_value=15,
            value=2,
            step=1
        )

    with col2:

        years_with_manager = st.slider(
            "Years With Current Manager",
            min_value=0,
            max_value=17,
            value=4,
            step=1
        )


    # --------------------------------------------------------
    # TRAVEL AND DISTANCE
    # --------------------------------------------------------

    st.subheader("✈️ Travel & Distance")

    col1, col2 = st.columns(2)

    with col1:

        business_travel = st.selectbox(
            "Business Travel",
            [
                "Non-Travel",
                "Travel-Frequently",
                "Travel-Rarely"
            ]
        )

    with col2:

        distance_from_home = st.slider(
            "Distance From Home",
            min_value=1,
            max_value=29,
            value=7,
            step=1
        )


    # --------------------------------------------------------
    # OTHER WORKPLACE FACTORS
    # --------------------------------------------------------

    st.subheader("⚙️ Other Workplace Factors")

    col1, col2, col3 = st.columns(3)

    with col1:

        num_companies = st.slider(
            "Number of Companies Worked",
            min_value=0,
            max_value=9,
            value=2,
            step=1
        )

    with col2:

        training_times = st.slider(
            "Training Times Last Year",
            min_value=0,
            max_value=6,
            value=3,
            step=1
        )

    with col3:

        stock_option = st.selectbox(
            "Stock Option Level",
            [0, 1, 2, 3],
            index=1
        )

    col1, col2 = st.columns(2)

    with col1:

        relationship_satisfaction = st.selectbox(
            "Relationship Satisfaction",
            [1, 2, 3, 4],
            index=2
        )

    with col2:

        performance_rating = st.selectbox(
            "Performance Rating",
            [1, 2, 3, 4],
            index=0
        )


    # --------------------------------------------------------
    # SUBMIT BUTTON
    # --------------------------------------------------------

    st.divider()

    submitted = st.form_submit_button(
        "🔮 Predict Attrition",
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

if submitted:

    # --------------------------------------------------------
    # CREATE NUMERICAL INPUT DATA
    # --------------------------------------------------------

    input_data = pd.DataFrame({

        "Age": [age],

        "DailyRate": [daily_rate],

        "DistanceFromHome": [
            distance_from_home
        ],

        "Education": [education],

        "EnvironmentSatisfaction": [
            environment_satisfaction
        ],

        "Gender": [
            1 if gender == "Male" else 0
        ],

        "HourlyRate": [hourly_rate],

        "JobInvolvement": [
            job_involvement
        ],

        "JobLevel": [job_level],

        "JobSatisfaction": [
            job_satisfaction
        ],

        "MonthlyIncome": [
            monthly_income
        ],

        "MonthlyRate": [
            monthly_rate
        ],

        "NumCompaniesWorked": [
            num_companies
        ],

        "OverTime": [
            1 if overtime == "Yes" else 0
        ],

        "PercentSalaryHike": [
            percent_salary_hike
        ],

        "PerformanceRating": [
            performance_rating
        ],

        "RelationshipSatisfaction": [
            relationship_satisfaction
        ],

        "StockOptionLevel": [
            stock_option
        ],

        "TotalWorkingYears": [
            total_working_years
        ],

        "TrainingTimesLastYear": [
            training_times
        ],

        "WorkLifeBalance": [
            work_life_balance
        ],

        "YearsAtCompany": [
            years_at_company
        ],

        "YearsInCurrentRole": [
            years_current_role
        ],

        "YearsSinceLastPromotion": [
            years_since_promotion
        ],

        "YearsWithCurrManager": [
            years_with_manager
        ]
    })


    # --------------------------------------------------------
    # BUSINESS TRAVEL ONE-HOT ENCODING
    # --------------------------------------------------------

    input_data["BusinessTravel_Non-Travel"] = (
        1 if business_travel == "Non-Travel" else 0
    )

    input_data["BusinessTravel_Travel-Frequently"] = (
        1 if business_travel == "Travel-Frequently" else 0
    )

    input_data["BusinessTravel_Travel-Rarely"] = (
        1 if business_travel == "Travel-Rarely" else 0
    )


    # --------------------------------------------------------
    # DEPARTMENT ONE-HOT ENCODING
    # --------------------------------------------------------

    input_data["Department_Human Resources"] = (
        1 if department == "Human Resources" else 0
    )

    input_data["Department_Research & Development"] = (
        1 if department == "Research & Development"
        else 0
    )

    input_data["Department_Sales"] = (
        1 if department == "Sales" else 0
    )


    # --------------------------------------------------------
    # EDUCATION FIELD ONE-HOT ENCODING
    # --------------------------------------------------------

    input_data["EducationField_Human Resources"] = (
        1 if education_field == "Human Resources"
        else 0
    )

    input_data["EducationField_Life Sciences"] = (
        1 if education_field == "Life Sciences"
        else 0
    )

    input_data["EducationField_Marketing"] = (
        1 if education_field == "Marketing"
        else 0
    )

    input_data["EducationField_Medical"] = (
        1 if education_field == "Medical"
        else 0
    )

    input_data["EducationField_Other"] = (
        1 if education_field == "Other"
        else 0
    )

    input_data["EducationField_Technical Degree"] = (
        1 if education_field == "Technical Degree"
        else 0
    )


    # --------------------------------------------------------
    # JOB ROLE ONE-HOT ENCODING
    # --------------------------------------------------------

    job_roles = [
        "Healthcare Representative",
        "Human Resources",
        "Laboratory Technician",
        "Manager",
        "Manufacturing Director",
        "Research Director",
        "Research Scientist",
        "Sales Executive",
        "Sales Representative"
    ]

    for role in job_roles:

        input_data[f"JobRole_{role}"] = (
            1 if job_role == role else 0
        )


    # --------------------------------------------------------
    # MARITAL STATUS ONE-HOT ENCODING
    # --------------------------------------------------------

    input_data["MaritalStatus_Divorced"] = (
        1 if marital_status == "Divorced" else 0
    )

    input_data["MaritalStatus_Married"] = (
        1 if marital_status == "Married" else 0
    )

    input_data["MaritalStatus_Single"] = (
        1 if marital_status == "Single" else 0
    )


    # --------------------------------------------------------
    # MATCH TRAINING FEATURE ORDER
    # --------------------------------------------------------

    input_data = input_data.reindex(
        columns=feature_names,
        fill_value=0
    )


    # --------------------------------------------------------
    # FEATURE VALIDATION
    # --------------------------------------------------------

    if list(input_data.columns) != list(feature_names):

        st.error(
            "Feature mismatch detected between the input data "
            "and the trained model."
        )

        st.stop()


    # ========================================================
    # MAKE PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    probability_percent = probability * 100


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.divider()

    st.subheader("🔍 Prediction Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        if prediction == 1:

            st.error(
                "⚠️ Employee is predicted to leave"
            )

        else:

            st.success(
                "✅ Employee is predicted to stay"
            )


    with result_col2:

        st.metric(
            "Attrition Probability",
            f"{probability_percent:.2f}%"
        )


    # --------------------------------------------------------
    # PROBABILITY VISUALIZATION
    # --------------------------------------------------------

    st.write("### Attrition Probability")

    st.progress(
        int(round(probability_percent))
    )


    if prediction == 1:

        st.warning(
            f"""
            The model predicts **Attrition** with an estimated
            probability of **{probability_percent:.2f}%**.
            """
        )

    else:

        st.info(
            f"""
            The model predicts **No Attrition** with an estimated
            attrition probability of **{probability_percent:.2f}%**.
            """
        )


    # --------------------------------------------------------
    # PREDICTION DETAILS
    # --------------------------------------------------------

    st.subheader("📊 Prediction Details")

    detail_col1, detail_col2 = st.columns(2)

    with detail_col1:

        st.metric(
            "Predicted Class",
            "Attrition" if prediction == 1
            else "No Attrition"
        )

    with detail_col2:

        st.metric(
            "No-Attrition Probability",
            f"{(1 - probability) * 100:.2f}%"
        )


    # --------------------------------------------------------
    # EMPLOYEE INPUT SUMMARY
    # --------------------------------------------------------

    with st.expander("📋 View Employee Information"):

        summary = pd.DataFrame({

            "Feature": [

                "Age",
                "Gender",
                "Marital Status",
                "Education",
                "Education Field",
                "Department",
                "Job Role",
                "Job Level",
                "Job Involvement",
                "Job Satisfaction",
                "Environment Satisfaction",
                "Work-Life Balance",
                "Monthly Income",
                "Monthly Rate",
                "Hourly Rate",
                "Daily Rate",
                "Percent Salary Hike",
                "OverTime",
                "Business Travel",
                "Distance From Home",
                "Total Working Years",
                "Years at Company",
                "Years in Current Role",
                "Years Since Last Promotion",
                "Years With Current Manager",
                "Number of Companies Worked",
                "Training Times Last Year",
                "Stock Option Level",
                "Relationship Satisfaction",
                "Performance Rating"

            ],

            "Value": [

                age,
                gender,
                marital_status,
                education,
                education_field,
                department,
                job_role,
                job_level,
                job_involvement,
                job_satisfaction,
                environment_satisfaction,
                work_life_balance,
                monthly_income,
                monthly_rate,
                hourly_rate,
                daily_rate,
                percent_salary_hike,
                overtime,
                business_travel,
                distance_from_home,
                total_working_years,
                years_at_company,
                years_current_role,
                years_since_promotion,
                years_with_manager,
                num_companies,
                training_times,
                stock_option,
                relationship_satisfaction,
                performance_rating

            ]
        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Employee Attrition Prediction | "
    "Random Forest Classifier | "
    "Machine Learning + Streamlit"
)
