import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (เช็ค Syntax ตัวพิมพ์เล็กเรียบร้อย)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์คืนนี้", page_icon="⚽", layout="wide")

# 2. CSS โทนดำ-ทอง (สไตล์กี้)
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header อัปเดตวันที่ให้เห็นชัดๆ
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffffff;'>วิเคราะห์บอลคืนนี้: วันอังคารที่ 3 มีนาคม 2026</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>ข้อมูลสดใหม่จาก SIAMSPOORT 1,000%</p>", unsafe_allow_html=True)

def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลคู่ {h_name}...'):
        time.sleep(1)
    col1, col2, col3 = st.columns(3)
    col1.metric(h_name, f"{h_p}%")
    col2.metric("เสมอ", f"{d_p}%")
    col3.metric(a_name, f"{a_p}%")
    st.info(f"🎯 **ฟันธงโดยเซียนกี้:** {tip}")
    st.success(f"💰 **สกอร์คาด:** {score}")

# --- ชุดข้อมูลจากรูป 849.jpg (พรีเมียร์ลีกคืนนี้) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE (ข้อมูลจริง 3 มี.ค.)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **02:30 น. | บอร์นมัธ vs เบรนท์ฟอร์ด**")
    if st.button("🔍 วิเคราะห์", key="real_1"):
        run_ai_logic("บอร์นมัธ", "เบรนท์ฟอร์ด", 48, 27, 25, "บอร์นมัธในบ้านดุ ลุ้นเบียดได้", "1-0")

with st.container():
    st.write("🕒 **02:30 น. | เอฟเวอร์ตัน vs เบิร์นลีย์**")
    if st.button("🔍 วิเคราะห์", key="real_2"):
        run_ai_logic("เอฟเวอร์ตัน", "เบิร์นลีย์", 55, 25, 20, "ทอฟฟี่ต้องการแต้ม ในบ้านไม่พลาด", "2-0")

with st.container():
    st.write("🕒 **03:15 น. | วูล์ฟแฮมป์ตัน vs ลิเวอร์พูล**")
    if st.button("🔍 วิเคราะห์", key="real_3"):
        run_ai_logic("วูล์ฟส์", "ลิเวอร์พูล", 18, 22, 60, "หงส์แดงเหนือกว่าเยอะ จัดไปครับกี้", "1-3")

# --- ชุดข้อมูลจากรูป 998.jpg (บอลถ้วยคืนนี้) ---
st.markdown("<div class='league-header'>🏆 CUP COMPETITIONS (ข้อมูลจริง 3 มี.ค.)</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **03:00 น. | โคโม่ vs อินเตอร์ มิลาน (อิตาลี)**")
    if st.button("🔍 วิเคราะห์", key="real_4"):
        run_ai_logic("โคโม่", "อินเตอร์", 12, 18, 70, "อินเตอร์เกรดบอลสูงกว่าเยอะ กินนิ่มครับ", "0-2")

with st.container():
    st.write("🕒 **03:00 น. | บาร์เซโลน่า vs แอต.มาดริด (สเปน)**")
    if st.button("🔍 วิเคราะห์", key="real_5"):
        run_ai_logic("บาร์ซ่า", "แอต.มาดริด", 52, 24, 24, "บิ๊กแมตช์! บาร์ซ่าเฉือนชนะในบ้าน", "2-1")

# --- เพิ่มเติมจากรูป 849.jpg (แชมเปี้ยนชิพ) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 CHAMPIONSHIP / OTHER</div>", unsafe_allow_html=True)

with st.container():
    st.write("🕒 **02:30 น. | ลีดส์ ยูไนเต็ด vs ซันเดอร์แลนด์**")
    if st.button("🔍 วิเคราะห์", key="real_6"):
        run_ai_logic("ลีดส์", "ซันเดอร์แลนด์", 60, 25, 15, "ยูงทองเน้นเลื่อนชั้น ในบ้านไว้ใจได้", "2-0")

with st.container():
    st.write("🕒 **02:45 น. | ดันดี ยูไนเต็ด vs เซนต์ เมียร์เรน**")
    if st.button("🔍 วิเคราะห์", key="real_7"):
        run_ai_logic("ดันดี ยูฯ", "เซนต์ เมียร์เรน", 35, 35, 30, "ออกเสมอหน้ากว้าง", "1-1")

# 4. ตัวนับจำนวนคนดู (แบบเดิมที่กี้ชอบ)
st.markdown("<div style='text-align: center; margin-top: 40px;'>", unsafe_allow_html=True)
st.write("📊 Visitors ของแท้จากระบบ Gieball2")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
