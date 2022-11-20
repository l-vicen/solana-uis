import streamlit as st
import loaner
import customer
import merchant
import home

# Page configurations in App
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto"
)

# Router to control paging
class Router:

    def display_router(self):
        """ Sidebar Navbar """
        # Sidebar attributes
        home.Sidebar.sidebar_functionality(self)
        self.features = ['Home','Customer', 'Merchant', 'Loaner']
        self.page = st.sidebar.selectbox('Choose the option', self.features)
        st.sidebar.markdown('---')

    def route(self):
        """ Router Functionality """
         # Credit worthness test
        if self.page == self.features[0]:
            home.display_home()
        
        # Get your credit score
        elif self.page == self.features[1]:
            customer.display_customer_dashboard()

        # Get your credit score
        elif self.page == self.features[2]:
            merchant.display_merchant_dashboard()

        # Merchant statistics
        elif self.page == self.features[3]:
            loaner.display_loaner_dashboard()

            
# Initiating class
route = Router()

# Displaying home structure
#home.sidebar.sidebar_functionality()
route.display_router()
route.route()

#loaner.sidebar.sidebar_inform_libs()
home.sidebar.sidebar_contact()