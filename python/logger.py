from gps import *
import time
import gpxpy
import gpxpy.gpx
from datetime import datetime

TIME_INTERVAL_SECONDS = 30.0
MAX_SEGMENT_TIME = 900.0
running = True

def saveCurrentSegment():
    with open(datetime.now().strftime("%Y-%M-%dT%H:%M:%S.gpx"), "w") as f:
        f.write(gpx.to_xml())
    gpx_segment.points.clear()
    print("Segment saved")

def getPositionData(gps):
    while True:
        nx = gpsd.next()
        print("Class = ", nx['class'])
        if nx['class'] == 'TPV':
            latitude = getattr(nx,'lat', "Unknown")
            longitude = getattr(nx,'lon', "Unknown")
            elevation = getattr(nx, 'altHAE', "Unknown")
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(latitude, longitude, elevation))
            # If the number of points saved multiplied by the time interval is greater
            # than the maximum segment size then save the current segment and reset it.
            print("Current points", len(gpx_segment.points))
            if (len(gpx_segment.points) * TIME_INTERVAL_SECONDS) > MAX_SEGMENT_TIME:
                saveCurrentSegment()
            return
        else:
            continue

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

gpx = gpxpy.gpx.GPX()
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

try:
    while running:
        print("Tick")
        getPositionData(gpsd)
        print("Tock");
        time.sleep(TIME_INTERVAL_SECONDS)

except (KeyboardInterrupt):
    running = False
    saveCurrentSegment()
