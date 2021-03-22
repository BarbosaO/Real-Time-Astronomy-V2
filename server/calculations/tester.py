from calculations.calculator import calculateData, calculateJupiterPert, calculateSaturnPert, calculateUranusPert, calculateSunData, calculateGeocentric
from calculations import planets
from flask import jsonify
import datetime, time
import threading
import math
import json

def serializeDistances(mercury_dist, venus_dist, mars_dist, jupiter_dist, saturn_dist, uranus_dist, neptune_dist):
    return {
        'mercury_heliocentric_distance' : mercury_dist,
        'venus_heliocentric_distance'  : venus_dist,
        'mars_heliocentric_distance': mars_dist,
        'jupiter_heliocentric_distance' : jupiter_dist,
        'saturn_heliocentric_distance': saturn_dist,
        'uranus_heliocentric_distance' : uranus_dist,
        'neptune_heliocentric_distance' :  neptune_dist,
    }

class PlanetResponse:
    def __init__(self, planet_name, helio_distance, helio_x_coor, helio_y_coor, helio_z_coor, geo_distance, geo_x_coor, geo_y_coor, geo_z_coor):
        self.planet_name = planet_name
        self.helio_distance = helio_distance
        self.helio_x_coor = helio_x_coor
        self.helio_y_coor = helio_y_coor
        self.helio_z_coor = helio_z_coor
        self.geo_distance = geo_distance
        self.geo_x_coor = geo_x_coor
        self.geo_y_coor = geo_y_coor
        self.geo_z_coor = geo_z_coor
    
    def serialize(self):
        return {
            'planet_name' : self.planet_name,
            'heliocentric_distance' : self.helio_distance,
            'heliocentric_x_coordinate' : self.helio_x_coor,
            'heliocentric_y_coordinate' : self.helio_y_coor,
            'heliocentric_z_coordinate' : self.helio_z_coor,
            'geocentric_distance' : self.geo_distance,
            'geocentric_x_coordinate' : self.geo_x_coor,
            'geocentric_y_coordinate' : self.geo_y_coor,
            'geocentric_z_coordinate' : self.geo_z_coor
        }

def serializeObj(obj):
    if isinstance(obj, PlanetResponse):
        return {
            'planet_name' : obj.planet_name,
            'heliocentric_distance' : obj.helio_distance,
            'heliocentric_x_coordinate' : obj.helio_x_coor,
            'heliocentric_y_coordinate' : obj.helio_y_coor,
            'heliocentric_z_coordinate' : obj.helio_z_coor,
            'geocentric_distance' : obj.geo_distance,
            'geocentric_x_coordinate' : obj.geo_x_coor,
            'geocentric_y_coordinate' : obj.geo_y_coor,
            'geocentric_z_coordinate' : obj.geo_z_coor
        }
    else:
        return TypeError('Type could not be serialized') 

def jsonifyDataResponse(mercury, venus, mars, jupiter, saturn, uranus, neptune):
    response = [mercury, venus, mars, jupiter, saturn, uranus, neptune]
    return jsonify(res = [planet.serialize() for planet in response])

def jsonDataResponse(mercury, venus, mars, jupiter, saturn, uranus, neptune):
    response = {
        'mercury' : mercury,
        'venus' : venus,
        'mars' : mars,
        'jupiter' : jupiter,
        'saturn' : saturn,
        'uranus' : uranus,
        'neptune' : neptune 
    }

    return json.dumps(response, default=serializeObj)


def rev(angle):
    """ Reduce an angle to within 0 to +360 degrees """
    while(angle <= 0 or angle >= 360):
        if(angle < 0):
            angle += 360
        else:
            angle -= 360
    return angle

