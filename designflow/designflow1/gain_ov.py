import numpy as np
from PyLTSpice import RawRead
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

raw = RawRead("NMOS_10u_0u15.raw", dialect="ngspice")

par_names = raw.get_trace_names()

par_prefix = par_names[1].split('[')[0]

short_names = {}
for name in par_names:
    short_name = name.split('[', 1)[1].split(']', 1)[0] if '[' in name and ']' in name else name
    short_names[short_name] = name


var1 = raw.get_trace(short_names["gm"]).get_wave()
var2 = raw.get_trace(short_names["gds"]).get_wave()
var3 = raw.get_trace(short_names["vgsteff"]).get_wave()
sweep = raw.get_trace(short_names["v(v-sweep)"]).get_wave()


plt.figure(figsize=(5, 3))
plt.plot(var3, var1*1000, color='b')
plt.xlabel('Vov = Vgs - Vth')
plt.ylabel('gm (m)', color='b')
plt.grid(True)
plt.twinx()
plt.plot(var3, var1/var2, color='r')
plt.ylabel('gm/gds', color='r')
plt.grid(True)
plt.tight_layout()
plt.show()


raw = RawRead("NMOS_100u_1u5.raw", dialect="ngspice")

par_names = raw.get_trace_names()

par_prefix = par_names[1].split('[')[0]

short_names = {}
for name in par_names:
    short_name = name.split('[', 1)[1].split(']', 1)[0] if '[' in name and ']' in name else name
    short_names[short_name] = name


var1 = raw.get_trace(short_names["gm"]).get_wave()
var2 = raw.get_trace(short_names["gds"]).get_wave()
var3 = raw.get_trace(short_names["vgsteff"]).get_wave()
sweep = raw.get_trace(short_names["v(v-sweep)"]).get_wave()


plt.figure(figsize=(5, 3))
plt.plot(var3, var1*1000, color='b')
plt.xlabel('Vov = Vgs - Vth')
plt.ylabel('gm (m)', color='b')
plt.grid(True)
plt.twinx()
plt.plot(var3, var1/var2, color='r')
plt.ylabel('gm/gds', color='r')
plt.grid(True)
plt.tight_layout()
plt.show()

