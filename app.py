import streamlit as st

# 1. تصميم المطعم (CSS)
st.markdown("""
    <style>
    .food-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #ddd;
        text-align: center;
        margin-bottom: 10px;
    }
    .total-box {
        background-color: #023047;
        color: #ffb703;
        padding: 20px;
        border-radius: 10px;
        font-size: 25px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 منيو مطعم المدينة")
st.write("اختر وجباتك وسنحسب لك المجموع فوراً")

# تعريف الأسعار
price_burger = 25000
price_pizza = 40000
price_fries = 10000

total_price = 0
order_details = []

# 2. عرض المنيو مع خيارات الاختيار
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="food-card"><h3>برجر 🍔</h3><p>25,000 ل.س</p></div>', unsafe_allow_html=True)
    if st.checkbox("إضافة برجر", key="burger"):
        total_price += price_burger
        order_details.append("برجر")

with col2:
    st.markdown('<div class="food-card"><h3>بيتزا 🍕</h3><p>40,000 ل.س</p></div>', unsafe_allow_html=True)
    if st.checkbox("إضافة بيتزا", key="pizza"):
        total_price += price_pizza
        order_details.append("بيتزا")

with col3:
    st.markdown('<div class="food-card"><h3>بطاطا 🍟</h3><p>10,000 ل.س</p></div>', unsafe_allow_html=True)
    if st.checkbox("إضافة بطاطا", key="fries"):
        total_price += price_fries
        order_details.append("بطاطا")

st.divider()

# 3. عرض المجموع النهائي
if total_price > 0:
    st.markdown(f'<div class="total-box">الحساب الإجمالي: {total_price:,} ل.س</div>', unsafe_allow_html=True)
    
    # تجهيز رسالة الواتساب تلقائياً
    items_text = " + ".join(order_details)
    whatsapp_msg = f"مرحباً، أريد طلب: {items_text}. الحساب الإجمالي: {total_price:,} ل.س"
    whatsapp_url = f"https://wa.me/963985033064?text={whatsapp_msg}"
    
    st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="display: block; text-align: center; padding: 15px; background-color: #25d366; color: white; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top:10px;">إرسال الطلب عبر واتساب 💬</a>', unsafe_allow_html=True)
else:
    st.info("قم باختيار وجباتك من الأعلى للبدء بالطلب.")
