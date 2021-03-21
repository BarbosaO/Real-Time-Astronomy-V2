import math

def rev(angle):
    """ Minimize an angle to [0, 360] degrees """
    while(angle <= 0 or angle >= 360):
        if(angle < 0):
            angle += 360
        else:
            angle -= 360
    return angle

def toRadians():
    """ Converts degrees to radians for trigonometric functions"""
    return math.pi / 180

def calculateData(N, i, w, a, e, M):
    """ Calculates inital orbital data """
    # verify that w and M are between 0 and +360
    if(N < 0 or N > 360):
        n = (int)(N / 360)
        if(w < 0):
            N += 360 * n
        else:
            N -= 360 * n

    if(w < 0 or w > 360):
        n = (int)(w / 360)
        if(w < 0):
            w += 360 * n
        else:
            w -= 360 * n

    if(M < 0 or M > 360):
        k = (int)(M / 360)
        if(M < 0):
            M += 360 * k
        else:
            M -= 360 * k

    toRadians = math.pi / 180
    
    # get initial value for E
    E = M + (e * (180/math.pi)) * math.sin(toRadians * M) * (1.0 + e * math.cos(toRadians * M))
    E_0 = E

    # perform iteration until accurate enough
    while(True):
        E_1 = E_0 - (E_0 - (e * (180/math.pi)) * math.sin(E_0 * toRadians) - M) / (1 - e * math.cos(toRadians *  E_0))

        error = abs(E_1 -E_0)
        E_0 = E_1

        if(error < 1.0e-8):
            break
    
    x = a * (math.cos(E_0 * toRadians) - e)
    y = a * (math.sqrt(1.0 - e * e) * math.sin(E_0 * toRadians))
    v = math.degrees(math.atan2(y , x))
    v = rev(v)

    r = math.sqrt(x * x + y * y)
    rMi = r * 92955807.26743

    # get heliocentric cartesian coordinates for planet
    xh = r * (math.cos(toRadians * N) * math.cos(toRadians * (v+w)) - math.sin(toRadians * N) * math.sin(toRadians * (v+w)) * math.cos(toRadians * i))
    yh = r * (math.sin(toRadians * N) * math.cos(toRadians * (v+w)) + math.cos(toRadians * N) * math.sin(toRadians * (v+w)) * math.cos(toRadians * i))
    zh = r * (math.sin(toRadians * (v+w)) * math.sin(toRadians * i))

    # get heliocentric distance
    rh = math.sqrt(xh * xh + yh * yh + zh * zh)

    # get ecliptic longitude and latitude to correct for perturbations (Jupiter, Saturn, and Uranus only)
    lonecl = rev(math.degrees(math.atan2(yh, xh)))
    
    latecl = math.degrees(math.atan2(zh, math.sqrt(xh * xh + yh * yh)))

    # converting factor from 1 AU to 1 mile
    milesPerAu = 92955807.26743

    # get current distance in miles
    rhMi = rh * milesPerAu
    
    # calculate geocentric distances

    # store returning values
    values = [xh, yh, zh, rhMi, lonecl, latecl, rh, x, y, v, E_0, r]

    return values

def calculateJupiterPert(Mj, Ms, longitude, latitude, rh):
    """ Calculates Jupiter perturbations """
    # perturbation correction for Jupiter Heliocentric Longitude
    j1 = -0.332 * math.sin((2*Mj - 5*Ms - 67.6) * toRadians())
    j2 = -0.056 * math.sin((2*Mj - 2*Ms + 21.0) * toRadians())
    j3 = +0.042 * math.sin((3*Mj - 5*Ms + 21.0) * toRadians())
    j4 = -0.036 * math.sin((Mj - 2*Ms)* toRadians ())
    j5 = +0.022 * math.cos((Mj - Ms) * toRadians ())
    j6 = +0.023 * math.sin((2*Mj - 3*Ms + 52.0)* toRadians())
    j7 = -0.016 * math.sin((Mj - 5*Ms - 69.0) * toRadians())

    # total corrections for Jupiter Heliocentric Longitude
    totalCorrections = j1 + j2 + j3 + j4 + j5 + j6 + j7
    
    # new corrected Jupiter Heliocentric Logitude
    correctedJupiterLong = longitude + totalCorrections

    # new hx, hy, and hy values 
    xh = rh * (math.cos(correctedJupiterLong * toRadians()) * math.cos(latitude * toRadians()))
    yh = rh * (math.sin(correctedJupiterLong * toRadians()) * math.cos(latitude * toRadians()))
    zh = rh * (math.sin(latitude * toRadians()))

    # new rh value
    rh = math.sqrt(xh * xh + yh * yh + zh * zh)

    # converting factor from 1 AU to 1 mile
    milesPerAu = 92955807.26743

    # get current distance in miles
    rhMi = rh * milesPerAu

    return [rhMi, xh, yh, zh]

