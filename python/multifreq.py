import math

def shape_mf(freq, duration, nstep):
	amplitudes = [] #  normalized to 0...100
	phases = [] # in degrees
	
	nfreq = len(freq)
	dt = duration / nstep
	
	for i in range(nstep):
		temp_real = 0.0
		temp_imag = 0.0
		for k in range(nfreq):
			temp_phase = 2.0 * math.pi * i * freq[k] * dt
			temp_real += math.cos( temp_phase )
			temp_imag += math.sin( temp_phase )
		
		amplitudes.append(100.0 / nfreq * math.sqrt(math.pow(temp_real,2) + math.pow(temp_imag,2)))
		phases.append(math.degrees(math.atan2(temp_imag, temp_real) ))

	return (amplitudes, phases)

result1 = INPUT_DIALOG("Making a shape", "# of frequencies, # of steps, and duration",
                       ["# of frequencies = ", "# of steps = ", "Pulse duration (in sec) = "],
                       ["1", "1000","1"],None,["1","1","1"])
if result1 <> None:
	MSG("# of frequencies = " + result1[0] + "\n# of steps = "+ result1[1]
        + "\nPulse duration = "+ result1[2] + " sec")
	nfreq = float(result1[0])
	nstep = float(result1[1])
	duration = float(result1[2])
	
	text = []
	value = []
	for i in range(nfreq):
		text.append("Frequency #" + str(i) + " in Hz = ")
		value.append("0.0")
	
	result2 = INPUT_DIALOG("What are those frequencies?", "Frequency Offsets", text, value)
	freq = []
	freqlist = ""
	for i in range(nfreq):
		freq.append( float( result2[i] ) )
		freqlist += "Frequency #" + str(i+1) + " at " + str(result2[i]) + "Hz\n"
				
	MSG(freqlist)
	
	if CONFIRM("Making a shape","Do you want to make a shape with the frequency list?") == 1:
		amplitudes, phases = shape_mf(freq, duration, nstep)
		array_x = range(nstep)
		props_amp = GET_DISPLAY_PROPS(array_x[1], array_x[int(nstep)-1], "", "", "amplitude", "", "line")
		props_phase = GET_DISPLAY_PROPS(array_x[1], array_x[int(nstep)-1], "", "", "phase", "", "line")
		DISPLAY_DATALIST_XY([amplitudes, phases], [array_x, array_x], [props_amp, props_phase], "", 1)		
		
		if CONFIRM("Save the shape file","Do you want to save the shape into a wavefile?") == 1:
			result3 = INPUT_DIALOG("What is the name of the wavefile?", "File name",
                                   ["File name"], ["multi-frequency"])
			SAVE_SHAPE(result3[0], "", amplitudes, phases)
