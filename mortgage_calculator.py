import streamlit as st
import math

def calculate_mortgage(loan_amount, interest_rate, loan_term_years):
    """Calculate monthly mortgage payment using the standard amortization formula."""
    n_payments = loan_term_years * 12
    monthly_rate = interest_rate / 100 / 12
    
    if monthly_rate > 0:
        mortgage_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** n_payments) / ((1 + monthly_rate) ** n_payments - 1)
    else:
        mortgage_payment = loan_amount / n_payments
    
    return mortgage_payment

def main():
    st.set_page_config(
        page_title="Mortgage Calculator",
        page_icon="🏠",
        layout="wide"
    )
    
    st.title("🏠 Mortgage Calculator")
    st.markdown("Calculate your monthly mortgage payment, including estimated insurance and property tax.")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Property Details")
        
        # Property inputs
        home_price = st.number_input(
            "Home Price ($)",
            min_value=0.0,
            value=1500000.0,
            step=10000.0,
            format="%.0f"
        )
        
        down_payment = st.number_input(
            "Down Payment ($)",
            min_value=0.0,
            max_value=home_price,
            value=600000.0,
            step=10000.0,
            format="%.0f"
        )
        
        # Auto-calculate loan amount
        loan_amount = home_price - down_payment
        st.metric("Loan Amount", f"${loan_amount:,.0f}")
        
        # Loan terms
        interest_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            max_value=20.0,
            value=6.5,
            step=0.01,
            format="%.2f"
        )
        
        loan_term_years = st.selectbox(
            "Loan Term",
            options=[15, 20, 30],
            index=2
        )
    
    with col2:
        st.subheader("💰 Additional Costs")
        
        # Insurance options
        insurance_option = st.radio(
            "Insurance Calculation",
            ["Use percentage of home price", "Enter annual amount"]
        )
        
        if insurance_option == "Use percentage of home price":
            insurance_percentage = st.slider(
                "Insurance (% of home price)",
                min_value=0.1,
                max_value=2.0,
                value=0.5,
                step=0.01
            )
            insurance_annual = home_price * (insurance_percentage / 100)
        else:
            insurance_annual = st.number_input(
                "Annual Insurance ($)",
                min_value=0.0,
                value=2500.0,
                step=100.0,
                format="%.0f"
            )
        
        # Property tax options
        tax_option = st.radio(
            "Property Tax Calculation",
            ["Use percentage of home price", "Enter annual amount"]
        )
        
        if tax_option == "Use percentage of home price":
            tax_percentage = st.slider(
                "Property Tax (% of home price)",
                min_value=0.1,
                max_value=3.0,
                value=1.25,
                step=0.01
            )
            tax_annual = home_price * (tax_percentage / 100)
        else:
            tax_annual = st.number_input(
                "Annual Property Tax ($)",
                min_value=0.0,
                value=5000.0,
                step=100.0,
                format="%.0f"
            )
    
    # Calculate results
    mortgage_payment = calculate_mortgage(loan_amount, interest_rate, loan_term_years)
    insurance_monthly = insurance_annual / 12
    tax_monthly = tax_annual / 12
    total_monthly = mortgage_payment + insurance_monthly + tax_monthly
    
    # Display results
    st.markdown("---")
    st.subheader("📈 Monthly Payment Breakdown")
    
    # Create three columns for results
    result_col1, result_col2, result_col3, result_col4 = st.columns(4)
    
    with result_col1:
        st.metric(
            "Mortgage Payment",
            f"${mortgage_payment:,.0f}",
            help="Principal + Interest"
        )
    
    with result_col2:
        st.metric(
            "Insurance",
            f"${insurance_monthly:,.0f}",
            help=f"Monthly (${insurance_annual:,.0f}/year)"
        )
    
    with result_col3:
        st.metric(
            "Property Tax",
            f"${tax_monthly:,.0f}",
            help=f"Monthly (${tax_annual:,.0f}/year)"
        )
    
    with result_col4:
        st.metric(
            "Total Monthly",
            f"${total_monthly:,.0f}",
            help="All costs combined"
        )
    
    # Additional information
    st.markdown("---")
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.subheader("📋 Summary")
        st.write(f"**Home Price:** ${home_price:,.0f}")
        st.write(f"**Down Payment:** ${down_payment:,.0f} ({(down_payment/home_price)*100:.1f}%)")
        st.write(f"**Loan Amount:** ${loan_amount:,.0f}")
        st.write(f"**Interest Rate:** {interest_rate}%")
        st.write(f"**Loan Term:** {loan_term_years} years")
    
    with col_info2:
        st.subheader("💡 Tips")
        st.write("• Down payment of 20% or more avoids PMI")
        st.write("• Property tax rates vary by location")
        st.write("• Insurance costs depend on coverage and location")
        st.write("• Consider additional costs like HOA fees")
    
    # Footer
    st.markdown("---")
    st.markdown("*This calculator provides estimates only. Actual costs may vary based on your specific situation and location.*")

if __name__ == "__main__":
    main() 