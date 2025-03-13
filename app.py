import streamlit as st
import pandas as pd
import plotly.express as px

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
        435000,
        725000,
        None,
        None,
        3000
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

# Sidebar filters
st.sidebar.header("Filters")
selected_manufacturer = st.sidebar.selectbox("Select Manufacturer", ["All"] + list(df["Manufacturer"].unique()))
price_range = st.sidebar.slider("Select Price Range (INR/USD)", min_value=3000, max_value=725000, value=(3000, 725000))

# Filter data
filtered_df = df.copy()
if selected_manufacturer != "All":
    filtered_df = filtered_df[filtered_df["Manufacturer"] == selected_manufacturer]
filtered_df = filtered_df[(filtered_df["Price (INR/USD)"].fillna(0) >= price_range[0]) & 
                          (filtered_df["Price (INR/USD)"].fillna(0) <= price_range[1])]

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Price Comparison", "Machine Specifications", "Best Value Options"])

with tab1:
    st.subheader("Price Comparison by Manufacturer")
    fig = px.bar(filtered_df, x="Manufacturer", y="Price (INR/USD)", title="Price Comparison", text="Price (INR/USD)")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Machine Specifications")
    st.dataframe(filtered_df, use_container_width=True)

with tab3:
    st.subheader("Best Value Machines")
    best_value_df = filtered_df.sort_values(by="Price (INR/USD)", ascending=True).head(3)
    st.dataframe(best_value_df, use_container_width=True)

# Footer message
st.write("Click on the website links in the table to explore each machine in more detail.")

