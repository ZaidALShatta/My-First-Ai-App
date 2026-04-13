
import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(page_title="AI Content Creator", page_icon="🚀")

st.title("صانع المحتوى الذكي 🤖")
st.write("اكتب فكرتك واترك الباقي على الذكاء الاصطناعي")

# مكان وضع الـ API Key
# ملاحظة: سنضعه لاحقاً في الإعدادات للأمان
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if st.button("توليد المحتوى الآن"):
    if not api_key:
        st.error("يرجى إدخال الـ API Key في القائمة الجانبية أولاً.")
    elif topic := st.text_input("عن ماذا تريد أن نكتب اليوم؟"):
        client = OpenAI(api_key=api_key)
        with st.spinner('جاري البرمجة وكتابة الإبداع...'):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "أنت خبير تسويق محترف، اكتب سيناريو فيديو جذاب."},
                        {"role": "user", "content": topic}
                    ]
                )
                st.success("تم التجهيز!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("يرجى كتابة موضوع")
