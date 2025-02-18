# File :            reg_gen.py
# Title :           reg_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates the necessary HDL logic to modify
#                   the easyaxil slave w/ parameterized # registers
#
#                   Assumes familiarity with the D. Gisselquist's 
#                   easyaxil logic 
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (11/26/24)  Jonathan Roa    1.0         Initial Revision

reg_count = 128
wr_offset = 128

# Helper hex function
def hex_with_length(num, length):
        return f"{num:0{length}x}"

f= open("axil_slv_txt_gen.txt", "w")

# Generate register declarations
f.write ("\n")
f.write ("=========================\n")
f.write ("= REGISTER DECLARATIONS\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("reg  [C_AXI_DATA_WIDTH-1:0] r" + str(i) + ";\n")

# Generate wskd wire declarations
f.write ("\n")
f.write ("=========================\n")
f.write ("= WSKD WIRE DECLARATIONS\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("wire  [C_AXI_DATA_WIDTH-1:0] wskd_r" + str(i) + ";\n")

########################
# WRITE REGISTER LOGIC
########################

# Apply wstrb
f.write ("\n")
f.write ("=========================\n")
f.write ("= APPLY WSTRB TO WSKD\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("assign wskd_r" + str(i) + " = apply_wstrb(r" + str(i) + ", wskd_data, wskd_strb);\n")

# Create initial register values
f.write ("\n")
f.write ("=========================\n")
f.write ("= INITIAL REGISTER VALUES\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("initial r" + str(i) + " = 0;\n")

# Create initial register values via reset
f.write ("\n")
f.write ("=========================\n")
f.write ("= INITIAL REGISTER VIA RST\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("r" + str(i) + " <= 0;\n")

# Generate Addressing scheme for targeting the registers
f.write ("\n")
f.write ("=========================\n")
f.write ("= ADDRESSING SCHEME FOR REG WRITES\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("8'h" + hex_with_length(wr_offset+i, 2).upper() + ":  r" + str(i) + " <= wskd_r" + str(i) + ";\n")

########################
# READ REGISTER LOGIC
########################

f.write ("\n")
f.write ("=========================\n")
f.write ("= ADDRESSING SCHEME FOR REG RD\n")
f.write ("=========================\n\n")
for i in range(reg_count):
    f.write("8'h" + hex_with_length(i, 2).upper() + ":  axil_read_data  <= r" + str(i) + ";\n")

f.close()
