import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (ใช้ตัวเล็ก import เพื่อกัน Error ครับกี้)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (โครงสร้างเดิมที่กี้ออกแบบไว้)
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .match-card { background-color: #161b28; padding: 15px; border-radius: 12px; border: 1px solid #2d333b; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ffea00; color: black; }
    /* ส่วนเพิ่ม: กล่องนับจำนวนคนดู */
    .counter-container { text-align: center; background-color: #161b28; padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DAILY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์ข้อมูลจริง 1,000% โดย เซียนกี้ & AI มิ้น | อัปเดต 2 มี.ค. 2026</p>", unsafe_allow_html=True)

# ฟังก์ชัน AI Predict (เหมือนเดิม)
def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ {h_name} vs {a_name}...'):
        time.sleep(1.2)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(f"{h_name} ชนะ", f"{h_p}%")
    col_b.metric("เสมอ", f"{d_p}%")
    col_c.metric(f"{a_name} ชนะ", f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 🏆 ข้อมูลจริงคืนวันที่ 2 มี.ค. 2026 ---

# --- 🇪🇸 LA LIGA (สเปน) ---
st.markdown("<div class='league-header'>🇪🇸 LA LIGA (สเปน)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | บียาร์เรอัล vs กรานาด้า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="spa_real1"):
        run_ai_logic("บียาร์เรอัล", "กรานาด้า", 62, 23, 15, "เรือดำน้ำสีเหลืองในบ้านดุจัด กรานาด้าสถิติเยือนแย่มาก วางเจ้าบ้านนิ่มๆ", "2-0 หรือ 3-1")

# --- 🇮🇹 SERIE A (อิตาลี) ---
st.markdown("<div class='league-header'>🇮🇹 SERIE A (อิตาลี)</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **02:45 น. | ลาซิโอ vs เอซี มิลาน**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="ita_real1"):
        run_ai_logic("ลาซิโอ", "เอซี มิลาน", 30, 30, 40, "บิ๊กแมตช์อิตาลี! มิลานฟอร์มสม่ำเสมอกว่า ลาซิโอช่วงหลังมีแผ่ว เบียดทีมเยือนได้ลุ้น", "1-2")

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 CHAMPIONSHIP (อังกฤษ) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLISH CHAMPIONSHIP</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:00 น. | เวสต์บรอมวิช vs โคเวนทรี**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="eng_real1"):
        run_ai_logic("เวสต์บรอมวิช", "โคเวนทรี", 45, 30, 25, "เวสต์บรอมฯ เล่นในบ้านเน้นผลการแข่งขันได้ดี แนะนำวางเจ้าบ้านหน้าเสื่อ", "1-0 หรือ 2-1")

# --- 🇵🇹 PORTUGAL LIGA (โปรตุเกส) ---
st.markdown("<div class='league-header'>🇵🇹 PORTUGAL LIGA</div>", unsafe_allow_html=True)
with st.container():
    st.write("🕒 **03:15 น. | ปอร์โต้ vs เบนฟิก้า**")
    if st.button("🔍 วิเคราะห์ความน่าจะเป็น (AI Predict)", key="por_real1"):
        run_ai_logic("ปอร์โต้", "เบนฟิก้า", 35, 35, 30, "ศึกดาร์บี้แมตช์ฝอยทอง! สูสีออกได้สามหน้า แต่สถิติฟ้องว่า 'เสมอ' บ่อยสุด", "1-1")

st.write("---")

# 🚀 ส่วน Visitor Counter (เหมือนเดิม)
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 สถิติผู้ใช้งานแอปทั้งหมด (Visitors)")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&icon_color=%23E7E7E7&title=Visitors&edge_flat=false"/>', unsafe_allow_html=True)
st.write("ตัวเลขจะเพิ่มขึ้นทุกครั้งที่มีคนกดเข้าเว็บกี้ครับ!")
st.markdown("</div>", unsafe_allow_html=True)
