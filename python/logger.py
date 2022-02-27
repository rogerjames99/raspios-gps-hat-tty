from gps import *
import time
import gpxpy
import gpxpy.gpx

running = True

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        elevation = getattr(nx, 'altHAE', "Unknown")
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon, elevation))


gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

gpx = gpxpy.gpx.GPX()
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)


try:
    while running:
        getPositionData(gpsd)
        time.sleep(1.0)
    with open("output.gpx", "w") as f:
        f.write( gpx.to_xml())
    print "Track saved"

except (KeyboardInterrupt):
    running = False
