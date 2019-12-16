from __future__ import print_function, division

import matplotlib.pyplot as plt
import datetime as datetime
from sunpy.timeseries import TimeSeries
from sunpy.time import TimeRange, parse_time
from sunpy.net import hek, Fido, attrs as a
from matplotlib import dates,colors
"""
tr = TimeRange(['2017-09-10 12:00', '2017-09-10 16:00'])
results = Fido.search(a.Time(tr), a.Instrument('XRS'))
results
files = Fido.fetch(results)
goes = TimeSeries(files)
"""
results= '/Users/cmaguir4/sunpy/data/go1520170910.fits'
goes = TimeSeries(results, source='XRS')  
#plt.plot(goes)
#plt.legend(loc=2)
#t.show()


xr=goes.data.xrsa
xr1=goes.data.xrsb
time_goes=goes.data.index 
font = {'size': 10, 'color':'k'}

plt.figure(figsize=(8,5))
ax2=plt.subplot(1,1,1)
plt.plot(time_goes,xr1 ,'-',label=('GOES '+str(1.0)+'-'+str(8.0)+' '+r'$\AA$'),linewidth=0.9)

plt.plot(time_goes,xr ,'-',label=('GOES '+str(0.5)+'-'+str(4)+' '+r'$\AA$'),linewidth=0.9)

plt.ylabel('Xray Flux'+'\n'+'(Watts m$^-$$^2$)')
plt.xlabel('Start Time: 2017-09-10 11:30')
plt.legend(loc=1,frameon=False,markerscale=0)
ax2.xaxis_date()
ax2.text(datetime.datetime(2017,9,10, 12, 30, 7), 10**-5.5,'Pre-flare phase', fontdict=font)
ax2.text(datetime.datetime(2017,9,10, 13, 36, 7), 10**-3.3,'Impulsive phase', fontdict=font)
ax2.text(datetime.datetime(2017,9,10, 18, 0, 0), 10**-3.9,'Gradual phase', fontdict=font)


ax2.xaxis.set_major_locator(dates.MinuteLocator(interval=90))

ax2.xaxis.set_minor_locator(dates.MinuteLocator(interval=30))
ax2.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
ax2.set_yticks((1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2))
plt.grid()
plt.xlim(datetime.datetime(2017,9,10, 11, 40, 0),datetime.datetime(2017,9,10, 23, 50, 0))
ax2.set_yscale('log')
ax2.set_ylim(10**-9,10**-2)

ax = ax2.twinx()
ax.set_yscale("log")
ax.set_ylim(1e-9, 1e-2)
ax.set_yticks((1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2))
ax.set_yticklabels((' ', 'A', 'B', 'C', 'M', 'X', ' '))
plt.savefig('goes.pdf',dpi=500)