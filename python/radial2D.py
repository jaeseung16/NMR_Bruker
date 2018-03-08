import math

result1 = INPUT_DIALOG("Making a gradient trajectory - Radial 2D", "# of trajectories and initial angle", ["# of trajectories", "Initial angle (degrees)"], ["512", "0"], None, ["1", "1"] )

if result1 <> None:
	MSG("# of trajectories = " + result1[0] + "\nInitial angle = " + result1[1] + " degree")
	
	ntraj = int(result1[0])
	angle_initial = float(result1[1])
	
	phi = math.pi / 180.0 * angle_initial
	dphi = 2.0 * math.pi / float(ntraj)
	gradx = []
	grady = []
	
	for k in range(ntraj):
		gradx.append( 100.0 * math.cos(phi) )
		grady.append( 100.0 * math.sin(phi) )
		
		if phi + dphi > 2.0 * math.pi:
			phi = phi + dphi - 2.0 * math.pi
		else:
			phi = phi + dphi
			
	if CONFIRM("Making a gradient trajectory", "Do you want to make the trajectory?") == 1:
		array_x = range(ntraj)
		props_gradx = GET_DISPLAY_PROPS( array_x[1], array_x[ -1 ], "", "", "Gx", "", "line")
		props_grady = GET_DISPLAY_PROPS( array_x[1], array_x[ -1 ], "", "", "Gy", "", "line")
		DISPLAY_DATALIST_XY( [gradx, grady], [array_x, array_x], [props_gradx, props_grady], "", 1)
		
		if CONFIRM("Save the gradient file", "Do you want to save the shape into a gradient file?") == 1:
			result3 = INPUT_DIALOG("What is the name of the gradient file?", "File Name", ["File name"], ["Radial2D"])
			SAVE_SHAPE("%s%s" % (result3[0], "x"), "Excitation", gradx, array_x)
			SAVE_SHAPE("%s%s" % (result3[0], "y"), "Excitation", grady, array_x)
	
