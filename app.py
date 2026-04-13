import streamlit as st
from openai import OpenAI

# إعدادات الصفحة (لتشبه الصورة الاحترافية)
st.set_page_config(page_title="AI Content Creator", page_icon="🚀", layout="centered")

# تنسيق CSS لجعل الواجهة غامقة وفخمة (Dark Mode)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #7f00ff; color: white; }
    </style>
    """, unsafe_content_type=True)

st.title("صانع المحتوى الذكي 🤖")
st.write("اكتب فكرتك واترك الباقي على الذكاء الاصطناعي")

# مكان وضع الـ API Key الخاص بك
client = OpenAI(api_key="ضع_مفتاحك_هنا")

# واجهة المدخلات
topic = st.text_input("عن ماذا تريد أن نكتب اليوم؟")
platform = st.selectbox("اختار المنصة:", ["TikTok", "Instagram", "Facebook", "YouTube"])

if st.button("توليد المحتوى الآن"):
    if topic:
        with st.spinner('جاري البرمجة وكتابة الإبداع...'):
            # البرومبت السحري الذي صممته لك
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"أنت خبير تسويق محترف، اكتب سيناريو فيديو جذاب لمنصة {platform} عن الموضوع التالي بصيغة تبيع وتجذب المشاهدين."},
                    {"role": "user", "content": topic}
                ]
            )
            result = response.choices[0].message.content
            st.success("تم التجهيز!")
            st.markdown(f"### النتيجة المقترحة:\n {result}")
    else:
        st.warning("يرجى كتابة موضوع أولاً")