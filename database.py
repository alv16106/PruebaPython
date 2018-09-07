from math import sin, cos, sqrt, atan2, radians

# de https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
def distancia(p1, p2):
    #radio de la tierra
    R = 6373.0

    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c * 1000

def padres(id, lat, lon, dist):
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    punto = lat, lon
    onPerimeter = []
    cursor.execute('SELECT s.id, s.lat, s.lon FROM RouteStop as s WHERE s.route_id IN (SELECT r.id FROM Route as r WHERE r.school_id = %d) AND ' %id)
    paradas = cursor.fetchall()
    #paradas cercanas
    for line in paradas:
        if distancia((line[1] line[2]), punto)<dist:
            onPerimeter.append(line[0])
     cursor.execute('SELECT p.id, p.name FROM Parent as p WHERE p.id IN (SELECT s1.parent_id FROM Student as s1 WHERE s1.parada_id IN %s)' %",".join(map(str,onPerimeter)))

     for padre in cursor:
         print('ID: %d --- NAME: %d' %(padre[0], padre[1]))
    db.close()

def estMalos():
    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()
    cursor.execute('SELECT s.id, s.name, s.stop_id FROM Student as s, RouteStop as rs WHERE s.stop_id = rs.id AND rs.id IN (SELECT rs1.id FROM RouteStop rs1 INNER JOIN Route r ON r.id = rs1.route_id WHERE r.school_id != s.school_id)')
    estudiantes = curso.fetchall()
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(["ID_Student", "Nombre", "Stop ID"])
        writer.writerows(estudiantes)
