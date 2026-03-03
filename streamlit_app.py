import streamlit as st
import time

# 1. ตั้งค่าหน้าแอป (เช็ค Syntax เรียบร้อย)
st.set_page_config(page_title="GIE BALL PRO - วิเคราะห์บอลคืนนี้", page_icon="⚽", layout="wide")

# 2. CSS โทนดำ-ทอง สไตล์เซียนกี้
st.markdown("""
    <style>
    .stApp { background-color: #0b101a; color: #ffffff; }
    .league-header { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; padding: 10px; border-radius: 5px; font-weight: bold; margin: 25px 0 10px 0; text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ffd700; color: black; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #ffea00; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown("<h1 style='text-align: center; color: #ffd700;'>⚽ GIE BALL PRO : DATA TODAY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>วิเคราะห์เจาะลึกตามโปรแกรมจริง | อัปเดต 3 มี.ค. 2026</p>", unsafe_allow_html=True)

def run_ai_logic(h_name, a_name, tip, score):
    with st.spinner(f'AI มิ้น กำลังประมวลผลสถิติ...'):
        time.sleep(0.5)
    st.info(f"🎯 **เซียนกี้ฟันธง:** {tip}")
    st.success(f"💰 **สกอร์ที่คาด:** {score}")

# --- 1. พรีเมียร์ลีก อังกฤษ (4 คู่) ---
st.markdown("<div class='league-header'>🏴󠁧󠁢󠁥󠁮󠁧󠁿 พรีเมียร์ลีก อังกฤษ</div>", unsafe_allow_html=True)
pl_matches = [
    ("เอฟเวอร์ตัน", "เบิร์นลีย์", "02:30", "pl1", "ทอฟฟี่หนีตายใส่ยับ", "2-1"),
    ("บอร์นมัธ", "เบรนท์ฟอร์ด", "02:30", "pl2", "เจ้าบ้านในรังไว้ใจได้", "1-0"),
    ("ลีดส์ ยูไนเต็ด", "ซันเดอร์แลนด์", "02:30", "pl3", "ยูงทองนัดตกค้างต้องเน้น", "2-0"),
    ("วูล์ฟแฮมป์ตัน", "ลิเวอร์พูล", "03:15", "pl4", "คู่บิ๊กแมตช์! หงส์แดงบุกตบ", "1-3")
]
for h, a, t, k, tip, sc in pl_matches:
    st.write(f"🕒 **{t} น. | {h} vs {a}**")
    if st.button("🔍 วิเคราะห์", key=k): run_ai_logic(h, a, tip, sc)

# --- 2. เอฟเอ คัพ อังกฤษ (1 คู่) ---
st.markdown("<div class='league-header'>🏆 เอฟเอ คัพ อังกฤษ (นัดรีเพลย์)</div>", unsafe_allow_html=True)
st.write("🕒 **02:45 น. | พอร์ท เวล vs บริสตอล ซิตี้**")
if st.button("🔍 วิเคราะห์", key="fa1"):
    run_ai_logic("พอร์ท เวล", "บริสตอล ซิตี้", "ทีมเยือนดูดีกว่าเล็กน้อย", "1-2")

# --- 3. โกปา เดล เรย์ สเปน (1 คู่) ---
st.markdown("<div class='league-header'>🇪🇸 โกปา เดล เรย์ สเปน (รอบรองฯ เลก 2)</div>", unsafe_allow_html=True)
st.write("🕒 **03:00 น. | บาร์เซโลน่า vs แอตเลติโก มาดริด**")
st.warning("⚠️ เลกแรกแอตฯ ชนะ 4-0 คืนนี้บาร์ซ่าต้องยิงคืนหนักมาก!")
if st.button("🔍 วิเคราะห์", key="sp1"):
    run_ai_logic("บาร์ซ่า", "แอต.มาดริด", "บาร์ซ่าบุกแหลกเพื่อกู้หน้า", "3-1")

# --- 4. โคปปา อิตาเลีย (1 คู่) ---
st.markdown("<div class='league-header'>🇮🇹 โคปปา อิตาเลีย (รอบรองฯ)</div>", unsafe_allow_html=True)
st.write("🕒 **03:00 น. | โคโม่ vs อินเตอร์ มิลาน**")
if st.button("🔍 วิเคราะห์", key="it1"):
    run_ai_logic("โคโม่", "อินเตอร์", "งูใหญ่เหนือกว่าทุกขุมกำลัง", "0-2")

# --- 5. เฟร้นช์ คัพ ฝรั่งเศส (1 คู่) ---
st.markdown("<div class='league-header'>🇫🇷 เฟร้นช์ คัพ ฝรั่งเศส</div>", unsafe_allow_html=True)
st.write("🕒 **03:00 น. | สตราส์บูร์ก vs แร็งส์**")
if st.button("🔍 วิเคราะห์", key="fr1"):
    run_ai_logic("สตราส์บูร์ก", "แร็งส์", "บอลถ้วยออกหน้าเสมอหน้ากว้าง", "1-1")

# --- 6. เคเอ็นวีบี คัพ เนเธอร์แลนด์ (1 คู่) ---
st.markdown("<div class='league-header'>🇳🇱 เคเอ็นวีบี คัพ เนเธอร์แลนด์</div>", unsafe_allow_html=True)
st.write("🕒 **02:00 น. | เอ็นอีซี ไนเมเก้น พบ พีเอสวี**")
if st.button("🔍 วิเคราะห์", key="nl1"):
    run_ai_logic("ไนเมเก้น", "พีเอสวี", "พีเอสวีมาตรฐานสูงกว่าเยอะ", "0-3")

# 🚀 Visitor Counter
st.write("---")
st.markdown(f'<div style="text-align: center;"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgieball2.streamlit.app&count_bg=%23FFD700&title_bg=%23555555&icon=skype.svg&title=Visitors"/></div>', unsafe_allow_html=True)
