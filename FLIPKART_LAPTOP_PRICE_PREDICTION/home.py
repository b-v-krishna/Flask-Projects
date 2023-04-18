import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Bhanu's Profile", page_icon=":smiley:")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
profile_pic = Image.open(os.path.join(BASE_DIR, 'resources/images/pic.jpg'))
st.image(profile_pic, width=500)

st.title('Welcome to my Profile')
st.header("Hi, :blue[I'm Bhanu.]")

#education
st.subheader(":blue[EDUCATION]")
st.write("- B.TECH IN :red[COMPUTER SCIENCE], SRKR ENGINEERING COLLEGE 2019 - 2023\n\n\n  CGPA:8.24")
st.write("- INTERMEDIATE, NARAYANA JUNIOR COLLEGE 2017 - 2019\n\n\n  CGPA:10.0")

#experience
st.subheader(":blue[EXPERIENCE]")
st.write("- Intern - :red[INNOMATICS RESEARCH LABS]\n    FEB - APRIL 2023")
st.write("  • Developed NOTE TAKING APP, REGEX WEB APP by using Python, HTML, CSS, Flask.")
st.write("  • I had the opportunity to work on real-world problems through case studies and data analysis projects. ")
st.write("  • I worked on a case study for Dominos, where i analyzed their business operations and provided recommendations for optimizing their supply chain and delivery processes.In addition to that, I also worked on a marketing data analysis project where i have analyzed customer behavior data to help a local business optimize their marketing campaigns.")

#projects
st.subheader(":blue[PROJECTS]")
st.write("- :red[Movie Recommendation System]")
st.write("  • Developed a Recommendation System by using Numpy, Pandas,Cosine Similarity Metrics in Machine Learning.")
st.write("  • It recommends a movie to the user based on Content.")


# Skills 
st.subheader(":blue[SKILLS]")
st.write("- :red[Technical Skills:]")
st.write("• Java, Python, Data Structures, OOPS, MY SQL, HTML, CSS, Machine Learning.")
st.write("- Soft Skills:")
st.write(" • Problem Solving, Communication, Team Work.")

# Certificates 
st.subheader(":blue[CERTIFICATES]")
st.write("• Certificate of Completion in :red[Java programming] from Great Learning Academy")
st.write("• Certificate for completion of Programming Essentials in Python from Cisco Networking Academy")

# Achievements section
st.subheader(":blue[ACHIEVEMENTS]")
st.write("• Earned Gold Badge for :red[Python(5 star) ]and :red[Problem Solving(5 star) ]from Hackerrank")

st.write("Connect with me on:")
st.write("👉[LinkedIn](https://www.linkedin.com/in/bhanu-katuri/)")
st.write("👉[GitHub](https://github.com/b-v-krishna)")
