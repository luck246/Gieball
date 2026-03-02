import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (มิ้นแก้ i ตัวเล็กให้แล้วครับกี้)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .match-card { background-color: #161b28; padding: 15px; border-radius: 12px; border: 1px solid #2d333b; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# ฟังก์ชัน AI Predict
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผล...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name}", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name}", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🏆 คู่บอลวันที่ 2 เมษายน 2026 ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (2 APR 2026)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **02:15 น. | ลิเวอร์พูล vs เชลซี**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="apr2_1"):
        run_ai_logic("ลิเวอร์พูล", "เชลซี", 55, 25, 20, "หงส์แดงในบ้านเน้นมาก เชลซีช่วงนี้ยังแกว่ง วางเจ้าบ้านยาวๆ", "2-1")

with st.container():
    st.write("🕒 **03:00 น. | แมนฯ ซิตี้ vs บาเยิร์น มิวนิค**")
    if st.button("🔍 วิเคราะห์ (AI Predict)", key="apr2_2"):
        run_ai_logic("แมนฯ ซิตี้", "บาเยิร์น", 50, 25, 25, "บอลระบบแมนฯ ซิตี้ในบ้านไว้ใจได้ที่สุดในโลกตอนนี้", "3-1")
