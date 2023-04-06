import pandas as pd
import numpy
from datetime import date, datetime
import pprint

#pp = pprint.PrettyPrinter(indent=4)

def create_kpis(db):
    today = date.today()
    # mm/dd/y
    today = today.strftime("%m/%d/%Y")
    db = db

    kpis = {}

    #ez_mean_kpis
    top_materials = db.groupby('Material')['Quantity'].sum().nlargest(20).to_dict()
    kpis["top_materials"] = (top_materials)

    all_materials = db['Material'].unique()
    kpis["all_materials"] = (all_materials)

    return kpis

#pp.pprint(create_kpis("company_x"))