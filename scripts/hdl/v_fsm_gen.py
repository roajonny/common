# File :            v_fsm_gen.py
# Title :           v_fsm_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates a 2-block verilog FSM dynamically depending
#                   on the log2() ceiling of the # states specified by the 
#                   user
#
#                   E.G. Creating an FSM template for # of bits needed to
#                   encode 5 states - in command line: 
#
#                   1) python3 v_fsm_gen.py 5
#                   2) check v_fsm_template.txt file
#                    
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (12/05/24)  Jonathan Roa    1.0         Initial Revision

import math
import sys

def ceil_log2(x):
    return math.ceil(math.log2(x))

def int_to_binary(num, length):
    return format(num, 'b').zfill(length)

# Number of states is input as an argument from cmd line
if len (sys.argv) == 1:
    p_STATE_COUNT = 4
else:
    p_STATE_COUNT = int(sys.argv[1])

f= open("v_fsm_template.txt", "w")

# Generates bits needed to represent all states
p_STATE_BITS = ceil_log2(p_STATE_COUNT)

# Enumerate the states
for i in range(2**p_STATE_BITS):
    if i < ((2**p_STATE_BITS)-1):
        f.write ("    localparam s_STATE" + str(i) + " = " + str(p_STATE_BITS) + "'b" + int_to_binary(i, p_STATE_BITS) + ";\n")
    else:
        f.write ("    localparam s_STATE" + str(i) + " = " + str(p_STATE_BITS) + "'b" + int_to_binary(i, p_STATE_BITS) + ";\n\n")

# Generate current and next state registers
f.write ("    reg  [" + str(p_STATE_BITS-1) + ":0]" + " r_STATE;\n")
f.write ("    reg  [" + str(p_STATE_BITS-1) + ":0]" + " r_STATE_next;\n\n")

# Current state logic
f.write ("    // 2-block FSM\n")
f.write ("    always @ (posedge i_clk) begin\n")
f.write ("        if (!i_rst_n) begin\n")
f.write ("            r_STATE <= s_STATE0;\n")
f.write ("        end else begin\n")
f.write ("            r_STATE <= r_STATE_next;\n")
f.write ("        end\n")
f.write ("    end\n\n")

# Next state logic
f.write ("    always @ (*) begin\n")
f.write ("        case (r_STATE)\n")

for i in range(2**p_STATE_BITS):
     f.write ("            s_STATE" + str(i) +": begin\n")
     f.write ("            end\n")

f.write ("            default: begin\n")
f.write ("            end\n")
f.write ("        endcase\n")
f.write ("    end\n")


f.close()