def calc():
    """ Calculates initial date """
    # calculating UT and d
    currentDT = datetime.datetime.now()
    UT = currentDT.hour + (currentDT.minute / 60.0) + (currentDT.second / 3600)
    year = currentDT.year
    month = currentDT.month
    day = currentDT.day

    # get day zero of J2000 cut off. Assume that it was on December 31, 1999 at 17:00 hours
    d_0 = 367 * 1999 - (7 * (1999 + ((12 + 9) / 12))) / 4 - (3 * ((1999 + (12 - 9) / 7) / 100 + 1)) / 4 + (275 * 12) / 9 + 29.50 - 730515

    #d = 367 * year - (7 * (year + ((month + 9) / 12))) / 4 - (3 * ((year + (month - 9) / 7) / 100 + 1)) / 4 + (275 * month) / 9 + day - 730515
    d = 367 * year - (7 * (year + ((month + 9) / 12))) / 4  + (275 * month) / 9 + day - 730530
    
    # add cut off to compensate for the assumed start of J2000. This will give more accurate readings.
    d += UT/24 + (-1 * d_0) / 10

    currentTimeMills = int(round(time.time()) * 1000)
    millsSince2000 = datetime.datetime(2000, 1, 1).timestamp() * 1000
    millsSince2000 =  946684800000

    d= round((1.0 + (currentTimeMills - millsSince2000) / (3600 * 24.0 * 1000)), 5)
    #d = -3543.0
    #d = 7306.20833
    
    # sun calculations
    new_sun = planets.Sun()

    N_sun = new_sun.N
    i_sun = new_sun.i
    w_sun = rev(new_sun.w + new_sun.w_ * d)
    a_sun = new_sun.a
    e_sun = new_sun.e - new_sun.e_ * d
    M_sun = rev(new_sun.M + new_sun.M_ * d)

    sun_values = calculateSunData(N_sun, i_sun, w_sun, a_sun, e_sun, M_sun)

    #print(M_sun)

    # mercury calculations
    new_mercury = planets.Mercury()

    N_mercury = rev(new_mercury.N + new_mercury.N_ * d)
    i_mercury = new_mercury.i + new_mercury.i_ * d
    w_mercury = rev(new_mercury.w + new_mercury.w_ * d)
    a_mercury = new_mercury.a
    e_mercury = new_mercury.e + new_mercury.e_ * d
    M_mercury = rev(new_mercury.M + new_mercury.M_ * d)

    mercury_values = calculateData(N_mercury, i_mercury, w_mercury, a_mercury, e_mercury, M_mercury)

    # calculate geocentric coordinates
    mercury_geocentric = calculateGeocentric(sun_values[0], sun_values[1], mercury_values[0], mercury_values[1], mercury_values[2])

    # venus calculations
    new_venus = planets.Venus()

    N_venus = rev(new_venus.N + new_venus.N_ * d)
    i_venus = new_venus.i + new_venus.i_ * d
    w_venus = rev(new_venus.w + new_venus.w_ * d)
    a_venus = new_venus.a
    e_venus = new_venus.e - new_venus.e_ * d
    M_venus = rev(new_venus.M + new_venus.M_ * d)

    venus_values = calculateData(N_venus, i_venus, w_venus, a_venus, e_venus, M_venus)

    # calculate geocentric coordinates
    venus_geocentric = calculateGeocentric(sun_values[0], sun_values[1], venus_values[0], venus_values[1], venus_values[2])

    # mars calculations
    new_Mars = planets.Mars()

    N_mars = new_Mars.N + new_Mars.N_ * d
    i_mars = new_Mars.i - new_Mars.i_ * d
    w_mars = new_Mars.w + new_Mars.w_ * d
    a_mars = new_Mars.a
    e_mars = new_Mars.e + new_Mars.e_ * d
    M_mars = new_Mars.M + new_Mars.M_ * d

    mars_values = calculateData(N_mars, i_mars, w_mars, a_mars, e_mars, M_mars)

     # calculate geocentric coordinates
    mars_geocentric = calculateGeocentric(sun_values[0], sun_values[1], mars_values[0], mars_values[1], mars_values[2])

    # saturn calculations
    new_Saturn = planets.Saturn()

    N_saturn = rev(new_Saturn.N + new_Saturn.N_ * d)
    i_saturn = new_Saturn.i - new_Saturn.i_ * d
    w_saturn = rev(new_Saturn.w + new_Saturn.w_ * d)
    a_saturn = new_Saturn.a
    e_saturn = new_Saturn.e - new_Saturn.e_ * d
    M_saturn = rev(new_Saturn.M + new_Saturn.M_ * d)
        
    saturn_values = calculateData(N_saturn, i_saturn, w_saturn, a_saturn, e_saturn, M_saturn)

    # jupiter calculations
    new_Jupiter = planets.Jupiter()

    N_jupiter = rev(new_Jupiter.N + new_Jupiter.N_ * d)
    i_jupiter = new_Jupiter.i - new_Jupiter.i_ * d
    w_jupiter = rev(new_Jupiter.w + new_Jupiter.w_ * d)
    a_jupiter = new_Jupiter.a
    e_jupiter = new_Jupiter.e + new_Jupiter.e_ * d
    M_jupiter = rev(new_Jupiter.M + new_Jupiter.M_ * d)

    jupiter_values = calculateData(N_jupiter, i_jupiter, w_jupiter, a_jupiter, e_jupiter, M_jupiter)
    
    # perform perturbations calculations for Jupiter
    correctedJupiter = calculateJupiterPert(M_jupiter, M_saturn, jupiter_values[4], jupiter_values[5], jupiter_values[6])

    # calculate geocentric coordinates for Jupiter
    jupiter_geocentric = calculateGeocentric(sun_values[0], saturn_values[1], correctedJupiter[1], correctedJupiter[2], correctedJupiter[3])

    # perform perturbations calculations for Saturn
    correctedSaturn = calculateSaturnPert(M_jupiter, M_saturn, saturn_values[4], saturn_values[5], saturn_values[6])

    # calculate geocentric coordinates for Saturn
    saturn_geocentric = calculateGeocentric(sun_values[0], sun_values[1], correctedSaturn[1], correctedSaturn[2], correctedSaturn[3])

    # uranus calculations
    new_Uranus = planets.Uranus()

    N_uranus = rev(new_Uranus.N + new_Uranus.N_ * d)
    i_uranus = new_Uranus.i + new_Uranus.i_ * d
    w_uranus = rev(new_Uranus.w + new_Uranus.w_ * d)
    a_uranus = new_Uranus.a - new_Uranus.a_ * d
    e_uranus = new_Uranus.e + new_Uranus.e_ * d
    M_uranus = rev(new_Uranus.M + new_Uranus.M_ * d)

    uranus_values = calculateData(N_uranus, i_uranus, w_uranus, a_uranus, e_uranus, M_uranus)

    # perform perturbations calculations for Uranus
    correctedUranus = calculateUranusPert(M_jupiter, M_saturn, M_uranus, uranus_values[4], uranus_values[5], uranus_values[6])

    # calculate geocentric coordinates for Uranus

    uranus_geocentric = calculateGeocentric(sun_values[0], sun_values[1], correctedUranus[1], correctedUranus[2], correctedUranus[3])

    # neptune calculations
    new_Neptune = planets.Neptune()

    N_neptune = rev(new_Neptune.N + new_Neptune.N_ * d)
    i_neptune = new_Neptune.i - new_Neptune.i_ * d
    w_neptune = rev(new_Neptune.w - new_Neptune.w_ * d)
    a_neptune = new_Neptune.a + new_Neptune.a_ * d
    e_neptune = new_Neptune.e + new_Neptune.e_ * d
    M_neptune = rev(new_Neptune.M + new_Neptune.M_ * d)

    neptune_values = calculateData(N_neptune, i_neptune, w_neptune, a_neptune, e_neptune, M_neptune)

    # calculate geocentric coordinates for Neptune
    neptune_geocentric = calculateGeocentric(sun_values[0], sun_values[1], neptune_values[0], neptune_values[1], neptune_values[2])

    # all_data
    
    # mercury
    mercury_data = PlanetResponse('Mercury', round(mercury_values[3]), round(mercury_values[0], 6), round(mercury_values[1], 6), round(mercury_values[2], 6),
                                mercury_geocentric[0], mercury_geocentric[1], mercury_geocentric[2], mercury_geocentric[3])

    # venus 
    venus_data = PlanetResponse('Venus', round(venus_values[3]), round(venus_values[0], 6), round(venus_values[1], 6), round(venus_values[2], 6),
                                venus_geocentric[0], venus_geocentric[1], venus_geocentric[2], venus_geocentric[3])

    # mars
    mars_data = PlanetResponse('Mars', round(mars_values[3]), round(mars_values[0], 6), round(mars_values[1], 6), round(mars_values[2], 6),
                                mars_geocentric[0], mars_geocentric[1], mars_geocentric[2], mars_geocentric[3])
    
    # jupiter
    jupiter_data = PlanetResponse('Jupiter', round(correctedJupiter[0]), round(jupiter_values[0], 6), round(jupiter_values[1], 6), round(jupiter_values[2], 6),
                                jupiter_geocentric[0], jupiter_geocentric[1], jupiter_geocentric[2], jupiter_geocentric[3])

    # saturn
    saturn_data = PlanetResponse('Saturn', round(correctedSaturn[0]), round(saturn_values[0], 6), round(saturn_values[1], 6), round(saturn_values[2], 6),
                                saturn_geocentric[0], saturn_geocentric[1], saturn_geocentric[2], saturn_geocentric[3])

    # unranus
    uranus_data = PlanetResponse('Uranus', round(correctedUranus[0]), round(uranus_values[0], 6), round(uranus_values[1], 6), round(uranus_values[2], 6),
                                uranus_geocentric[0], uranus_geocentric[1], uranus_geocentric[2], uranus_geocentric[3])

    # neptune
    neptune_data = PlanetResponse('Neptune', round(neptune_values[3]), round(neptune_values[0], 6), round(neptune_values[1], 6), round(neptune_values[2], 6),
                                neptune_geocentric[0], neptune_geocentric[1], neptune_geocentric[2], neptune_geocentric[3])

    all_data = [mercury_data, venus_data, mars_data, jupiter_data, saturn_data, uranus_data, neptune_data]
             
    return all_data

