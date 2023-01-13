import PySimpleGUI as sg
import pandas as pd
import numpy as np

import functions as fx


sg.theme("LightBlue5")


#you can fit as many objects into the list horrizontally as you want. Just make sure you wrap them in a list!

layout1=[

    [sg.Text("Purchasing Costs",font = ("Arial", 15), text_color="black")],

    #upfront costs
    [sg.Text("Purchase Price"), sg.InputText(default_text = 500000,key = "purchase_price_abb", size = (10,5)), sg.Text("Downpayment (%)"),
     sg.InputText(default_text = .2,key = "dp_perc_abb",size = (10,5)),sg.Text("Closing Costs (%)"), sg.InputText(default_text = .035,key = "closing_cost_abb",size = (10,5))],

    [sg.Text("Interest Rate (%)"), sg.InputText(default_text = .07,key = "interest_abb", size = (10,5)), sg.Text("Loan Term Length"), sg.InputText(default_text = 30,key = "term_abb", size = (10,5)),sg.Text("Refurbishing Cost"),
     sg.InputText(default_text = 0,key = "refurb_abb", size = (10,5))],
    
    [sg.HSeparator(pad=(1,10))],
    [sg.Text("Monthly Costs",font = ("Arial", 15), text_color="black")],

    #monthly costs
    [sg.Text("Annual Property Tax (%)"), sg.InputText(default_text = .005,key = "prop_tax_perc_abb", size = (10,5)),sg.Text("Capex Budget Allocation of Monthly Rents (%)"), sg.InputText(default_text =.05,key = "capex_abb", size = (10,5)),
    sg.Text("Repair Budget Allocation of Monthly Rents (%)"), sg.InputText(default_text =.05,key = "repair_abb", size = (10,5))],

    
    [sg.Text("Home Owners Association"), sg.InputText(default_text = 0,key = "hoa_abb", size = (10,5)),sg.Text("Home Owners Insurance"), sg.InputText(default_text = 200,key = "hoi_abb", size = (10,5)),
    sg.Text("Private Morgage Insurance (%)"), sg.InputText(default_text = 0,key = "pmi_abb", size = (10,5)),sg.Text("Property Management Fee (%)"), sg.InputText(default_text = .25,key = "prop_man_abb", size = (10,5))],

    [sg.Text("Utilities When Occupied"), sg.InputText(default_text =200,key = "util_occ_abb", size = (10,5)),sg.Text("Utilities When Vacant"), sg.InputText(default_text =100,key = "util_vac_abb", size = (10,5)), 
    sg.Text("AirBnB Fee (%)"), sg.InputText(default_text = .03,key = "abb_fee", size = (10,5))],


    [sg.HSeparator(pad=(1,10))],
    [sg.Text("Monthly Income",font = ("Arial", 15), text_color="black")],

    #income
    [sg.Text("Average Cost Per Night"), sg.InputText(default_text = 125,key = "rent_estimate_abb", size = (10,5)),sg.Text("Estimated Occupancy %"), sg.InputText(default_text = .65,key = "occupancy_abb", size = (10,5))],   

    [sg.HSeparator(pad=(1,10))],

    [sg.Button("Analyze Property", key='analyze_airbnb')],   
    
    [sg.HSeparator(pad=(1,10))],
    [sg.Text("Results",font = ("Arial", 15), text_color="black")],

    [sg.Multiline(size=(75, 12), key = "results_abb",enable_events=True)]
        
    ]


