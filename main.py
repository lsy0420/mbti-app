import streamlit as st

 

# 페이지 설정

st.set_page_config(

    page_title="MBTI 청소년 문학 추천 ",

    page_icon="",

    layout="centered"

)

 

# 제목

st.title(" MBTI 청소년 문학 추천")

st.subheader(" 나의 MBTI에 맞는 청소년 문학을 찾아보세요!")

 

st.write("MBTI 유형을 선택하면 어울리는 청소년 문학을 추천해드립니다 ")

 

# MBTI 선택

mbti = st.selectbox(

    " MBTI 유형을 선택하세요",

    [

        "INTJ","INTP","ENTJ","ENTP",

        "INFJ","INFP","ENFJ","ENFP",

        "ISTJ","ISFJ","ESTJ","ESFJ",

        "ISTP","ISFP","ESTP","ESFP"

    ]

)

 

# 추천 도서 데이터

books = {

 

"INTJ": {

"title":"모모",

"author":"미하엘 엔데",

"desc":"시간을 훔치는 사람들에 맞서 싸우는 소녀 모모의 이야기. 깊은 사유와 철학적 메시지가 INTJ에게 잘 맞습니다."

},

 

"INTP": {

"title":"어린 왕자",

"author":"생텍쥐페리",

"desc":"세상과 인간을 깊이 생각하게 만드는 철학적 이야기."

},

 

"ENTJ": {

"title":"헝거게임",

"author":"수잔 콜린스",

"desc":"강한 리더십과 전략적 사고가 필요한 상황 속에서 성장하는 이야기."

},

 

"ENTP": {

"title":"셜록 홈즈",

"author":"아서 코난 도일",

"desc":"기발한 추리와 논리적 사고가 돋보이는 탐정 이야기."

},

 

"INFJ": {

"title":"나미야 잡화점의 기적",

"author":"히가시노 게이고",

"desc":"사람들의 고민을 통해 삶의 의미를 찾는 따뜻한 이야기."

},

 

"INFP": {

"title":"빨강머리 앤",

"author":"루시 모드 몽고메리",

"desc":"상상력 풍부한 앤의 성장 이야기."

},

 

"ENFJ": {

"title":"페인트",

"author":"이희영",

"desc":"청소년의 정체성과 가족에 대한 깊은 질문을 던지는 소설."

},

 

"ENFP": {

"title":"완득이",

"author":"김려령",

"desc":"유쾌하고 따뜻한 성장 이야기."

},

 

"ISTJ": {

"title":"마당을 나온 암탉",

"author":"황선미",

"desc":"책임감과 신념을 보여주는 감동적인 이야기."

},

 

"ISFJ": {

"title":"구름빵",

"author":"백희나",

"desc":"따뜻한 가족 이야기가 담긴 작품."

},

 

"ESTJ": {

"title":"데미안",

"author":"헤르만 헤세",

"desc":"자기 성장과 삶의 방향을 찾는 이야기."

},

 

"ESFJ": {

"title":"Wonder (원더)",

"author":"R.J. 팔라시오",

"desc":"다름을 이해하고 함께 살아가는 이야기."

},

 

"ISTP": {

"title":"로빈슨 크루소",

"author":"다니엘 디포",

"desc":"생존과 문제 해결 능력이 돋보이는 모험 이야기."

},

 

"ISFP": {

"title":"바람의 그림자",

"author":"카를로스 루이스 사폰",

"desc":"감성적인 분위기의 미스터리 성장 이야기."

},

 

"ESTP": {

"title":"해리포터",

"author":"J.K. 롤링",

"desc":"모험과 도전이 가득한 판타지 이야기."

},

 

"ESFP": {

"title":"찰리와 초콜릿 공장",

"author":"로알드 달",

"desc":"즐거움과 상상력이 가득한 이야기."

}

 

}

 

# 버튼

if st.button(" 도서 추천 받기"):

 

    st.balloons()

 

    book = books[mbti]

 

    st.success(f" {mbti}에게 추천하는 책!")

 

    st.markdown(f"""

###  {book['title']}

** 작가:** {book['author']}

 

 **추천 이유**

 

{book['desc']}

""")

 

    st.info(" 이 책은 MBTI 성향을 바탕으로 추천된 청소년 문학입니다.")
