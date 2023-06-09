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
    # company = company
    kpis = {}

    #ez_mean_kpis
    avg_wage = db["Wage per year in euro"].mean()
    min_wage = db["Wage per year in euro"].min()
    avg_sick_days = db["days sick"].mean()
    avg_age = db["age"].mean()
    avg_training_hours = db["training hours"].mean()
    avg_headcounts_in_upper_mgmt = db["upper management"].mean()

    kpis["avg_wage"] = (avg_wage)
    kpis["min_wage"] = (min_wage)
    kpis["avg_sick_days"] = (avg_sick_days)
    kpis["avg_age"] = (avg_age)
    kpis["avg_training_hours"] = (avg_training_hours)
    kpis["avg_headcounts_in_upper_mgmt"] = (avg_headcounts_in_upper_mgmt)

    #ez_gender_stuff
    distinct_genders = len(db["gender"].unique())
    kpis["distinct_genders"] = (distinct_genders)
    gender_count = db.groupby('gender').size()
    gender_ratio = gender_count / len(db)
    kpis["ratio_genders"] = (gender_ratio.to_dict())

    #time_in_company
    time_in_company = []
    start_dates = db["start date"].tolist()
    def diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month
    for start_date in start_dates:
        time_in_c = diff_month(datetime(int(today[6:10]),int(today[:2]),int(today[3:5])), datetime(int(start_date[6:10]),int(start_date[:2]),int(start_date[3:5])))
        time_in_company.append(time_in_c)
    db["time_in_company"] = time_in_company
    db["time_in_company"].mean()
    kpis["avg_time_in_company_months"] = db["time_in_company"].mean()

    #gender in upper management ATTENTION I THINK THIS JUST TAKES THE RATIO IN THE GENDER ITSELF NOT THE GENERAL FEMALES IN UPPER MGMT PER FULL
    gender_ratio = db.groupby('gender')['upper management'].mean().to_dict()
    kpis["gender_in_upper_mangement"] = gender_ratio

    #gender iwage ATTENTION THIS JUST TAKES THE RATIO IN THE GENDER ITSELF NOT THE GENERAL FEMALES IN UPPER MGMT PER FULL
    gender_ratio_wage = db.groupby('gender')['Wage per year in euro'].mean().to_dict()
    kpis["gender_ratio_wage"] = gender_ratio_wage

    return kpis

#pp.pprint(create_kpis("company_x"))