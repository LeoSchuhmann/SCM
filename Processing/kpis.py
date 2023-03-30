from extract_kpis_from_hcm import create_kpis as kpi_hcm
from extract_kpis_from_purch import create_kpis as kpi_pur
from extract_kpis_from_prod import create_kpis as kpi_prod

import pandas as pd
import numpy
from datetime import date, datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

all_kpis = {}


company = "Infineon"
data_pur = pd.read_csv("Mock_data/SAP_Purchasing.csv", sep=",")
data_prod = pd.read_csv("Mock_data/SAP_Production.csv", sep=",")
data_hcm = pd.read_csv("./Mock_data/SAP_HCM.csv", sep=",")

kpi_hcm = kpi_hcm(company, data_hcm)
kpi_pur = kpi_pur(company, data_pur)
kpi_prod = kpi_prod(company, data_prod)



all_kpis["HCM"] = kpi_hcm
all_kpis["PUR"] = kpi_pur
all_kpis["PROD"] = kpi_prod
print("-----")
pp.pprint(all_kpis)
print("-----")