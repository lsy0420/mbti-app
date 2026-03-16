import streamlit as st
import random

st.set_page_config(
    page_title="MBTI 청소년 문학 & 포켓몬 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 청소년 문학 & 포켓몬 추천")
st.write("🧠 MBTI를 선택하면 **어울리는 청소년 문학 도서와 포켓몬**을 추천해드립니다! ✨")

st.divider()

mbti_types = [
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

selected_mbti = st.selectbox("🔎 MBTI를 선택하세요", mbti_types)

data = {

"INTJ":{
"title":"📘 모모",
"author":"미하엘 엔데",
"story":"시간을 빼앗는 회색 신사들에 맞서는 소녀 모모의 이야기.",
"pokemon":"뮤츠",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"poke_reason":"뮤츠는 지능적이고 전략적인 포켓몬으로 깊이 생각하는 INTJ와 잘 어울립니다."
},

"INTP":{
"title":"📗 어린 왕자",
"author":"생텍쥐페리",
"story":"여러 행성을 여행하며 삶의 의미를 탐구하는 이야기.",
"pokemon":"후딘",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
"poke_reason":"후딘은 높은 지능과 분석력을 가진 포켓몬으로 탐구형 INTP와 잘 맞습니다."
},

"ENTJ":{
"title":"📕 헝거 게임",
"author":"수잔 콜린스",
"story":"독재 사회에서 살아남기 위해 싸우는 소녀의 이야기.",
"pokemon":"리자몽",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"poke_reason":"리자몽은 강력한 리더 느낌의 포켓몬으로 카리스마 있는 ENTJ와 잘 어울립니다."
},

"ENTP":{
"title":"📙 퍼시 잭슨",
"author":"릭 라이어던",
"story":"그리스 신화 세계에서 벌어지는 모험 이야기.",
"pokemon":"팬텀",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
"poke_reason":"장난기 많고 창의적인 팬텀은 아이디어가 넘치는 ENTP와 비슷합니다."
},

"INFJ":{
"title":"📘 책 도둑",
"author":"마커스 주삭",
"story":"전쟁 속에서도 책과 희망을 지키는 이야기.",
"pokemon":"루기아",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
"poke_reason":"루기아는 신비롭고 깊은 성격을 가진 포켓몬으로 이상주의적 INFJ와 잘 맞습니다."
},

"INFP":{
"title":"📗 테라비시아로 가는 다리",
"author":"캐서린 패터슨",
"story":"상상 속 왕국을 만들며 성장하는 아이들의 이야기.",
"pokemon":"이브이",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
"poke_reason":"이브이는 가능성과 상상력이 많은 포켓몬으로 감성적인 INFP와 어울립니다."
},

"ENFJ":{
"title":"📕 원더",
"author":"R.J 팔라시오",
"story":"차이를 극복하고 친구들과 성장하는 이야기.",
"pokemon":"피카츄",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"poke_reason":"피카츄는 모두에게 사랑받는 포켓몬으로 따뜻한 ENFJ와 잘 맞습니다."
},

"ENFP":{
"title":"📙 빨간 머리 앤",
"author":"루시 모드 몽고메리",
"story":"상상력이 풍부한 앤의 성장 이야기.",
"pokemon":"토게피",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
"poke_reason":"밝고 긍정적인 토게피는 자유로운 ENFP와 어울립니다."
},

"ISTJ":{
"title":"📘 작은 아씨들",
"author":"루이자 메이 올컷",
"story":"가족과 책임을 중심으로 한 성장 이야기.",
"pokemon":"거북왕",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
"poke_reason":"차분하고 안정적인 거북왕은 책임감 있는 ISTJ와 비슷합니다."
},

"ISFJ":{
"title":"📗 키다리 아저씨",
"author":"진 웹스터",
"story":"따뜻한 도움 속에서 성장하는 이야기.",
"pokemon":"해피너스",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
"poke_reason":"해피너스는 다른 포켓몬을 돌보는 성격이라 ISFJ와 잘 맞습니다."
},

"ESTJ":{
"title":"📕 로빈슨 크루소",
"author":"다니엘 디포",
"story":"무인도에서 살아남는 생존 이야기.",
"pokemon":"마기라스",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png",
"poke_reason":"강력하고 리더십 있는 마기라스는 ESTJ와 비슷합니다."
},

"ESFJ":{
"title":"📙 비밀의 화원",
"author":"프랜시스 버넷",
"story":"정원을 통해 아이들이 변화하는 이야기.",
"pokemon":"님피아",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/700.png",
"poke_reason":"님피아는 관계와 유대를 중요하게 여겨 ESFJ와 잘 맞습니다."
},

"ISTP":{
"title":"📘 손도끼",
"author":"게리 폴슨",
"story":"자연 속에서 생존하는 소년 이야기.",
"pokemon":"루카리오",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
"poke_reason":"루카리오는 조용하지만 강한 전투 스타일로 ISTP와 비슷합니다."
},

"ISFP":{
"title":"📗 별을 헤아리며",
"author":"로이스 로리",
"story":"전쟁 속에서도 친구를 지키려는 이야기.",
"pokemon":"세레비",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/251.png",
"poke_reason":"자연과 감성을 가진 세레비는 예술가형 ISFP와 잘 어울립니다."
},

"ESTP":{
"title":"📕 80일간의 세계일주",
"author":"쥘 베른",
"story":"세계 여행을 하는 모험 이야기.",
"pokemon":"갸라도스",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png",
"poke_reason":"강력하고 활동적인 갸라도스는 행동가 ESTP와 잘 맞습니다."
},

"ESFP":{
"title":"📙 찰리와 초콜릿 공장",
"author":"로알드 달",
"story":"초콜릿 공장에서 벌어지는 환상 이야기.",
"pokemon":"푸린",
"poke_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
"poke_reason":"귀엽고 사람을 즐겁게 하는 푸린은 ESFP와 잘 어울립니다."
}

}

st.divider()

if st.button("📖 추천 보기"):

    info = data[selected_mbti]

    st.balloons()
    st.snow()

    st.subheader(info["title"])
    st.write("✍ 작가:", info["author"])

    st.markdown("### 📚 줄거리")
    st.write(info["story"])

    st.markdown("### 🐾 어울리는 포켓몬")
    st.image(info["poke_img"], width=200)

    st.markdown("### ⭐ 포켓몬 추천 이유")
    st.info(info["poke_reason"])

st.caption("📚 MBTI 청소년 문학 + 포켓몬 추천 앱")
