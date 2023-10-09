import streamlit as st
import pandas as pd

company_data = {
    'Company Name': ['Newt Global'],
    'About Us': ['We are the leading expert in cloud migration. our deep expertise lie there. We provide transformative services to clients in evoving marketplace.  We are dedicated to delivering innovative technology solutions that empower businesses to thrive in todays fast-paced digital landscape.'],
    'Contact Email': ['ngproject@company.com'],
    'Phone Number': ['123-456-1230'],
}
df = pd.DataFrame(company_data)

def main():
    st.title('Newt Global')

    page = st.sidebar.radio('Navigation', ['Home', 'About Us', 'Contact Us'])

    if page == 'Home':
        st.header('Home')
        st.write("Welcome to our website. We provide excellent IT consulting and services to businesses.")

    elif page == 'About Us':
        st.header('About Us')
        about_text = df['About Us'].values[0]
        st.write(about_text)

    elif page == 'Contact Us':
        st.header('Contact Us')
        contact_info = df[['Contact Email', 'Phone Number']].iloc[0]
        st.write(f'Email: {contact_info["Contact Email"]}')
        st.write(f'Phone: {contact_info["Phone Number"]}')

if __name__ == '__main__':
    main()
