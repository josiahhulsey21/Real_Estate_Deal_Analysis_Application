from mortgage import Loan

def calculate_cashflow_abb_gui(dp_perc, sale_price, interest, term, refurb_cost, home_owners_insurance, property_tax_perc, cost_per_night, capex, repair_budget, occupancy, utility = 200, utility_vacant = 100, airbnb_fee=.03,closing_cost_perc =.035, prop_manage_perc=0.25, hoa=0, pmi_perc= 0.0):
    '''
    Function to calculate cashflow of a property. All none-percentage values are expected to be monthly.
    '''

    dp = sale_price * dp_perc
    closing_cost = closing_cost_perc * (sale_price-dp)

    loan_total = sale_price - (sale_price * dp_perc)

    if pmi_perc > 0.0:
        pmi_payment  = (loan_total * pmi_perc)/12
    else:
        pmi_payment = 0.0

    rent_estimate = int((occupancy*30)) * cost_per_night

    #loan object calculation from the mortgage library
    loan = Loan(principal = sale_price - dp, interest = interest, term=term)

    propm = prop_manage_perc*rent_estimate

    property_tax = (property_tax_perc * sale_price)/12

    #calculation of monthly payment
    mp = round(float(loan.monthly_payment) + pmi_payment + property_tax + hoa + propm + (repair_budget*rent_estimate) + (capex*rent_estimate) + home_owners_insurance  + utility, 2)

    #calculates cashflow
    cash_flow = rent_estimate - mp - (rent_estimate*airbnb_fee)


    ccr = (cash_flow*12)/(refurb_cost+dp+closing_cost)


    return_text = f'''
    The downpament for the property is $ {dp}
    The closing costs for this property is estimated at $ {round(closing_cost,2)}
    The total cost to buy this property is around $ {closing_cost + dp}

    The monthly payment is $ {mp}
    The nonvariant costs are $ {round(float(loan.monthly_payment)+home_owners_insurance+property_tax+utility_vacant,2)}
    
    The projected cashflow is $ {round(cash_flow,2)}
    The cash on cash return is {round(ccr,2)} %

    '''


    return return_text



def calculate_cashflow_ltr_gui(dp_perc, sale_price, interest, term, refurb_cost, home_owners_insurance, property_tax_perc, rent_estimate, capex, repair_budget, vacancy_rate, utilities, closing_cost_perc =.035, prop_manage_perc=0.1, hoa=0, pmi_perc= 0.0):
    '''
    Function to calculate cashflow of a property. All none-percentage values are expected to be monthly.
    '''

    dp = sale_price * dp_perc
    closing_cost = closing_cost_perc * (sale_price-dp)

    loan_total = sale_price - (sale_price * dp_perc)

    if pmi_perc > 0.0:
        pmi_payment  = (loan_total * pmi_perc)/12
    else:
        pmi_payment = 0.0
       

    #loan object calculation from the mortgage library
    loan = Loan(principal = sale_price - dp, interest = interest, term=term)

    propm = prop_manage_perc*rent_estimate

    property_tax = (property_tax_perc * sale_price)/12
    vacancy = (vacancy_rate*(rent_estimate*12))/12

    #calculation of monthly payment
    mp = round(float(loan.monthly_payment) + pmi_payment + property_tax + hoa + propm + (repair_budget*rent_estimate) + (capex*rent_estimate) + home_owners_insurance + vacancy + utilities, 2)
    
    #calculates cashflow
    cash_flow = rent_estimate - mp

    #calculates the roi
    ccr = round((cash_flow * 12)/(closing_cost + refurb_cost + dp),2)

    return_text = f'''
    The downpament for the property is $ {dp}
    The closing costs for this property is estimated at $ {round(closing_cost,2)}
    The total cost to buy this property is around $ {closing_cost + dp}

    The monthly payment is $ {mp}
    The nonvariant costs are $ {round(float(loan.monthly_payment)+home_owners_insurance+property_tax,2)}
    
    The projected cashflow is $ {round(cash_flow,2)}
    The cash on cash return is {round(ccr,2)} %

    '''

    return return_text