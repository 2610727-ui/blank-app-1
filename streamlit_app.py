import streamlit as st

# 1. 앱 제목과 안내 메시지
st.title("🎢 놀이기구 탑승 가능 여부 확인기")
st.write("아래에 키를 입력하고 결과를 확인하세요.")

st.markdown("---")

# 2. 키 입력 받기
height = st.number_input(
    label="키(cm)를 입력하세요", 
    min_value=0, 
    max_value=250, 
    value=130, 
    step=1
)

# 3. 판정 버튼
if st.button("탑승 가능 여부 확인"):
    if height < 100:
        st.error(f"❌ 입력하신 키는 {height}cm 입니다. **탑승 불가**합니다.")
    elif 100 <= height < 130:
        st.warning(f"⚠️ 입력하신 키는 {height}cm 입니다. **보호자 동행 시 탑승 가능**합니다.")
    elif 130 <= height < 195:
        st.success(f"✅ 입력하신 키는 {height}cm 입니다. **탑승 가능**합니다.")
    else:
        st.error(f"❌ 입력하신 키는 {height}cm 입니다. **탑승 불가**합니다.")
        # 기존 코드 맨 밑에 그대로 이어서 붙여넣으세요!
if __name__ == "__main__":
    import os
    os.system("streamlit run streamlit_app.py")