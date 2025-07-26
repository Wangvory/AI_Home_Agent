# 🏠 Mortgage Calculator Web App

A beautiful, interactive web application to calculate monthly mortgage payments including insurance and property tax estimates.

## Features

- **Interactive Inputs**: Easy-to-use sliders and input fields
- **Real-time Calculations**: See results update as you change values
- **Comprehensive Breakdown**: Monthly mortgage, insurance, and property tax
- **Flexible Options**: Choose between percentage-based or fixed amounts for insurance/tax
- **Professional UI**: Clean, modern interface with helpful tips

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

1. Start the web application:
```bash
streamlit run mortgage_calculator.py
```

2. Open your browser and go to the URL shown in the terminal (usually `http://localhost:8501`)

## How to Use

1. **Property Details** (Left Column):
   - Enter the home price
   - Set your down payment amount
   - Choose the interest rate
   - Select loan term (15, 20, or 30 years)

2. **Additional Costs** (Right Column):
   - Choose how to calculate insurance (percentage of home price or fixed amount)
   - Choose how to calculate property tax (percentage of home price or fixed amount)

3. **Results** (Bottom):
   - See your monthly mortgage payment
   - View estimated monthly insurance and property tax
   - Get the total monthly cost
   - Review helpful tips and summary

## Default Values

- Home Price: $500,000
- Down Payment: $100,000 (20%)
- Interest Rate: 6.5%
- Loan Term: 30 years
- Insurance: 0.5% of home price
- Property Tax: 1.0% of home price

## Tips

- A down payment of 20% or more typically avoids Private Mortgage Insurance (PMI)
- Property tax rates vary significantly by location
- Insurance costs depend on coverage level and property location
- Consider additional costs like HOA fees, utilities, and maintenance

---

*This calculator provides estimates only. Actual costs may vary based on your specific situation and location.*