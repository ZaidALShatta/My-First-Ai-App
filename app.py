import streamlit as st

# 1. إعدادات الصفحة والتصميم CSS
st.set_page_config(page_title="مطعم الفخامة الذكي", layout="wide")

st.markdown("""
    <style>
    /* زر واتساب الثابت عاليمين */
    .fixed-whatsapp {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25d366;
        color: white;
        padding: 15px;
        border-radius: 50%;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        z-index: 1000;
        font-size: 24px;
        text-decoration: none;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    <a href="https://wa.me/963985033064" class="fixed-whatsapp" target="_blank">💬</a>
    """, unsafe_allow_html=True)

# 2. إنشاء التبويبات (Tabs)
tab1, tab2, tab3, tab4 = st.tabs(["📜 المنيو", "🛍️ اطلب الآن", "🖼️ معرض الصور", "⭐ التقييمات"])

# --- الصفحة 1: المنيو ---
with tab1:
    st.header("📜 قائمة الطعام")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🍔 البرجر\n- كلاسيك: 25,000\n- دبل تشيز: 35,000")
    with c2:
        st.markdown("### 🍕 البيتزا\n- مارغريتا: 30,000\n- فصول أربعة: 45,000")

# --- الصفحة 2: نظام الطلب المباشر ---
with tab2:
    st.header("🛍️ طلب جديد")
    with st.form("order_form"):
        name = st.text_input("الاسم الكريم")
        address = st.text_input("عنوان التوصيل")
        order_details = st.text_area("شو حابب تطلب؟")
        submitted = st.form_submit_button("إرسال الطلب لواتساب المطعم")
        
        if submitted:
            msg = f"طلب جديد من: {name}%0Aالعنوان: {address}%0Aالطلب: {order_details}"
            st.markdown(f'<meta http-equiv="refresh" content="0;url=https://wa.me/963985033064?text={msg}">', unsafe_allow_html=True)

# --- الصفحة 3: معرض الصور ---
with tab3:
    st.header("🖼️ لقطات من مطبخنا")
    img_cols = st.columns(3)
    # ملاحظة: استبدل الروابط بصور حقيقية للمطعم
    img_cols[0].image("https://via.placeholder.com/300x200", caption="وجباتنا الطازجة")
    img_cols[1].image("https://via.placeholder.com/300x200", caption="صالة الطعام")
    img_cols[2].image("https://via.placeholder.com/300x200", caption="أجواء السهرة")

# --- الصفحة 4: التقييمات ---
with tab4:
    st.header("⭐ آراء زبائننا")
    st.chat_message("user").write("**أحمد:** الأكل وصل سخن وطعمة بتجنن! بنصح فيه.")
    st.chat_message("user").write("**ليلى:** خدمة سريعة جداً ونظافة واضحة.")
