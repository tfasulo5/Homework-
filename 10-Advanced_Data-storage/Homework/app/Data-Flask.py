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

@app.route("/api/v1.0/tobs/<tobs>")
def tobs(tobs)
station_numbers = active_stations[0][0]
    session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.station ==station_numbers).all()
    return jsonify(station_numbers)

highest_temp = session.query(Measurement.station, Measurement.tobs).\
                filter(Measurement.station == station_numbers).\
                filter(Measurement.date >= last_12_months).all()
high_df = pd.DataFrame(highest_temp)
high_df.set_index('station',)
high_df.head()
    return jsonify(high_df)

@app.route("/api/v1.0/start/<start>")
def start(start)
start_date (string): A date string in the format %Y-%m-%d
return jsonify(start)

@app.route("/api/v1.0/<start>/<end>/<start>/<end>")
def <start>/<end>(<start>/<end>)
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

trip_temps = calc_temps('2017-02-28', '2017-03-05')
trip_temps

if __name__ == "__main__":
    app.run(debug=True)




