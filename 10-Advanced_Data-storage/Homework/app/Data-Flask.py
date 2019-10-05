from matplotlib import style
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import datetime as dt 

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.Measurement
Station = Base.classes.Station

# Create our session (link) from Python to the DB
session = session.engine


#Flask set up
app = Flask(__name__)

@app.route("/")
def welcome(): 
    "List all available api routes"
    
  return f"Available Routes:<br/>"
   f"/api/v1.0/precipitation<br/>" 
   f"/api/v1.0/Station<br/>"
   f"/api/v1.0/tobs<br/>"
   f"/api/v1.0/<start>" 
   f"/api/v1.0/<start>/<end>"



@app.route("/api/v1.0/precipitation/<precipitation>")
def precipitation(precipitation):
    # Create our session (link) from Python to the DB
    last_12_months = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    prec_data = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= last_12_months).all()
    date_pr = {}
    for result in prec_data:
        date_pr[result[0]] = result[1]
    return jsonify(date_pr)
    
@app.route("/api/v1.0/Station/<Station>")
def Station(Station)
active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
            group_by(Measurement.station).\
                order_by(func.count(Measurement.station).desc()).all()
    return jsonify(active_stations)




