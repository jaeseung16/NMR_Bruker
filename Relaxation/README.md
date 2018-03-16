# T2SpinEcho

## Measuring the transverse relaxation time by using a spin echo

### Parameters
* d1: relaxation delay
* p1: excitation pulse, usually 90°
* p2: refocusing pulse, 180°
* vd: variable delay

---

# Jeener-Broekaert sequence

## Measuring the relaxation time of a dipolar order

### Parameters
* d1: relaxation delay
* p1: excitation pulse, 90°
* d2: delay for dephasing, usually 10-100 μs
* p3: rf pulse, 45°
* vd: variable delay

---

# ADRF - ARRF

## Measuring the relaxation time of a dipolar order by using adiabatic demagnetization and remagnetization
* ADRF: Adiabatic Demagnetization in the Rotating Frame
* ARRF: Adiabatic Remagnetization in the Rotating Frame

### Parameters
* d1: relaxation delay
* p1: excitation pulse, 90°
* p11: a shaped pulse, a few ms
* sp1 : shape for p11, linear decreasing ramp, power level sp1 = pl1
* p12: a shaped pulse, a few ms
* sp2 : shape for p12, linear increasing ramp, power level sp1 = pl1
* d4: delay required after a shaped pulse, 2-3 us
* vd: variable delay

---

# CPMG

## Measuring the transverse relaxation time by using the Carr-Purcell-Meiboom-Gill sequence

### Parameters
* d1: relaxation delay
* p1: excitation pulse, usually 90°
* p2: refocusing pulse, 180°
* td1: number of echoes
* vd: variable delay
* echo time = d20 + d11 * 2
* d11: delay for the command 'eoscnp'

>There is a minimum delay for the command 'eoscnp'.
>According to the TopSpin Pulse Programming manual, the minimum delay is 100 us.
>For the machine I use, the minimum delay is a few ms.
