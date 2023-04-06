#from extract_kpis_from_hcm import create_kpis as kpi_hcm
#from extract_kpis_from_purch import create_kpis as kpi_pur
#from extract_kpis_from_prod import create_kpis as kpi_prod

import pandas as pd
import numpy
from datetime import date, datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

all_kpis = {}


#company = "infineon"
#data_pur = pd.read_csv("./Mock_data/SAP_Purchasing.csv", sep=",")
#data_prod = pd.read_csv("./Mock_data/SAP_Production.csv", sep=",")
#data_hcm = pd.read_csv("./Mock_data/SAP_HCM.csv", sep=",")

#kpi_hcm = kpi_hcm(company, data_hcm)
#kpi_pur = kpi_pur(company, data_pur)
#kpi_prod = kpi_prod(company, data_prod)

#all_kpis["HCM"] = kpi_hcm
#all_kpis["PUR"] = kpi_pur
#all_kpis["PROD"] = kpi_prod

#df = pd.DataFrame.from_dict(all_kpis)
#print(df)
#df.to_excel("out.xlsx")



def find_risks_hcm(kpi_hcm):
    ########risks#########
    kpi_hcm = kpi_hcm
    risks = {}

    #demographic change:
    if kpi_hcm["avg_age"] >= 40:
        demogr_change_risk = "medium"
    if kpi_hcm["avg_age"] >= 50:
        demogr_change_risk = "high"
    else:
        demogr_change_risk = "low"

    demogr_change_age = kpi_hcm["avg_age"]

    risks["demogr_change_risk"]=demogr_change_risk
    risks["demogr_change_age"]=demogr_change_age


    #fluctuation_risk:
    if kpi_hcm["avg_time_in_company_months"] <= 36:
        fluctuation_risk = "medium"
    if kpi_hcm["avg_time_in_company_months"] <= 24:
        fluctuation_risk = "high"
    else:
        fluctuation_risk = "low"

    fluctuation_risk_months = kpi_hcm["avg_time_in_company_months"]

    risks["fluctuation_risk"]=fluctuation_risk
    risks["fluctuation_risk_months"]=fluctuation_risk_months

    print("x")
    return risks



def find_risks_pur(kpi_pur):
    kpi_pur = kpi_pur
    risks = {}
    #geo
    list_of_risky_countries = ["China", "Russia", "Ukraine"]

    risk_geo = 0
    risk_geo_locations = []
    for item in kpi_pur["top_countries"]:
        if item in list_of_risky_countries:
            risk_geo+=1
            risk_geo_locations.append(item)

    risks["risk_geo"]=risk_geo
    risks["risk_geo_locations"]=risk_geo_locations

    return risks


def find_risks_prod(kpi_prod):
    kpi_prod = kpi_prod
    risks = {}
    #geo
    list_of_risky_hazardous_material = ["Plastic", "Rubber"]

    risk_material = 0
    risk_materials = []
    for item in kpi_prod["top_materials"]:
        if item in list_of_risky_hazardous_material:
            risk_material+=1
            risk_materials.append(item)

    risks["risk_material"]=risk_material
    risks["risk_materials"]=risk_materials

    return risks