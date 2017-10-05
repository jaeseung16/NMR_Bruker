# UFZref

## Reference scan for Ultrafast Z-Spectroscopy

### Parameters
* d1: relaxation delay

**1D imaging with spin echo**
* p1: excitation pulse, usually 90°
* cnst23: I used 5 for CEST, 10 for MT
* d27: half of echo time 10 ~ 20 ms
* p2: refocusing 180° pulse}

**Acquisition**
* d15: delay for safety, try 0 us
* aq: about 2 × d27, 20 ~ 40 ms

**Acqusition**
* td: 2048 or 4096
* sw: ~100 kHz
* AQ_mod: DQD
* DSPFIRM: medium
* DE: 4.5 μs or less

**Processing**
* si: td/2

# UFZsat

## Scan with pre-saturation for Ultrafast Z-Spectroscopy

### Parameters
* d1: relaxation delay

**Saturation**
* p18: saturation pulse, usually 1 sec
* sp6: shape parameters for the saturation pulse, usually rectangular pulse & γB<sub>1</sub>/2π = 100 Hz
* cnst24: strength of a crusher gradient
* d12: duration of a crusher gradient

**1D imaging with spin echo**
* p1: excitation pulse, usually 90°
* cnst23: I used 5 for CEST, 10 for MT
* d27: half of echo time 10 ~ 20 ms
* p2: refocusing 180° pulse}

**Acquisition**
* d15: delay for safety, try 0 us
* aq: about 2 × d27, 20 ~ 40 ms

**Acqusition**
* td: 2048 or 4096
* sw: ~100 kHz
* AQ_mod: DQD
* DSPFIRM: medium
* DE: 4.5 μs or less

**Processing**
* si: td/2
