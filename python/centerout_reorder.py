import struct
import os
# result1 = INPUT_DIALOG("Making a shape", "# of frequencies, # of steps, and duration", ["# of frequencies = ", "# of steps = ", "Pulse duration (in sec) = "], ["1", "1000","1"],None,["1","1","1"])

curdat = CURDATA()

if curdat <> None:
	MSG("name="+curdat[0] + ", expno=" +curdat[1] + ", procno=" + curdat[2])
else:
	MSG("Choose a dataset.")
	EXIT() 

td1 = GETPAR("1 TD")
td2 = GETPAR("2 TD")
byte_order = GETPAR("BYTORDA")
MSG("TD1=" + td1 + ", TD2=" + td2)

byte_size = int(td1) * int(td2)
file_size = byte_size * 4

fname = curdat[3] + "/" + curdat[0] + "/" + curdat[1] + "/ser"

with open(fname, 'rb') as f: 
	temp = f.read(file_size)
	if byte_order == "0":
		temp_fid = list( struct.unpack(">%dl" % byte_size, temp) ) 
	else:
		temp_fid = list( struct.unpack("<%dl" % byte_size, temp) ) 
	MSG(str(len(temp_fid)))

fid_ordered = []

for k in range(int(td1)):
	if k < int(td1)/2: 
		start_index = ( int(td1)-(2*k+1) ) * int(td2) 
	else:
		start_index = ( 2*k-int(td1) ) * int(td2) 

	for m in range(int(td2)):
			fid_ordered.append( temp_fid[ start_index + m ] )
			
# DISPLAY_DATALIST_XY([temp_fid, fid_ordered], [range(len(temp_fid)), range(len(fid_ordered))], [], "", 1)	

with open(fname + "_ordered", 'wb') as f:
	if byte_order == "0":
		for k in range(byte_size):
			f.write( struct.pack(">l", fid_ordered[k] ) )
			
			 
os.rename(fname, fname+"_old")
os.rename(fname+"_ordered", fname) 

