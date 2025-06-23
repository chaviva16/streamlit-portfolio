import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Otabor Favour | Data Scientist", layout="wide")


# --- Header Section ---
col1, col2 = st.columns([1, 5])
with col1:
    image = Image.open("images/profile.jpg")
    st.image(image, width=140)
with col2:
    st.markdown("<h1 style='margin-bottom:0;'>👩‍💻 Otabor Favour</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0;'>Data Scientist | Machine Learning | Analytics</h4>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- About Me ---
st.markdown("## 👋 About Me")
st.markdown("""
I am a passionate data enthusiast with a background in data science and machine learning.  
Skilled in Python, data analysis, and predictive modeling, I enjoy transforming raw data into actionable insights.  
Driven by curiosity and continuous learning, I’m dedicated to solving real-world problems through innovative technology and analytics.
""")

# --- Work Experience ---
st.markdown("## 💼 Work Experience")
st.markdown("""
**Data Science Intern**  
*The Meerge Africa Technologies Limited (Nov 2024 – Feb 2025)*  
- 🧠 Developed a food price prediction model using machine learning  
- 🧹 Collected, cleaned, and analyzed large datasets  
- 📊 Implemented regression models and optimized performance  
- 📈 Designed dashboards using Power BI to translate complex insights
""")

# --- Projects Section ---
st.markdown("## 🚀 Projects")
projects = {
    "Calories Burnt Prediction": "https://github.com/chaviva16/CALORIES-BURNT-PREDICTION-APP",
    "Car Price Prediction App": "https://github.com/chaviva16/CAR-PREDICTION-APP",
    "Movie Recommendation System": "https://github.com/chaviva16/MOVIE-RECOMMENDATION",
    "Disease Prediction System": "https://github.com/chaviva16/Disease_Prediction",
    "Customer Review Classifier": "https://github.com/chaviva16/customer_review_classifier",
}

col1, col2 = st.columns(2)
project_list = list(projects.items())
for i in range(0, len(project_list), 2):
    with col1:
        name, link = project_list[i]
        st.markdown(f"🔗 [{name}]({link})")
    if i + 1 < len(project_list):
        with col2:
            name, link = project_list[i + 1]
            st.markdown(f"🔗 [{name}]({link})")

# --- Skills Section ---
st.markdown("## 🧠 Skills")
skills = [
    "🐍 Python", "📊 Pandas", "🔢 NumPy", "📈 Scikit-learn", "🌐 Streamlit",
    "📊 Power BI", "🗄️ SQL", "🧠 NLP", "🔍 EDA", "⚙️ Model Tuning", "🧹 Data Cleaning", "🐙 Git/GitHub"
]
st.markdown(f"<p style='font-size: 16px;'>{' | '.join(skills)}</p>", unsafe_allow_html=True)

# --- Education Section ---
st.markdown("## 🎓 Education")
st.markdown("""
- 🎓 *GoMyCode* – Data Science Certificate (2024)  
- 🎓 *High School Diploma* – 2017  
""")

# --- Contact Section ---
st.markdown("## 📫 Contact")
st.markdown("""
- 📧 Email: [favourotabor16@gmail.com](mailto:favourotabor16@gmail.com)  
- 🐙 GitHub: [chaviva16](https://github.com/chaviva16)  
- 🐦 X (Twitter): [@chavivaotas](https://x.com/chavivaotas?s=21)  
- 💼 LinkedIn: [Favour Otabor](https://www.linkedin.com/in/favour-otabor-0705a82a6)
""")
