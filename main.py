import streamlit as st
bg="""
<style>
.stApp { 
    background-color: #000000;
    color : #CCCCFF;
}
</style>
"""
st.html(bg)
st.title("Peem's Bmi Calculator")
st.markdown("---")
Sex=st.radio("เพศ",("ชาย","หญิง"),horizontal=True);
Weight=st.number_input("นํ้าหนัก (Kg) :",value=20,min_value=10,max_value=200,step=1,)
Tall=st.number_input("ส่วนสูง (cm) :",value=100,min_value=1,max_value=200,step=1,)

Final=Weight/(Tall/100)**2

if st.button("Calculate"):
    if Sex=="ชาย":
        if Sex == "ชาย" and Final < 19:
            st.info(f"{Final:.2f} น้อยกว่า 19 ")
            st.success(f"{Final} นํ้าหนักตํ่ากว่าเกณฑ์ ")
            st.image("Man_1.jpg")
        
        elif Sex == "ชาย" and Final >=19.0 and Final <=24.9:
            st.info (f"{Final:.2f} อยู่ระหว่าง 19.0 - 24.9")
            st.success(f"{Final} นํ้าหนักสมส่วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินระยะเริ่มต้น")
            st.image("Man_2.jpg")

        elif Sex == "ชาย" and Final >=25 and Final <=29.9:
            st.info(f"{Final:.2f} อยู่ระหว่าง 25.0 - 29.9")
            st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็านหนักเกินมากระยะอ้วนเริ่มต้น")
            st.image("Man_3.jpg")

        else :
            if Final >=30.0:
                st.error(f"{Final:.2f} มากกว่า 30")
                st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วนมาก ")
                st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินมากโรคอ้วน")
                st.image("Man_4.jpg")
        
    else:
        if Final < 18:
            st.info(f"{Final:.2f} น้อยกว่า 18 ")
            st.success(f"{Final} นํ้าหนักตํ่ากว่าเกณฑ์ ")
            st.image("Woman_1.jpg")

        elif Final >=18.0 and Final <=23.9:
            st.info (f"{Final:.2f} อยู่ระหว่าง 18.0 - 23.9")
            st.success(f"{Final} นํ้าหนักสมส่วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินระยะเริ่มต้น")
            st.image("Woman_2.jpg")

        elif Final >=24 and Final <=29.9:
            st.info(f"{Final:.2f} อยู่ระหว่าง 24.0 - 29.9")
            st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็านหนักเกินมากระยะอ้วนเริ่มต้น")
            st.image("Woman_3.jpg")
        
        else :
            if Final >=30.0:
                st.error(f"{Final:.2f} มากกว่า 30")
                st.success(f"{Final} นํ้าหนักอยู่ในเกณฑ์อ้วนมาก ")
                st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินมากโรคอ้วน")
                st.image("Woman_4.jpg")


