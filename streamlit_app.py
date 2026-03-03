import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (แก้ไข import ตัวเล็กเรียบร้อย)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลโลก", page_icon="⚽", layout="wide")

# 2. ปรับแต่ง CSS (ดีไซน์ทอง-ดำ ของเซียนกี้)
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 20px 0 10px 0; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ffea00; color: black; }
    .counter-container { text-align: center; background-color: #161b28; padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-top: 40px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DAILY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์ทุกลีกคืนนี้ 3 มี.ค. 2026 | โดย เซียนกี้ & AI มิ้น</p>", unsafe_allow_html=True)

def run_ai_logic(h_name, a_name, h_p, d_p, a_p, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลคู่ {h_name}...'):
        time.sleep(1)
    col1, col2, col3 = st.columns(3)
    col1.metric(h_name, f"{h_p}%")
    col2.metric("เสมอ", f"{d_p}%")
    col3.metric(a_name, f"{a_p}%")
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์คาด:** {score}")

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE</div>", unsafe_allow_html=True)
for match in [("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "p1"), ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "p2"), ("วูล์ฟส์", "ลิเวอร์พูล", "03:15", "p3")]:
    st.write(f"🕒 **{match[2]} น. | {match[0]} vs {match[1]}**")
    if st.button("🔍 วิเคราะห์", key=match[3]):
        run_ai_logic(match[0], match[1], 45, 25, 30, "เจ้าบ้านดูดีกว่าเล็กน้อย", "2-1")

# --- 🏴󠁧󠁢󠁥󠁮󠁧󠁿 CHAMPIONSHIP ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 CHAMPIONSHIP</div>", unsafe_allow_html=True)
for match in [("ลีดส์ ยูไนเต็ด", "ซันเดอร์แลนด์", "02:30", "c1"), ("นอริช", "สโต๊ค", "02:45", "c2"), ("ฮัลล์ ซิตี้", "สวอนซี", "02:45", "c3")]:
    st.write(f"🕒 **{match[2]} น. | {match[0]} vs {match[1]}**")
    if st.button("🔍 วิเคราะห์", key=match[3]):
        run_ai_logic(match[0], match[1], 50, 30, 20, "เจ้าบ้านเน้นผลการแข่งขัน", "1-0")

# --- 🇮🇹 COPPA ITALIA ---
st.markdown("<div class='league-header'>🇮🇹 COPPA ITALIA</div>", unsafe_allow_html=True)
st.write("🕒 **03:00 น. | โคโม่ vs อินเตอร์ มิลาน**")
if st.button("🔍 วิเคราะห์", key="it1"):
    run_ai_logic("โคโม่", "อินเตอร์", 10, 20, 70, "อินเตอร์ขี่มิด กินนิ่ม!", "0-3")

# --- 🇪🇸 COPA DEL REY ---
st.markdown("<div class='league-header'>🇪🇸 COPA DEL REY</div>", unsafe_allow_html=True)
st.write("🕒 **03:00 น. | บาร์เซโลน่า vs แอต.มาดริด**")
if st.button("🔍 วิเคราะห์", key="sp1"):
    run_ai_logic("บาร์ซ่า", "แอต.มาดริด", 55, 25, 20, "บาร์ซ่าในบ้านดุดันกว่า", "2-1")

# --- 🏴󠁧󠁢󠁳󠁣󠁴󠁿 PREMIERSHIP ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁳󠁣󠁴󠁿 PREMIERSHIP</div>", unsafe_allow_html=True)
st.write("🕒 **02:45 น. | ดันดี ยูไนเต็ด vs เซนต์ เมียร์เรน**")
if st.button("🔍 วิเคราะห์", key="sc1"):
    run_ai_logic("ดันดี ยูฯ", "เซนต์ เมียร์เรน", 40, 30, 30, "ออกเสมอหน้ากว้าง", "1-1")

# --- 🇩🇪 DFB POKAL ---
st.markdown("<div class='league-header'>🇩🇪 DFB POKAL</div>", unsafe_allow_html=True)
st.write("🕒 **02:45 น. | ไอน์ทรัค แฟร้งค์เฟิร์ต vs ดอร์ทมุนด์**")
if st.button("🔍 วิเคราะห์", key="ge1"):
    run_ai_logic("แฟร้งค์เฟิร์ต", "ดอร์ทมุนด์", 35, 25, 40, "เสือเหลืองบุกมาเบียดชนะ", "1-2")

# --- 🇫🇷 LIGUE 2 ---
st.markdown("<div class='league-header'>🇫🇷 LIGUE 2</div>", unsafe_allow_html=True)
st.write("🕒 **02:45 น. | ปารีส เอฟซี vs แก็งก็อง**")
if st.button("🔍 วิเคราะห์", key="fr1"):
    run_ai_logic("ปารีส เอฟซี", "แก็งก็อง", 50, 30, 20, "เจ้าบ้านมีลุ้นเฉือน", "1-0")

# 🚀 Visitor Counter
st.markdown("<div class='counter-container'>", unsafe_allow_html=True)
st.write("📊 Visitors ของแท้จากระบบ Gieball2")
st.markdown(f'<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