def calculateSaturnPert(Mj, Ms, longitude, latitude, rh):
    """ Calculates Saturn perturbations """

    # perturbation correction for Saturn Heliocentric Logitude
    s1 = 0.812 * (math.sin((2*Mj - 5*Ms - 67.6) * toRadians()))
    s2 = -0.229 * (math.cos((2*Mj - 4*Ms - 2.0) * toRadians())) 
    s3 = 0.119 * (math.sin((Mj - 2*Ms - 3.0) * toRadians()))
    s4 = 0.046 * (math.sin((2*Mj - 6*Ms - 69.0) * toRadians()))
    s5 = 0.014 * (math.sin((Mj - 3*Ms + 32.0)))

    # perturbation correction for Saturn Heliocentric Latitude
    s6 = 0.018 * (math.sin((2 * Mj - 6*Ms - 49.0) * toRadians()))
    s7 = -0.020 * (math.cos((2*Mj - 4*Ms - 2.0)* toRadians()))

    # total corrections for Saturn Heliocentric Longitude
    totalLongCorrections = s1 + s2 + s3 + s4 + s5

    # total corrections for Saturn Heliocentric Latitude
    totalLatCorrections = s6 + s7

    # new corrected Saturn Heliocentric Longitude
    correctedSaturnLong = longitude + totalLongCorrections

    # new corrected Jupiter Heliocentric Latitude
    correctedSaturnLat = latitude + totalLatCorrections

    # new hx, hy, and hy values 
    xh = rh * math.cos((correctedSaturnLong) * toRadians()) * math.cos((correctedSaturnLat) * toRadians())
    yh = rh * math.sin((correctedSaturnLong) * toRadians()) * math.cos((correctedSaturnLat) * toRadians())
    zh = rh * math.sin((correctedSaturnLat) * toRadians())

    # new rh value
    rh = math.sqrt(xh * xh + yh * yh + zh * zh)
   
    # converting factor from 1 AU to 1 mile
    milesPerAu = 92955807.26743

    # get current distance in miles
    rhMi = rh * milesPerAu

    return [rhMi, xh, yh, zh]
 
def calculateUranusPert(Mj, Ms, Mu, longitude, latitude, rh):
    """ Calculates Uranus perturbations """
    
    # perturbation correction for Uranus Heliocentric Logitude
    u1 = 0.040 * (math.sin((Ms - 2*Mu + 6.0) * toRadians()))
    u2 = 0.035 * (math.sin((Ms - 3*Mu + 33.0) * toRadians())) 
    u3 = -0.015 * (math.sin((Mj - Mu + 20.0) * toRadians()))

    # total corrections for Uranus Heliocentric Longitude
    totalLongCorrections = u1 + u2 + u3

    # new corrected Uranus Heliocentric Longitude
    correctedUranusLong = longitude + totalLongCorrections

    # new hx, hy, and hy values 
    xh = rh * math.cos((correctedUranusLong) * toRadians()) * math.cos((latitude) * toRadians())
    yh = rh * math.sin((correctedUranusLong) * toRadians()) * math.cos((latitude) * toRadians())
    zh = rh * math.sin((latitude) * toRadians())

    # new rh value
    rh = math.sqrt(xh * xh + yh * yh + zh * zh)

    # converting factor from 1 AU to 1 mile
    milesPerAu = 92955807.26743

    # get current distance in miles
    rhMi = rh * milesPerAu
    
    return [rhMi, xh, yh, zh]

def calculateSunData(N, i, w, a, e, M):
    """ Calculates sun data for geocentric coordinates of planets """

    E = M + e*(180/math.pi) * math.sin(M * toRadians()) * (1.0 + e * math.cos(M * toRadians()))

    xv = math.cos(E * toRadians()) - e
    yv = math.sqrt(1.0 - e*e) * math.sin(E * toRadians())

    v = math.degrees(math.atan2(yv, xv))
    v = rev(v)

    r = math.sqrt(xv*xv + yv*yv)

    lonsun = v + w
    lonsun = rev(lonsun)

    # conversion to radians
    xs = r * math.cos(lonsun * toRadians())
    ys = r * math.sin(lonsun * toRadians())

    return [xs, ys, xv, yv, E, v, lonsun, r] 

def calculateGeocentric(xs, ys, xh, yh, zh):
    """ Calculates geocentric coordinates of planets """
    
    xg = xh + xs
    yg = yh + ys
    zg = zh

      # new rh value
    rg = math.sqrt(xg * xg + yg * yg + zg * zg)

    # converting factor from 1 AU to 1 mile
    milesPerAu = 92955807.26743

    # get current distance in miles
    rgMi = rg * milesPerAu

    return [rgMi, round(xg, 6), round(yg, 6), round(zg, 6)]

    