layout2=[
    [sg.Text("Purchasing Costs",font = ("Arial", 15), text_color="black")],

    [sg.Text("Purchase Price"), sg.InputText(default_text = 500000,key = "purchase_price_ltr", size = (10,5)),sg.Text("Downpayment (%)"), sg.InputText(default_text = .2,key = "dp_perc_ltr", size = (10,5)),
    sg.Text("Closing Costs (%)"), sg.InputText(default_text = .035,key = "closing_cost_ltr", size = (10,5))],
    [sg.Text("Interest Rate (%)"), sg.InputText(default_text = .07,key = "interest_ltr", size = (10,5)),sg.Text("Loan Term Length"), sg.InputText(default_text = 30,key = "term_ltr", size = (10,5)),
    sg.Text("Refurbishing Cost"), sg.InputText(default_text = 0,key = "refurb_ltr", size = (10,5))],
    
    [sg.HSeparator(pad=(1,10))],
    
    [sg.Text("Monthly Costs",font = ("Arial", 15), text_color="black")],

    [sg.Text("Anual Property Tax (%)"), sg.InputText(default_text = .005,key = "prop_tax_perc_ltr", size = (10,5)),sg.Text("Capex Budget Allocation of Monthly Rents (%)"), sg.InputText(default_text =.05,key = "capex_ltr", size = (10,5)),
    sg.Text("Repair Budget Allocation of Monthly Rents (%)"), sg.InputText(default_text =.05,key = "repair_ltr", size = (10,5))],
    [sg.Text("Utilities"), sg.InputText(default_text =0,key = "util_ltr", size = (10,5)),sg.Text("Home Owners Association"), sg.InputText(default_text = 0,key = "hoa_ltr", size = (10,5)),
    sg.Text("Home Owners Insurance"), sg.InputText(default_text = 200,key = "hoi_ltr", size = (10,5))],
    [sg.Text("Private Morgage Insurance (%)"), sg.InputText(default_text = 0,key = "pmi_ltr", size = (10,5)),sg.Text("Property Management Fee (%)"), sg.InputText(default_text = .10,key = "prop_man_ltr", size = (10,5))],
    
    [sg.HSeparator(pad=(1,10))],

    [sg.Text("Monthly Income",font = ("Arial", 15), text_color="black")],

    [sg.Text("Monthly Rent"), sg.InputText(default_text = 1500,key = "rent_estimate_ltr", size = (10,5)), sg.Text("Vacancy %"), sg.InputText(default_text = .04,key = "vacancy_ltr", size = (10,5))],   
    # [sg.Text("Vacancy %"), sg.InputText(default_text = .04,key = "vacancy_ltr")],   
    
    [sg.HSeparator(pad=(1,10))],
    
    [sg.Button("Analyze Property", key='analyze_ltr')],   
    
    [sg.HSeparator(pad=(1,10))],
    
    [sg.Text("Results",font = ("Arial", 15), text_color="black")],

    [sg.Multiline(size=(75, 12), key = "results_ltr",enable_events=True)]
        
    ]


tabgrp = [[sg.TabGroup([[
                    
                    sg.Tab('AirBnB Calculator', layout1, title_color='black',border_width =10,
                                 element_justification= 'center'),
                    
                    sg.Tab('Long Term Rental Calculator', layout2,title_color='Black',element_justification= 'center')]], 
                    
                    
                    tab_location='centertop',
                       title_color='Black', tab_background_color='Gray',selected_title_color='Black',
                       selected_background_color='Green', border_width=5), sg.Button('Close')]] 


window = sg.Window("Mountain Cat Lodging Calculator", tabgrp)

while True:
    event,values = window.read()

    if event == "analyze_airbnb":


        purchase_price = float(values["purchase_price_abb"])
        dp = float(values["dp_perc_abb"])
        closing_costs = float(values["closing_cost_abb"])
        interest = float(values["interest_abb"])
        term = int(values["term_abb"])
        refurb = float(values["refurb_abb"])
        prop_tax = float(values["prop_tax_perc_abb"])
        capex = float(values["capex_abb"])
        repair = float(values["repair_abb"])
        utilities_occupied = float(values["util_occ_abb"])
        utilities_vacant = float(values["util_vac_abb"])
        abb_fee= float(values["abb_fee"])
        hoa = float(values["hoa_abb"])
        hoi = float(values["hoi_abb"])
        pmi = float(values["pmi_abb"])
        prop_man = float(values["prop_man_abb"])
        rent_estimate = float(values["rent_estimate_abb"])
        occupancy = float(values["occupancy_abb"])
        
        result_text = fx.calculate_cashflow_abb_gui(dp,purchase_price,interest,term,refurb,hoi,prop_tax,rent_estimate,capex,repair,occupancy,utilities_occupied,utilities_vacant,abb_fee,closing_costs,prop_man,hoa,pmi)

        window["results_abb"].update(result_text)

    if event == "analyze_ltr":
        purchase_price = float(values["purchase_price_ltr"])
        dp = float(values["dp_perc_ltr"])
        closing_costs = float(values["closing_cost_ltr"])
        interest = float(values["interest_ltr"])
        term = int(values["term_ltr"])
        refurb = float(values["refurb_ltr"])
        prop_tax = float(values["prop_tax_perc_ltr"])
        capex = float(values["capex_ltr"])
        repair = float(values["repair_ltr"])
        vacancy = float(values["vacancy_ltr"])

        utilities_occupied = float(values["util_ltr"])
        hoa = float(values["hoa_ltr"])
        hoi = float(values["hoi_ltr"])
        pmi = float(values["pmi_ltr"])
        prop_man = float(values["prop_man_ltr"])
        
        rent_estimate = float(values["rent_estimate_ltr"])

        result_text = fx.calculate_cashflow_ltr_gui(dp,purchase_price,interest,term,refurb,hoi,prop_tax,rent_estimate,capex,repair,vacancy,utilities_occupied,closing_costs,prop_man,hoa,pmi)
        window["results_ltr"].update(result_text)

    if event == sg.WIN_CLOSED:
        break

    if event == "Close":
        break


window.close()





