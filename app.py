import streamlit as st
from openai import OpenAI

# 1. تصميم المطعم (CSS)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .food-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }
    .price-tag {
        color: #e63946;
        font-weight: bold;
        font-size: 20px;
    }
    .stButton>button {
        background-color: #ffb703;
        color: #023047;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 مطعم المدينة الذكي")
st.write("أهلاً بك! تصفح المنيو أو اطلب من الذكاء الاصطناعي أن يختار لك.")

# 2. عرض المنيو (هون بنستخدم الـ HTML تبعك)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=200" width="100%">
            <h3>برجر كلاسيك</h3>
            <p class="price-tag">25,000 ل.س</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="food-card">
            <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=200" width="100%">
            <h3>بيتزا إيطالية</h3>
            <p class="price-tag">40,000 ل.س</p>
        </div>
    """, unsafe_allow_html=True)

# 3. ميزة الذكاء الاصطناعي (الاقتراحات)
st.divider()
st.subheader("🤖 محتار شو تاكل؟")
user_input = st.text_input("اكتب شو بتحب (مثلاً: شي حار، أو خفيف)")

if st.button("اعطني اقتراحاً"):
    # هون بنستخدم OpenAI لتلعب دور "الويتر الذكي"
    # لازم تكون حاطط الـ API Key بالسايد بار كما فعلنا سابقاً
    st.info("الويتر الذكي عم يفكر لك بأكلة طيبة...")
    # (هون بنحط نفس كود الـ OpenAI اللي تعلمناه بس بنغير الـ Prompt)

# 4. زر الطلب السريع
st.sidebar.markdown("""
    <a href="https://wa.me/963985033064?text=بدي+أطلب+وجبة" 
       style="display: block; text-align: center; padding: 15px; background-color: #25d366; color: white; border-radius: 10px; text-decoration: none; font-weight: bold;">
       طلب عبر واتساب 💬
    </a>
""", unsafe_allow_html=True)
