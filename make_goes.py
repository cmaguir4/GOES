#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Ciara Maguire 
Purpose: Produce GOES plots
Created :11 Jan 2018
"""

from __future__ import print_function, division
from sunpy.instr.goes import calculate_temperature_em
import sunpy.lightcurve as lc
import matplotlib.pyplot as plt
from sunpy.timeseries import TimeSeries
from sunpy.time import TimeRange, parse_time
from sunpy.net import hek, Fido, attrs as a
import matplotlib as mpl
import datetime as datetime
from datetime import datetime, timedelta, date
import time
import matplotlib.pyplot as plt
import matplotlib.dates as dates


mpl.rc('font', size = 12)
begin_time = datetime(2017,9,2,15,00,14)
fin_time=datetime(2017,9,2,17,30,14)
firsts=[]
for i in range(begin_time.minute, fin_time.minute):
    firsts.append(datetime(2017,9,2,15,i,14)) 
    i+10


plt.figure(figsize=(12,9))
tr = TimeRange(['2017-09-02 10:25:00', '2017-09-02 19:05:00'])
results = Fido.search(a.Time(tr), a.Instrument('XRS'))
files = Fido.fetch(results)
goes = TimeSeries(files)
client = hek.HEKClient()
flares_hek = client.search(hek.attrs.Time(tr.start, tr.end),hek.attrs.FL, hek.attrs.FRM.Name == 'SWPC')

goes.peek()
#plt.xticks(firsts)
#plt.gca().xaxis.set_major_locator(dates.HourLocator())
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
plt.xlim(begin_time,fin_time)
plt.savefig("goes_02092017.png")
