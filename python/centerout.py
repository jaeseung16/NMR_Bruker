import math

result1 = INPUT_DIALOG("Making a center-out graident shape", "# of phase encoding steps", ["# of phase encoding steps"], ["32"], None, ["1"] )

if result1 <> None:
	MSG("# of phase encoding steps = " + result1[0])
	
	nstep = int(result1[0])
	pos_half = range(0, nstep, 2)

	all = []
		
	amp = lambda x: 100.0 * float(x) / float(nstep)
	
	for k in range(nstep):
		if k in pos_half:
			all.append(amp(k))
		else:
			all.append(amp(-k-1))
			
	if CONFIRM("Making a gradient trajectory", "Do you want to make the trajectory?") == 1:
		array_x = range(0, nstep)
		props_gradx = GET_DISPLAY_PROPS( array_x[1], array_x[ -1 ], "", "", "Gx", "", "line")
		DISPLAY_DATALIST_XY( [all], [array_x], [props_gradx], "", 1)
		
		if CONFIRM("Save the gradient file", "Do you want to save the shape into a gradient file?") == 1:
			result3 = INPUT_DIALOG("What is the name of the gradient file?", "File Name", ["File name"], ["CenterOut"])
			SAVE_SHAPE("%s%s" % (result3[0], result1[0]), "Excitation", all, array_x)
	
