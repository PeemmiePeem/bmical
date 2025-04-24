import streamlit as st
st.title("Bmi Calculator")
st.markdown("---")
Weight=st.number_input("นํ้าหนัก (Kg) :",value=20,min_value=10,max_value=200,step=1,)
Tall=st.number_input("ส่วนสูง (cm) :",value=100,min_value=1,max_value=200,step=1,)

bg="""
<style>
.stApp { 
background-image: url ("https://wallpapercave.com/wp/wp9630625.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.html(bg)

Final=Weight/(Tall/100)**2

if st.button("Calculate"):
    if Final < 18.5:
        st.info(f"{Final:.2f} น้อยกว่า 18.5 ")
        st.success(f"{Final} นํ้าหนักตํ่ากว่าเกณฑ์ ")
        st.warning(f"ภาวะแทรกซ้อน : เสี่ยงขาดสารอาหาร")
        st.image("S__13484034_0.jpg")
        
    elif Final >=18.5 and Final <=22.9:
        st.info (f"{Final:.2f} อยู่ระหว่าง 18.5 - 22.9")
        st.success(f"{Final} นํ้าหนักสมส่วน")
        st.warning(f"ภาวะแทรกซ้อน : โอกาสมีโรคแทรกซ้อนน้อย")
        st.image("S__13484036_0.jpg")

    elif Final >=23.0 and Final <=24.9:
        st.info(f"{Final:.2f} อยู่ระหว่าง 23.0 - 24.9")
        st.success(f"{Final} นํ้าหนักเกินมาตรฐาน")
        st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินระยะเริ่มต้น")
        st.image("S__13484037_0.jpg")

    elif Final >=25.0 and Final <=29.9:
        st.error(f"{Final:.2f} อยู่ระหว่าง 25.0 - 29.9")
        st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วน ")
        st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็านหนักเกินมากระยะอ้วนเริ่มต้น")
        st.image("S__13484038_0.jpg")

    else:
        Final >=30.0;
        st.error(f"{Final:.2f} มากกว่า 30")
        st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วนมาก ")
        st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็าหนักเกินมากโรคอ้วน")
        st.image("S__13484039_0.jpg")


