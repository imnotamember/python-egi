"""
    The only real difference in the code between this example and the "multi-threaded" one are three lines:
    Start of your script:
    1. "import egi.simple as egi" vs "import egi.threaded as egi"
    2. "ns.connect('11.0.0.42', 55513)" vs. "ns.initialize('11.0.0.42', 55513)"

    End of your script:
    3. "ns.disconnect()" vs "ns.finalize()"

    The two last differences are left intentionally,
    to make a little bit more difficult to mix up the two variants of usage of the module.
"""

import time

import egi.simple as egi

ms_localtime = egi.ms_localtime

# # # Viewing in NetStation 4.x
# # Panels / Multi-Port ECI --> log
# # or just Panels --> Log (I assume you have selected 'Long Form')
# # Timestamps listed as NetStation time since the moment of recording (relative time)

# # NetStation Changes:
# Main Window: (None)
# Log: "Connected to PC"
# Log: "NTEL" (Might be different if using non-intel CPU)
ns = egi.Netstation()
ns.connect('11.0.0.42', 55513)  # sample address and port -- change according to your network settings
ns.BeginSession()

# # NetStation Changes:
# Main Window: (None)
# Log: (timestamp)
ns.sync()

# # NetStation Changes:
# Main Window: (Colors should change from yellow to pink to indicate it is now recording)
# Log: (timestamp)
ns.StartRecording()
# Note 1: NetStation drops session files on exit if they are "too short",
#  which only occurs during these sorts of tests.
# Here, we estimate recordings less than 5 seconds in length will be dropped.
time.sleep(5)

# # # Sending an event to NetStation
# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): 'evt1'
ns.send_event('evt1')
# Note 2: Force the events to arrive in the "correct" order by padding their times with 100ms
# Typically you shouldn't need to pad times since events are typically sent with more than 1ms of time difference.
time.sleep(0.1)

# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): event2 'evt2'
ns.send_event('evt2', label="event2")
# See Note 2 above.
time.sleep(0.1)

# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): event3 'evt3'
# Log: this will appear
ns.send_event('evt3', label="event3", description="this will appear")
# See Note 2 above.
time.sleep(0.1)


# # Sending events in NetStation with Pre-calculated timestamps
# # Note 3: Events will appear in the order sent, but with "altered" timestamps
# # (i.e. `evt5` has a timestamp that is 50 ms "earlier" than `evt4`)
# # Note 4: When sending events, if you don't list anything for `timestamp=` then the timestamp
# # will automatically be set to the time the event is sent. This is the preferred method.
# # (i.e. your timestamp is based on the time you run the line, not on the time you tell it)
# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (Event-sending PC's pre-calculated timestamp): 'evt4'
ns.send_event('evt4', timestamp=egi.ms_localtime())

# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (Event-sending PC's pre-calculated timestamp minus 50ms): 'evt5'
# Log: back in time
ns.send_event('evt5', description='back in time', timestamp=egi.ms_localtime() - 50)
# See Note 2 above.
time.sleep(0.1)

# # More realistic event-sending examples
# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): 'evt_'
ns.send_event('evt_')
# See Note 2 above.
time.sleep(0.1)

# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): 'evt_'
# Log: 'fld1': 123
# Log: 'fld2': "abc"
# Log: 'fld3': 0.042
ns.send_event('evt_', table={'fld1': 123, 'fld2': "abc", 'fld3': 0.042})
# See Note 2 above.
time.sleep(0.1)

# # NetStation Changes:
# Main Window: (Event flag listed in the events track)
# Log: (timestamp): 'stop'
ns.send_event('stop')
# See Note 1 above.
time.sleep(5)

# # NetStation Changes:
# Main Window: (Colors should change from pink to yellow to indicate it the recording is now "paused")
# Log: (timestamp)
ns.StopRecording()

# # NetStation Changes:
# Main Window: Sessions will end and all session windows will close. NetStation returns to welcome-menu.
ns.EndSession()
ns.disconnect()

# # Old Notes (Not by Josh):
# 0. open file -- Events -- Event List -- opt-click -- File -- Save Events     
# 1. auto rec is not recommended
# 2. in our version of NetStation software, the 'Label' filed shows up and gets exported;
#     the 'description' appears only in the log file, so it seems to exist for amusement mostly.
# 3. evt5, 6 would appear in the corrected order ;
#    actually, *all* the events get sorted, so if som events arrive at the same millisecond,
#    they may appear in the "wrong" order in the list
