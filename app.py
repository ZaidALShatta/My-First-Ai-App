import streamlit as st
from openai import OpenAI

# 1. إعدادات الصفحة والتصميم (HTML/CSS)
st.set_page_config(page_title="AI Content Master", page_icon="🤖")

st.markdown("""
    <style>
    /* خلفية الموقع المتدرجة */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    /* تنسيق صندوق الإدخال */
    .stTextInput>div>div>input {
        background-color: #1e1e2f !important;
        color: white !important;
        border-radius: 10px !important;
    }
    /* تنسيق الزر الرئيسي */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(45deg, #00dbde, #fc00ff);
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px;
        font-size: 18px;
    }
    /* تنسيق زر الواتساب */
    .whatsapp-btn {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        border-radius: 15px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("⚙️ الإعدادات")
    api_key = st.text_input("أدخل مفتاح OpenAI الخاص بك", type="password")
    st.markdown("---")
    st.write("🔧 **هل تريد تطبيقاً مخصصاً لمشروعك؟**")
    
    # رابط الواتساب مع رقمك السوري
    whatsapp_url = "https://wa.me/963985033064?text=أريد+طلب+تطبيق+ذكاء+اصطناعي+مخصص"
    st.markdown(f'<a href="{whatsapp_url}" class="whatsapp-btn">تواصل معي واتساب 💬</a>', unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي
st.title("صانع المحتوى الذكي 🤖✨")
st.write("أدخل فكرتك وسأقوم بتحويلها إلى سيناريو فيديو احترافي.")

with st.form("main_form"):
    topic = st.text_input("ما هو موضوع الفيديو اليوم؟")
    submit_button = st.form_submit_button("توليد الإبداع الآن 🚀")

if submit_button:
    if not api_key:
        st.error("⚠️ يرجى إدخال API Key في القائمة الجانبية.")
    elif not topic:
        st.warning("⚠️ يرجى كتابة عنوان للموضوع.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner('جاري التحليل والكتابة...'):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "أنت خبير تسويق رقمي وصانع محتوى محترف. اكتب سيناريو فيديو قصير (Reels/TikTok) باللغة العربية بأسلوب مشوق ومبدع."},
                        {"role": "user", "content": topic}
                    ]
                )
                st.success("✅ تم توليد السيناريو بنجاح!")
                st.markdown("### 📝 السيناريو المقترح:")
                st.info(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ حدث خطأ تقني: {e}")
