from extract_kpis_from_hcm import create_kpis as kpi_hcm
from extract_kpis_from_purch import create_kpis as kpi_pur
from extract_kpis_from_prod import create_kpis as kpi_prod

import pandas as pd
import numpy
from datetime import date, datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

all_kpis = {}

kpi_hcm = kpi_hcm("company_x")
kpi_pur = kpi_pur("company_x")
kpi_prod = kpi_prod("company_x")



all_kpis["HCM"] = kpi_hcm
all_kpis["PUR"] = kpi_pur
all_kpis["PROD"] = kpi_prod
print("-----")
pp.pprint(all_kpis)
print("-----")