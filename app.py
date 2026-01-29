import streamlit as st
import pandas as pd
import numpy as np

# Set page config first
st.set_page_config(page_title="HealthBot Dashboard", layout="wide")

# Import plotting libraries after page config
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        /* Background Gradient */
        .main {
            background: linear-gradient(to bottom right, #b3e5fc, #f8bbd0);
        }
        /* Title */
        .title {
            font-size: 70px !important;
            font-weight: bold;
            text-align: center;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background: -webkit-linear-gradient(#ff4081, #0288d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        /* Subheaders */
        h2 {
            font-size: 36px !important;
            color: #0288d1;
            font-family: 'Segoe UI', sans-serif;
        }
        /* Paragraphs */
        .markdown-text-container p {
            font-size: 22px !important;
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        /* Sidebar boxes */
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #e1f5fe, #fce4ec);
        }
        .sidebar .stRadio > label {
            font-size: 20px !important;
            padding: 10px;
            background-color: #b3e5fc;
            border-radius: 10px;
            margin-bottom: 10px;
            display: block;
            transition: background 0.3s;
        }
        .sidebar .stRadio > label:hover {
            background-color: #81d4fa;
        }
        /* Buttons */
        .stButton>button {
            background-color: #0288d1;
            color: white;
            border-radius: 8px;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Create Sample Dataset ----------
@st.cache_data
def load_data():
    """Create sample health data if CSV doesn't exist"""
    np.random.seed(42)  # For reproducibility
    data = {
        'Name': [f'Person_{i}' for i in range(1, 51)],
        'Age': np.random.randint(20, 70, 50),
        'BMI': np.round(np.random.uniform(18, 35, 50), 2),
        'Heart_Rate': np.random.randint(60, 100, 50),
        'Blood_Pressure': np.random.randint(110, 140, 50),
        'Cholesterol': np.random.randint(150, 250, 50),
        'Blood_Sugar': np.random.randint(70, 150, 50),
        'Weight': np.round(np.random.uniform(50, 100, 50), 1),
        'Height': np.round(np.random.uniform(1.5, 1.9, 50), 2)
    }
    return pd.DataFrame(data)

# Load data
try:
    df = load_data()
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    numeric_columns = numeric_df.columns.tolist()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# ---------- Sidebar ----------
st.sidebar.markdown("### 🏥 HealthBot Menu")
option = st.sidebar.radio("Navigate to:", [
    "🏠 Home",
    "🧮 BMI Calculator",
    "📊 Visualizations",
    "🧾 Check Your Health"
])

# ------------------- HOME PAGE -------------------
if option == "🏠 Home":
    st.markdown('<h1 class="title">🏥 Welcome to HealthBot 🏥</h1>', unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align:center; font-size:24px; color:#0288d1; font-family:Helvetica, Arial, sans-serif;'>
        Your Personal Health Assistant Dashboard
        </p>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align:center; font-size:20px; color:#333333; font-family:Arial, sans-serif;'>
        HealthBot helps you track health metrics, check reports, and get wellness suggestions. 
        Stay fit, stay healthy! 🏃‍♀️🥗💪
        </p>
    """, unsafe_allow_html=True)

    # ---------- Key Metrics Boxes ----------
    total_users = 1200
    bmi_calculations = 875
    reports_checked = 450

    st.markdown("### Key Metrics")
    st.markdown(f"""
        <style>
            .card-container {{
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
                flex-wrap: wrap;
            }}
            .card {{
                background: #b3e5fc;
                border-radius: 15px;
                width: 300px;
                height: 300px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                transition: transform 0.3s, background 0.3s;
                margin: 15px;
            }}
            .card:hover {{
                transform: scale(1.05);
                background: #81d4fa;
            }}
            .card h2 {{
                font-size: 36px;
                margin: 0;
                color: #0288d1;
            }}
            .card p {{
                font-size: 18px;
                color: #333;
                text-align: center;
                padding: 0 10px;
            }}
        </style>
        <div class="card-container">
            <div class="card">
                <h2>🌟 {total_users}</h2>
                <p>Total Users</p>
                <p>People using HealthBot to track and maintain health metrics.</p>
            </div>
            <div class="card">
                <h2>🧮 {bmi_calculations}</h2>
                <p>BMI Calculations</p>
                <p>Users calculated their BMI to monitor weight and fitness levels.</p>
            </div>
            <div class="card">
                <h2>🧾 {reports_checked}</h2>
                <p>Reports Checked</p>
                <p>Users uploaded medical reports to get wellness suggestions.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- Sample Health Insights ----------
    st.markdown("### Sample Health Insights")

    col1, col2 = st.columns(2)
    
    with col1:
        # BMI Pie Chart
        bmi_data = pd.DataFrame({
            "BMI Category": ["Underweight", "Normal", "Overweight", "Obese"],
            "Count": [50, 400, 300, 125]
        })
        fig_bmi = px.pie(bmi_data, names="BMI Category", values="Count",
                         title="BMI Distribution", color_discrete_sequence=px.colors.sequential.Pinkyl)
        st.plotly_chart(fig_bmi, use_container_width=True)

    with col2:
        # Heart Disease Pie Chart
        heart_data = pd.DataFrame({
            "Heart Disease": ["Yes", "No"],
            "Count": [120, 1080]
        })
        fig_heart = px.pie(heart_data, names="Heart Disease", values="Count",
                           title="Heart Disease Prevalence", color_discrete_sequence=px.colors.sequential.Teal)
        st.plotly_chart(fig_heart, use_container_width=True)

    # Sample Line Chart
    st.markdown("### Sample Health Trends")
    fig, ax = plt.subplots(figsize=(10,4))
    days = np.arange(1, 8)
    weight = [65, 64.8, 64.5, 64.3, 64.0, 63.8, 63.7]
    steps = [7000, 7500, 8000, 6500, 9000, 8500, 8000]

    ax.plot(days, weight, marker='o', label="Weight (kg)", color="#ff4081", linewidth=2)
    ax2 = ax.twinx()
    ax2.plot(days, steps, marker='s', label="Steps per Day", color="#0288d1", linewidth=2)
    
    ax.set_xticks(days)
    ax.set_xlabel("Day", fontsize=12)
    ax.set_ylabel("Weight (kg)", fontsize=12, color="#ff4081")
    ax2.set_ylabel("Steps per Day", fontsize=12, color="#0288d1")
    ax.set_title("Sample Health Trends", fontsize=14)
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # Sample Bar Chart
    st.markdown("### Sample Average Health Metrics")
    health_metrics = ['BMI', 'Heart Rate', 'Blood Pressure', 'Cholesterol']
    avg_values = [22.5, 72, 120, 180]
    colors = ['#ff4081', '#0288d1', '#ff80ab', '#81d4fa']

    fig2, ax2 = plt.subplots(figsize=(8,5))
    bars = ax2.bar(health_metrics, avg_values, color=colors, alpha=0.8)
    ax2.set_ylabel("Average Value", fontsize=12)
    ax2.set_title("Sample Average Health Metrics", fontsize=14)
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

# ------------------- BMI CALCULATOR -------------------
elif option == "🧮 BMI Calculator":
    st.header("🧮 BMI Calculator")
    st.markdown("Calculate your Body Mass Index (BMI) to understand your weight category.")
    
    col1, col2 = st.columns(2)
    height = col1.number_input("Height (meters)", min_value=1.0, max_value=2.5, value=1.65, step=0.01)
    weight = col2.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=65.0, step=0.5)

    if st.button("Calculate BMI", use_container_width=True):
        bmi = weight / (height ** 2)
        st.markdown("---")
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("⚠️ Category: Underweight")
            st.info("💡 **Suggestion:** Consider consulting a nutritionist to develop a healthy weight gain plan.")
        elif bmi < 24.9:
            st.success("✅ Category: Normal weight")
            st.info("💡 **Suggestion:** Great! Maintain your current lifestyle with balanced diet and regular exercise.")
        elif bmi < 29.9:
            st.warning("⚠️ Category: Overweight")
            st.info("💡 **Suggestion:** Consider increasing physical activity and consulting a nutritionist for dietary advice.")
        else:
            st.error("🚨 Category: Obese")
            st.info("💡 **Suggestion:** It's recommended to consult with a healthcare provider for a comprehensive health plan.")
        
        # BMI Scale visualization
        st.markdown("### BMI Scale Reference")
        bmi_categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
        bmi_ranges = ['< 18.5', '18.5 - 24.9', '25 - 29.9', '≥ 30']
        bmi_colors = ['#FFD700', '#4CAF50', '#FFA500', '#F44336']
        
        fig, ax = plt.subplots(figsize=(10, 2))
        for i, (cat, rng, color) in enumerate(zip(bmi_categories, bmi_ranges, bmi_colors)):
            ax.barh(0, 1, left=i, color=color, alpha=0.7, edgecolor='black')
            ax.text(i + 0.5, 0, f'{cat}\n{rng}', ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Mark user's BMI
        if bmi < 18.5:
            position = 0.5
        elif bmi < 24.9:
            position = 1 + (bmi - 18.5) / (24.9 - 18.5)
        elif bmi < 29.9:
            position = 2 + (bmi - 25) / (29.9 - 25)
        else:
            position = 3.5
        
        ax.plot(position, 0, 'v', color='red', markersize=15, label=f'Your BMI: {bmi:.1f}')
        ax.set_xlim(0, 4)
        ax.set_ylim(-0.5, 0.5)
        ax.axis('off')
        ax.legend(loc='upper right')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# ------------------- VISUALIZATIONS -------------------
elif option == "📊 Visualizations":
    st.header("📊 Health Data Visualizations")
    st.markdown("Explore various health metrics through interactive visualizations.")
    
    chart_type = st.selectbox("Select Visualization Type", 
                              ["Bar Chart", "Line Chart", "Correlation Heatmap", "Distribution Plot"])
    
    if chart_type == "Bar Chart":
        metric = st.selectbox("Choose Metric", numeric_columns)
        st.markdown(f"### {metric} by Person")
        
        # Show only first 20 for readability
        df_subset = df.head(20)
        
        fig, ax = plt.subplots(figsize=(12,6))
        bars = ax.bar(range(len(df_subset)), df_subset[metric], color='#0288d1', alpha=0.7)
        ax.set_xlabel("Person Index", fontsize=12)
        ax.set_ylabel(metric, fontsize=12)
        ax.set_title(f"{metric} Distribution (First 20 People)", fontsize=14)
        ax.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        # Statistics
        st.markdown("### Statistics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Mean", f"{df[metric].mean():.2f}")
        col2.metric("Median", f"{df[metric].median():.2f}")
        col3.metric("Min", f"{df[metric].min():.2f}")
        col4.metric("Max", f"{df[metric].max():.2f}")
        
    elif chart_type == "Line Chart":
        metric = st.selectbox("Choose Metric", numeric_columns)
        st.markdown(f"### {metric} Trend by Age")
        
        # Sort by age for better visualization
        df_sorted = df.sort_values('Age')
        
        fig, ax = plt.subplots(figsize=(12,6))
        ax.plot(df_sorted['Age'], df_sorted[metric], marker='o', linestyle='-', 
                color='#ff4081', linewidth=2, markersize=6, alpha=0.7)
        ax.set_xlabel("Age", fontsize=12)
        ax.set_ylabel(metric, fontsize=12)
        ax.set_title(f"{metric} vs Age", fontsize=14)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
    elif chart_type == "Distribution Plot":
        metric = st.selectbox("Choose Metric", numeric_columns)
        st.markdown(f"### {metric} Distribution")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
        
        # Histogram
        ax1.hist(df[metric], bins=20, color='#0288d1', alpha=0.7, edgecolor='black')
        ax1.set_xlabel(metric, fontsize=12)
        ax1.set_ylabel("Frequency", fontsize=12)
        ax1.set_title(f"{metric} Histogram", fontsize=14)
        ax1.grid(axis='y', alpha=0.3)
        
        # Box plot
        ax2.boxplot(df[metric], vert=True, patch_artist=True,
                    boxprops=dict(facecolor='#ff4081', alpha=0.7),
                    medianprops=dict(color='red', linewidth=2))
        ax2.set_ylabel(metric, fontsize=12)
        ax2.set_title(f"{metric} Box Plot", fontsize=14)
        ax2.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
    else:  # Correlation Heatmap
        st.markdown("### Correlation Between Health Metrics")
        st.markdown("This heatmap shows how different health metrics relate to each other.")
        
        fig, ax = plt.subplots(figsize=(10,8))
        correlation_matrix = numeric_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", 
                   center=0, square=True, linewidths=1, 
                   cbar_kws={"shrink": 0.8}, ax=ax, fmt='.2f')
        ax.set_title("Health Metrics Correlation Matrix", fontsize=14, pad=20)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        st.markdown("""
        **How to read this heatmap:**
        - Values range from -1 to 1
        - 1 (dark red) = strong positive correlation
        - 0 (white) = no correlation
        - -1 (dark blue) = strong negative correlation
        """)

# ------------------- HEALTH REPORT CHECKER -------------------
elif option == "🧾 Check Your Health":
    st.header("🧾 Upload & Check Your Health Report")
    st.markdown("""
    Upload your medical report image and select the condition for personalized wellness suggestions.
    """)
    
    uploaded_image = st.file_uploader("Upload your medical report image", type=["png", "jpg", "jpeg"])
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Report", use_container_width=True)
        st.info("⚠️ **Important:** This tool provides general wellness suggestions and is NOT a substitute for professional medical advice.")
        
        st.markdown("---")
        issue = st.selectbox("Select the condition mentioned in your report (if known):", [
            "None / Not Sure",
            "High Blood Pressure",
            "Diabetes",
            "Anemia",
            "High Cholesterol",
            "Heart Disease",
            "Obesity",
            "Thyroid Issues",
            "Kidney Issues",
            "Liver Issues"
        ])
        
        if st.button("Get Wellness Suggestions", use_container_width=True):
            st.markdown("---")
            st.markdown("### 📋 Wellness Suggestions")
            
            suggestions = {
                "High Blood Pressure": [
                    ("⚠️", "warning", "Possible Hypertension detected."),
                    ("👨‍⚕️", "info", "**Consult:** Cardiologist or general physician for proper diagnosis and treatment plan."),
                    ("🥗", "success", "**Diet Tips:**\n- Reduce salt intake (< 5g per day)\n- Eat more fruits and vegetables\n- Include oats, bananas, and leafy greens\n- Avoid processed and fried foods"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Daily walking (30 minutes)\n- Practice stress-reduction techniques\n- Maintain healthy weight\n- Avoid smoking and limit alcohol")
                ],
                "Diabetes": [
                    ("⚠️", "warning", "Possible Diabetes condition."),
                    ("👨‍⚕️", "info", "**Consult:** Endocrinologist for blood sugar monitoring and medication."),
                    ("🥗", "success", "**Diet Tips:**\n- Choose low glycemic index foods\n- Include whole grains, legumes\n- Eat plenty of leafy vegetables\n- Avoid sugary drinks and desserts"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Regular exercise (150 min/week)\n- Monitor blood sugar levels\n- Maintain healthy weight\n- Stay hydrated")
                ],
                "Anemia": [
                    ("⚠️", "warning", "Possible Iron Deficiency (Anemia)."),
                    ("👨‍⚕️", "info", "**Consult:** Doctor for complete blood count test and iron supplementation."),
                    ("🥗", "success", "**Diet Tips:**\n- Iron-rich foods: spinach, beetroot, dates\n- Vitamin C foods for better absorption\n- Red meat, fish, and poultry\n- Fortified cereals and legumes"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Avoid tea/coffee with meals\n- Cook in iron utensils\n- Get adequate rest")
                ],
                "High Cholesterol": [
                    ("⚠️", "warning", "High cholesterol levels detected."),
                    ("👨‍⚕️", "info", "**Consult:** Doctor for lipid profile review and possible statin therapy."),
                    ("🥗", "success", "**Diet Tips:**\n- Eat oats, barley, and whole grains\n- Include nuts and fatty fish\n- Use olive oil instead of butter\n- Avoid trans fats and fried foods"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Regular aerobic exercise\n- Maintain healthy weight\n- Quit smoking\n- Limit alcohol consumption")
                ],
                "Heart Disease": [
                    ("⚠️", "warning", "Possible heart condition detected."),
                    ("👨‍⚕️", "info", "**Consult:** Cardiologist immediately for comprehensive cardiac evaluation."),
                    ("🥗", "success", "**Diet Tips:**\n- Low-fat, high-fiber diet\n- Plenty of fruits & vegetables\n- Omega-3 rich foods (fish, walnuts)\n- Limit sodium and saturated fats"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Supervised cardio exercises\n- Stress management techniques\n- Avoid smoking & alcohol\n- Regular health monitoring")
                ],
                "Obesity": [
                    ("⚠️", "warning", "Possible Obesity condition."),
                    ("👨‍⚕️", "info", "**Consult:** Nutritionist or physician for personalized weight management plan."),
                    ("🥗", "success", "**Diet Tips:**\n- Balanced low-calorie diet\n- Portion control\n- Reduce sugar & junk food\n- Increase protein and fiber intake"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Daily physical activity (walking, swimming)\n- Aerobic and strength training\n- Set realistic weight loss goals\n- Track food intake and progress")
                ],
                "Thyroid Issues": [
                    ("⚠️", "warning", "Possible Thyroid condition."),
                    ("👨‍⚕️", "info", "**Consult:** Endocrinologist for thyroid function tests and hormone therapy."),
                    ("🥗", "success", "**Diet Tips:**\n- Iodine-rich foods (seafood, dairy)\n- Selenium-rich foods (Brazil nuts)\n- Avoid processed foods\n- Include fruits & vegetables"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Moderate exercise routine\n- Regular thyroid checkups\n- Stress management\n- Adequate sleep (7-8 hours)")
                ],
                "Kidney Issues": [
                    ("⚠️", "warning", "Possible kidney condition."),
                    ("👨‍⚕️", "info", "**Consult:** Nephrologist for kidney function tests and treatment plan."),
                    ("🥗", "success", "**Diet Tips:**\n- Low-sodium diet\n- Controlled protein intake\n- Stay well-hydrated\n- Limit potassium and phosphorus\n- Fresh fruits & vegetables"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Avoid dehydration\n- Regular health monitoring\n- Control blood pressure\n- Avoid NSAIDs without doctor's advice")
                ],
                "Liver Issues": [
                    ("⚠️", "warning", "Possible liver condition."),
                    ("👨‍⚕️", "info", "**Consult:** Hepatologist for liver function tests and appropriate treatment."),
                    ("🥗", "success", "**Diet Tips:**\n- Completely avoid alcohol\n- Reduce fatty foods\n- Eat green leafy vegetables\n- Include antioxidant-rich foods\n- Stay hydrated"),
                    ("🏃", "success", "**Lifestyle Tips:**\n- Regular moderate exercise\n- Avoid toxin exposure\n- Maintain healthy weight\n- Vaccination for hepatitis")
                ],
                "None / Not Sure": [
                    ("✅", "success", "No specific issue selected."),
                    ("💡", "info", "**General Health Tips:**\n- Maintain balanced diet\n- Regular exercise (150 min/week)\n- Adequate sleep (7-8 hours)\n- Annual health checkups\n- Stay hydrated\n- Manage stress effectively")
                ]
            }
            
            for emoji, msg_type, msg in suggestions[issue]:
                if msg_type == "warning":
                    st.warning(f"{emoji} {msg}")
                elif msg_type == "success":
                    st.success(f"{emoji} {msg}")
                else:
                    st.info(f"{emoji} {msg}")
            
            st.markdown("---")
            st.markdown("""
            <div style='background-color: #fff3cd; padding: 15px; border-radius: 10px; border-left: 5px solid #ffc107;'>
            <strong>⚠️ Disclaimer:</strong> These are general wellness suggestions only. 
            Always consult with qualified healthcare professionals for proper diagnosis and treatment.
            Never ignore professional medical advice or delay seeking it because of information provided here.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("👆 Please upload a medical report image to get started.")

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>🏥 <strong>HealthBot Dashboard</strong> | Your Personal Health Assistant</p>
        <p style='font-size: 14px;'>Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
