import time
import requests
import gtfs_realtime_pb2
from gtfs_realtime_NYCT_pb2 import nyct_trip_descriptor, nyct_stop_time_update
from datetime import datetime

URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
STOP_ID_72_ST_S = "Q03S"
STOP_ID_72_ST_N = "Q03S"

resp = requests.get(URL, timeout=20)
resp.raise_for_status()

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(resp.content)

print(len(feed.entity))


shown = 0
for e in feed.entity:
    if e.HasField("trip_update"):
        pass
        # tu = e.trip_update
        # trip = tu.trip

        # if trip.route_id == "Q":
        #     # print(f"TRIP id:{trip.trip_id} route:{trip.route_id} direction:{trip.direction_id}")
        #     # print(len(tu.stop_time_update))
        #     stop_count = 0
        #     for stu in tu.stop_time_update:
        #         if stu.stop_id == STOP_ID_72_ST_S:
        #             arrival_ts = stu.arrival.time
        #             current_ts = time.time()
        #             time_delta_min = ((arrival_ts - current_ts) / 60)
        #             print(datetime.fromtimestamp(arrival_ts).strftime('%Y-%m-%d %H:%M:%S'))
        #             print(f"delta: {time_delta_min} mins away")
    elif e.HasField("vehicle"):
        pass
        # print(e.vehicle)
    elif e.HasField("alert"):
        print(e.alert)


    # print("----")
    # print(f"trip_id: {trip.trip_id} route_id: {trip.route_id}")

    # if trip.HasExtension(nyct_trip_descriptor):
    #     ny = trip.Extensions[nyct_trip_descriptor]
    #     print(f"nyct.train_id: {ny.train_id} assigned: {ny.is_assigned} dir: {ny.direction}")

    # for stu in tu.stop_time_update[:3]:
    #     arr = stu.arrival.time if stu.HasField("arrival") else None
    #     dep = stu.departure.time if stu.HasField("departure") else None
    #     if stu.HasExtension(nyct_stop_time_update):
    #         nstu = stu.Extensions[nyct_stop_time_update]
    #         print(f"stop_id: {stu.stop_id} arr: {arr} dep: {dep} "
    #               f"headsign: {nstu.headsign_text} sched_track: {nstu.scheduled_track} actual_track: {nstu.actual_track}")
    #     else:
    #         print(f"stop_id: {stu.stop_id} arr: {arr} dep: {dep}")

    # shown += 1
    # if shown >= 2:
    #     break
