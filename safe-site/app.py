from database.DAL.SiteSample import SiteSample
from virustotal_python import Virustotal
from config import api_key, site_risks
from base64 import urlsafe_b64encode
from database.DbUtils import DbUtils
from flask import Flask, request
import pandas as pd
import requests
import os


app = Flask(__name__)

@app.route('/ds1',methods = ['GET'])
def get_ds1():
    """
    Download the data source to the fs
    """
    url = "https://elementor-pub.s3.eu-central-1.amazonaws.com/Data-Enginner/Challenge1/request1.csv"    
    response = requests.get(url)
    with open(os.path.join("usr/sites", "sites.csv"), 'wb') as f:
        f.write(response.content)

@app.route('/check',methods = ['GET'])
def check_sites():
    """
    Writing the events to the DB
    """
    # Connect to the API
    vtotal = Virustotal(API_KEY=api_key, API_VERSION="v3")

    # Connect to the DB
    db = DbUtils()

    # Read the csv
    try:
        df = pd.read_csv(os.path.join("usr/sites", "sites.csv"), header=None)
    except Exception as e:
        print(e)

    # Iterate over the sites
    for _, site_url in df.iterrows():
        try:
            url = site_url[0]
            # URL safe encode URL in base64 format
            # https://developers.virustotal.com/v3.0/reference#url
            url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
            # Obtain the analysis results for the URL using the url_id
            analysis_resp = vtotal.request(f"urls/{url_id}")

            # Parse the categories
            categories_dict = dict()
            for x in analysis_resp.data['attributes']['categories'].values():
                if x not in categories_dict: 
                    categories_dict[x] = 0
                categories_dict[x] += 1

            # Parse the results
            results_dict = dict()
            for x in analysis_resp.data['attributes']['last_analysis_results'].values():
                if x['result'] not in results_dict: 
                    results_dict[x['result']] = 0
                results_dict[x['result']] += 1
            
            # Check if the site has risks
            is_risk = False
            for site_risk in site_risks:
                if site_risk in results_dict:
                    is_risk = True  
                    break
            
            # Insert to the DB
            site_sample = SiteSample(site=url,
                                    votes=str(results_dict),
                                    categories=str(categories_dict),
                                    is_risk=is_risk)

            db.session.add(site_sample)
            db.session.commit()
        except Exception as err:
            print(f"An error occurred: {err}\nCatching and continuing with program.")