import streamlit as st
from openai import OpenAI

# إعدادات الصفحة
st.set_page_config(page_title="AI Content Creator", page_icon="🚀")

st.title("صانع المحتوى الذكي 🤖")
st.write("اكتب فكرتك واترك الباقي على الذكاء الاصطناعي")

# القائمة الجانبية للـ API Key
with st.sidebar:
    api_key = st.text_input("OpenAI API Key", type="password")
    st.info("احصل على مفتاحك من platform.openai.com")

# استخدام "نموذج" (Form) لمنع اختفاء البيانات
with st.form("my_form"):
    topic = st.text_input("عن ماذا تريد أن نكتب اليوم؟")
    submit_button = st.form_submit_button("توليد المحتوى الآن")

if submit_button:
    if not api_key:
        st.error("⚠️ يرجى إدخال الـ API Key في القائمة الجانبية أولاً.")
    elif not topic:
        st.warning("⚠️ يرجى كتابة موضوع أولاً.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner('جاري البرمجة وكتابة الإبداع...'):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "أنت خبير تسويق محترف، اكتب سيناريو فيديو جذاب ومبدع باللغة العربية."},
                        {"role": "user", "content": topic}
                    ]
                )
                st.success("✅ تم التجهيز!")
                st.markdown("---")
                st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ حدث خطأ: {e}")
