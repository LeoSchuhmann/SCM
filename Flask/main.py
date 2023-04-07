# Importing required functions
import pandas
from flask import Flask, render_template, request, redirect, url_for
from fileinput import filename

from Processing.extract_kpis_from_hcm import create_kpis as create_kpis_hcm
from Processing.extract_kpis_from_purch import create_kpis as create_kpis_pur
from Processing.extract_kpis_from_prod import create_kpis as create_kpis_prod
from Processing.risks import find_risks_hcm, find_risks_pur, find_risks_prod

# Flask constructor
app = Flask(__name__)

@app.get('/')
def home():
	return render_template('main.html')
# Root endpoint
@app.get('/upload')
def upload():
	return render_template('upload-excel.html')


@app.post('/view')
def view():
	# Read the File using Flask request
	# file = request.files
	files = request.files.getlist("file")
	company_name = request.form['company']
	print(company_name)
	for file in files:
		file.save("Flask/data/" + file.filename)
	# save file in local directory
	# file.save("Flask/data/" + file.filename)
	
	data = pandas.read_csv("Flask/data/SAP_HCM.csv")
	kpi_hcm = create_kpis_hcm(data)
	print(kpi_hcm)
	risks_hcm = find_risks_hcm(kpi_hcm)
	print(risks_hcm)
	hcm_risks_db = pandas.DataFrame.from_dict(risks_hcm, orient='index')
	hcm_risks_db.to_excel("Flask/risks/HCM_risks.xlsx")

	# Return HTML snippet that will render the table
	# find_risks()
	#return render_template('success.html')


	data = pandas.read_csv("Flask/data/SAP_Purchasing.csv")

	## change
	kpi_pur = create_kpis_pur(data)
	print(kpi_pur)
	risks_pur = find_risks_pur(kpi_pur)
	print(risks_pur)
	pur_risks_db = pandas.DataFrame.from_dict(risks_pur, orient='index')
	pur_risks_db.to_excel("Flask/risks/PUR_risks.xlsx")

	# Return HTML snippet that will render the table
	# find_risks()

	data = pandas.read_csv("Flask/data/SAP_Production.csv")

	## change
	kpi_prod = create_kpis_prod(data)
	print(kpi_prod)
	kpi_prod = find_risks_prod(kpi_prod)
	print(kpi_prod)
	prod_risks_db = pandas.DataFrame.from_dict(kpi_prod, orient='index')
	prod_risks_db.to_excel("Flask/risks/PROD_risks.xlsx")

	# Return HTML snippet that will render the table
	# find_risks()
	return redirect(url_for('risks'))
# render_template('show_tables.html',  tables=[hcm_risks_db.to_html(classes='data'), data.to_html(classes='data')])

@app.get('/risks')
def risks():
	hcm=pandas.read_excel("Flask/risks/HCM_risks.xlsx").rename(columns={"Unnamed: 0": "risk", 0:"value"})
	pur=pandas.read_excel("Flask/risks/PUR_risks.xlsx").rename(columns={"Unnamed: 0": "risk", 0:"value"})
	prod=pandas.read_excel("Flask/risks/PROD_risks.xlsx").rename(columns={"Unnamed: 0": "risk", 0:"value"})

	df2 = pandas.concat([hcm, pur], axis=0)
	df3 = pandas.concat([df2, prod], axis=0).reset_index().drop('index', axis=1)


	return render_template('show_tables.html',  tables=[df3.to_html(classes='data')])


# Main Driver Function
if __name__ == '__main__':
	# Run the application on the local development server
	app.run(debug=True)
