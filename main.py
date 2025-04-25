import streamlit as st
bg="""
<style>
.stApp { 
    backgroung-image: url ("https://sdmntpreastus2.oaiusercontent.com/files/00000000-095c-61f6-b7f3-2de3715f638a/raw?se=2025-04-25T08%3A48%3A25Z&sp=r&sv=2024-08-04&sr=b&scid=2af5761f-4b29-5641-8ead-858360f70595&skoid=ac1d63ad-0c69-4017-8785-7a50eb04382c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-25T00%3A05%3A48Z&ske=2025-04-26T00%3A05%3A48Z&sks=b&skv=2024-08-04&sig=qWA/J0iuB8GM6Y3Lzw9wbvRZk8HO/ei08QS9/h7tZac%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color : #000000;
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
            st.success(f"นํ้าหนักตํ่ากว่าเกณฑ์ ")
            st.warning(f"ภาวะแทรกซ้อน : เสี่ยงโรคขาดสารอาหาร")
            st.image("S__13738042_0.jpg")
        
        elif Sex == "ชาย" and Final >=19.0 and Final <=24.9:
            st.info (f"{Final:.2f} อยู่ระหว่าง 19.0 - 24.9")
            st.success(f"นํ้าหนักสมส่วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินระยะเริ่มต้น")
            st.image("S__13738044_0.jpg")

        elif Sex == "ชาย" and Final >=25 and Final <=29.9:
            st.info(f"{Final:.2f} อยู่ระหว่าง 25.0 - 29.9")
            st.success(f"นํ้าหนักอยู่ในเกณฑ์อ้วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็านหนักเกินมากระยะอ้วนเริ่มต้น")
            st.image("S__13738045_0.jpg")

        else :
            if Final >=30.0:
                st.error(f"{Final:.2f} มากกว่า 30")
                st.success(f"นํ้าหนักอยู่ในเกณฑ์อ้วนมาก ")
                st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินมากโรคอ้วน")
                st.image("S__13738046_0.jpg")
        
    else:
        if Final < 18:
            st.info(f"{Final:.2f} น้อยกว่า 18 ")
            st.success(f"นํ้าหนักตํ่ากว่าเกณฑ์ ")
            st.image("S__13738047_0.jpg")

        elif Final >=18.0 and Final <=23.9:
            st.info (f"{Final:.2f} อยู่ระหว่าง 18.0 - 23.9")
            st.success(f"นํ้าหนักสมส่วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินระยะเริ่มต้น")
            st.image("S__13738049_0.jpg")

        elif Final >=24 and Final <=29.9:
            st.info(f"{Final:.2f} อยู่ระหว่าง 24.0 - 29.9")
            st.success(f"นํ้าหนักอยู่ในเกณฑ์อ้วน")
            st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ็านหนักเกินมากระยะอ้วนเริ่มต้น")
            st.image("S__13738050_0.jpg")
        
        else :
            if Final >=30.0:
                st.error(f"{Final:.2f} มากกว่า 30")
                st.success(f"นํ้าหนักอยู่ในเกณฑ์อ้วนมาก ")
                st.warning(f"ภาวะแทรกซ้อน : ภาวะนํ้าหนักเกินมากโรคอ้วน")
                st.image("S__13738051_0.jpg")

st.markdown("---")


