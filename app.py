
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Cybersecurity Skills Forecast",
    page_icon="🔐",
    layout="centered"
)

# Main Title
st.title("🔐 Future Cybersecurity Skills – POC Demo")

# Description
st.markdown("""
Welcome to our project demo for **predicting future skill needs in cybersecurity**.
This is a proof-of-concept for how companies can align with upcoming trends.

Use the tabs below to explore:
- 📊 Skill trends from past data
- 🏢 Company-specific skill gaps
- 🧭 Strategic workforce recommendations
""")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Skill Trends", "🏢 Company Fit", "🧭 Recommendations"])

# === Tab 1: Skill Trends ===
with tab1:
    st.subheader("Top Emerging Skills (2023–2025)")
    st.markdown("These are the cybersecurity skills showing strong growth signals.")
    
    try:
        st.image("images/skill_trend_chart.png", caption="Sample skill trends (placeholder)")
    except:
        st.warning("No image found. Add 'skill_trend_chart.png' to the images folder.")

    st.markdown("""
    **Example skills:**
    - Zero Trust Architecture  
    - Threat Modeling  
    - Quantum Cryptography  
    """)

# === Tab 2: Company Fit ===
with tab2:
    st.subheader("Company: SecureFuture AB")
    st.markdown("""
    A fictional company focused on cloud security and SOC automation.
    
    **Current workforce size:** 50  
    **Strategic goal:** Full Zero Trust rollout by 2025
    """)

    try:
        st.image("images/skill_gap_chart.png", caption="Skill gap analysis (placeholder)")
    except:
        st.warning("No image found. Add 'skill_gap_chart.png' to the images folder.")

    st.markdown("**Top gaps identified:**")
    st.markdown("- 🟥 Zero Trust Design (+3 staff needed)\n- 🟨 AI-assisted Threat Detection (+2)\n- 🟩 Cloud Security (no gap)")

# === Tab 3: Recommendations ===
with tab3:
    st.subheader("What Should the Company Do?")
    st.markdown("""
    ✅ **Upskill Internal Teams**  
    - Train 3 current staff in Zero Trust Architecture  
    - Offer certifications in AI-driven threat detection

    ✅ **New Hires**  
    - Recruit 2 experts in threat modeling with experience in automation tools

    ✅ **Long-term Strategy**  
    - Track trends quarterly  
    - Use skill forecasting in hiring plans
    """)

# Footer
st.markdown("---")
st.markdown("📅 May 2025 · A Project Management Course POC · Made with ❤️ and Streamlit")