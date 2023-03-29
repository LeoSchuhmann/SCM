import pandas as pd
import numpy
from datetime import date, datetime
import pprint

pp = pprint.PrettyPrinter(indent=4)

def create_kpis(company):
    today = date.today()
    # mm/dd/y
    today = today.strftime("%m/%d/%Y")
    db = pd.read_csv("./Mock_data/SAP_Production.csv", sep=",")
    company = company
    kpis = {}

    #ez_mean_kpis
    top_materials = db.groupby('Material')['Quantity'].sum().nlargest(20).to_dict()
    kpis["top_materials"] = (top_materials)

    return kpis

pp.pprint(create_kpis("company_x"))