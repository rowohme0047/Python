import streamlit as rs
import pandas as pd

company_data = {
    'Company Name': ['Newt Global'],
    'About Us': ['We are the leading expert in cloud migration. our deep expertise lie there. We provide transformative services to clients in evoving marketplace.  We are dedicated to delivering innovative technology solutions that empower businesses to thrive in todays fast-paced digital landscape.'],
    'Contact Email': ['ngproject@company.com'],
    'Phone Number': ['123-456-1230'],
}
df = pd.DataFrame(company_data)

def main():
    rs.title('Newt Global')

    page = rs.sidebar.radio('Navigation', ['Home', 'About Us', 'Contact Us'])

    if page == 'Home':
        rs.header('Home')
        rs.write("Welcome to our website. We provide excellent IT consulting and services to businesses.")

    elif page == 'About Us':
        rs.header('About Us')
        about_text = df['About Us'].values[0]
        rs.write(about_text)

    elif page == 'Contact Us':
        rs.header('Contact Us')
        contact_info = df[['Contact Email', 'Phone Number']].iloc[0]
        rs.write(f'Email: {contact_info["Contact Email"]}')
        rs.write(f'Phone: {contact_info["Phone Number"]}')

if __name__ == '__main__':
    main()
