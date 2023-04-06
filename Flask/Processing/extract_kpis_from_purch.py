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
    top_materials = db.groupby('Materials')['Quantity'].sum().nlargest(20).to_dict()
    kpis["top_materials_pur"] = (top_materials)

    top_vendor_price = db.groupby('Vendor')['Price'].sum().nlargest(20).to_dict()
    kpis["top_vendor_byprice"] = (top_vendor_price)

    top_vendor_quant = db.groupby('Vendor')['Quantity'].sum().nlargest(20).to_dict()
    kpis["top_vendor_byquant"] = (top_vendor_quant)

    all_vendors = db['Vendor'].unique()
    kpis["all_vendors"] = (all_vendors)
                                  
    #process mine the most common SC: THIS WOULD WORK IN THEORY BUT CURRENTLY THE DATA IS SO UNIQUE THAT 1 wins.
    db = db.sort_values('Delivery_Date')
    db['Previous_Vendor'] = db['Vendor'].shift(1)

    most_occurring = db.groupby(['Previous_Vendor', 'Vendor']).size().nlargest(10).to_dict()
    kpis["most_occurring_SCs"] = (most_occurring)

    top_countries = db['Country'].value_counts().nlargest(20).to_dict()

    top_cities = db['City'].value_counts().nlargest(20).to_dict()
    #does not really make sense to only take top results, since we want to make sure the WHOLE supply chain works. But for now lets take tops.

    kpis["top_countries"] = (top_countries)
    kpis["top_cities"] = (top_cities)




    return kpis

#pp.pprint(create_kpis("company_x"))