def getAllData(all_data):
    mercury_data = all_data[0]
    venus_data = all_data[1]
    mars_data = all_data[2]
    jupiter_data = all_data[3]
    saturn_data = all_data[4]
    uranus_data = all_data[5]
    neptune_data = all_data[6]

    return jsonDataResponse(mercury_data, venus_data, mars_data, jupiter_data, saturn_data, uranus_data, neptune_data)

def getMiDistances(all_data):

    mercury_data_mi = all_data[0].helio_distance
    venus_data_mi = all_data[1].helio_distance
    mars_data_mi = all_data[2].helio_distance
    jupiter_data_mi = all_data[3].helio_distance
    saturn_data_mi = all_data[4].helio_distance
    uranus_data_mi = all_data[5].helio_distance
    neptune_data_mi = all_data[6].helio_distance

    serialized = serializeDistances(mercury_data_mi, venus_data_mi, mars_data_mi,
                    jupiter_data_mi, saturn_data_mi, uranus_data_mi, neptune_data_mi)
    
    return json.dumps(serialized, indent=6)

def getKmDistances(all_data):

    km_multiplier = 1.60934
    mercury_data_km = round(all_data[0].helio_distance * km_multiplier)
    venus_data_km = round(all_data[1].helio_distance * km_multiplier)
    mars_data_km = round(all_data[2].helio_distance * km_multiplier)
    jupiter_data_km = round(all_data[3].helio_distance * km_multiplier)
    saturn_data_km = round(all_data[4].helio_distance * km_multiplier)
    uranus_data_km = round(all_data[5].helio_distance * km_multiplier)
    neptune_data_km = round(all_data[6].helio_distance * km_multiplier)

    serialized = serializeDistances(mercury_data_km, venus_data_km, mars_data_km,
                    jupiter_data_km, saturn_data_km, uranus_data_km, neptune_data_km)
    
    return json.dumps(serialized, indent=6)


def getAuDistances(all_data):

    au_multiplier = 1.07578e-8
    mercury_data_au = round(all_data[0].helio_distance * au_multiplier, 8)
    venus_data_au = round(all_data[1].helio_distance * au_multiplier, 8)
    mars_data_au = round(all_data[2].helio_distance * au_multiplier, 8)
    jupiter_data_au = round(all_data[3].helio_distance * au_multiplier, 8)
    saturn_data_au = round(all_data[4].helio_distance * au_multiplier, 8)
    uranus_data_au = round(all_data[5].helio_distance * au_multiplier, 8)
    neptune_data_au = round(all_data[6].helio_distance * au_multiplier, 8)

    serialized = serializeDistances(mercury_data_au, venus_data_au, mars_data_au,
                    jupiter_data_au, saturn_data_au, uranus_data_au, neptune_data_au)
    
    return json.dumps(serialized, indent=6)
    
    
    