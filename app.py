import streamlit as st
import pandas as pd

# Creating the dataset
data = {
    "Manufacturer": [
        "We3 Group",
        "Dunamis Machines",
        "Shyam Plastic",
        "Blow Chenn Machines",
        "Alibaba Supplier"
    ],
    "Machine Name": [
        "Semi Auto Drop PET Blowing Machine",
        "Semi-Automatic PET Blow Moulding Machine",
        "Versatile PET Blow Moulding Machine",
        "Semi Automatic Pet Jar Blowing Machine",
        "Semi Automatic 5 Gallon PET Blowing Machine"
    ],
    "Capacity (ml)": [
        "50ml and above",
        "200ml - 2000ml",
        "50ml - 5000ml",
        "Up to 5 liters",
        "5-gallon containers"
    ],
    "Production Capacity (bottles/hour)": [
        "Varies",
        "Up to 1800",
        "Varies",
        "Varies",
        "Varies"
    ],
    "Price (INR/USD)": [
        "₹435,000",
        "₹725,000",
        "On Request",
        "On Request",
        "$3,000"
    ],
    "Website": [
        "https://www.we3group.com/bottle-making-machine.html",
        "https://dunamismachines.in/service/semi-automatic-pet-blow-moulding-machine-2/",
        "https://www.shyamplastic.com/products/versatile-machine/",
        "https://www.blowchennmachines.com/pet-jar-blowing-machine.html",
        "https://www.alibaba.com/showroom/semi-automatic-pet-blowing-machine.html"
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Streamlit app title
st.title("PET Jar Moulding Machine Dashboard")

# Display the DataFrame
st.dataframe(df, use_container_width=True)

# Instructions
st.write("Click on the website links to explore each machine in more detail.")
