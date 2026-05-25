import streamlit as st
import pandas as pd
import joblib

# 페이지 설정
st.set_page_config(
    page_title="토마토 착과율 예측",
    page_icon="🍅",
    layout="centered"
)

# CSS 꾸미기
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #f8fff4, #e8f5e9);
}

.main {
    padding-top: 2rem;
}

h1 {
    color: #4e7d4e;
    text-align: center;
    font-size: 3rem !important;
}

.stButton>button {
    background-color: #7cb342;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 0.7rem 2rem;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #689f38;
    color: white;
}

[data-testid="stNumberInput"] {
    background-color: white;
    padding: 10px;
    border-radius: 15px;
    border: 2px solid #dcedc8;
}

.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    border: 3px dashed #aed581;
    text-align: center;
    font-size: 28px;
    color: #558b2f;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# 모델 불러오기
model = joblib.load("tomato_model.pkl")

# 제목
st.markdown("<h1>🍅 토마토 착과율 예측 🌱</h1>", unsafe_allow_html=True)

st.write("### 🌿 온실 환경 데이터를 입력해보세요!")

# 입력창
temp = st.number_input("🌡️ 내부온도", value=25.0)
humidity = st.number_input("💧 내부습도", value=60.0)
soil_temp = st.number_input("🪴 지온", value=20.0)

# 버튼
if st.button("🍅 예측하기"):

    input_data = pd.DataFrame(
        [[temp, humidity, soil_temp]],
        columns=['내부온도', '내부습도', '지온']
    )

    predicted = model.predict(input_data)

    # 결과 출력
    st.markdown(
        f"""
        <div class="result-box">
            🌟 예측 착과율 🌟<br><br>
            <b>{predicted[0]:.1f}%</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 멘트 추가
    if predicted[0] >= 80:
        st.balloons()
        st.success("🎉 토마토 상태가 아주 좋아요!")
    elif predicted[0] >= 60:
        st.info("🙂 적당히 좋은 환경이에요!")
    else:
        st.warning("⚠️ 환경 조절이 필요해요!")
