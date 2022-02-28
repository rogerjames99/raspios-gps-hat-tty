from gps import *
import time
import gpxpy
import gpxpy.gpx
from datetime import datetime

TIME_INTERVAL_SECONDS = 30.0
MAX_SEGMENT_TIME = 900.0
running = True

def saveCurrentSegment():
    with open(datetime.now().strftime("%Y-%M-%d-%H:%M:%S.gpx", "w") as f:
        f.write(gpx.to_xml())
    gpx_segment.points.clear()
    print("Segment saved")

def getPositionData(gps):
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        elevation = getattr(nx, 'altHAE', "Unknown")
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(latitude, longitude, elevation))
        # If the number of points saved multiplied by the time interval is greater
        # than the maximum segment size then save the current segment and reset it.
        if (gpx_segment.points.count * TIME_INTERVAL_SECONDS) > MAX_SEGMENT_TIME:
            saveCurrentSegment()

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

gpx = gpxpy.gpx.GPX()
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

try:
    while running:
        getPositionData(gpsd)
        time.sleep(TIME_INTERVAL_SECONDS)

except (KeyboardInterrupt):
    running = False
    saveCurrentSegment()
