
# File :            vhd_fsm_gen.py
# Title :           vhd_fsm_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates a 2-block VHDL FSM dynamically depending
#                   on the log2() ceiling of the # states specified by the 
#                   user, as well as the number of outputs specified
#
#                   E.G. Creating an FSM template for # of bits needed to
#                   encode 5 states w/ 4 outputs - in command line: 
#
#                   1) python3 vhd_fsm_gen.py 5 4
#                   2) check vhd_fsm_template.txt file
#                    
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (07/22/25)  Jonathan Roa    1.0         Initial Revision

import math
import sys

def ceil_log2(x):
    return math.ceil(math.log2(x))

def int_to_binary(num, length):
    return format(num, 'b').zfill(length)

# Number of states is input as an argument from cmd line
if len (sys.argv) == 1:
    p_STATE_COUNT  = 4
    p_OUTPUT_COUNT = 2
else:
    p_STATE_COUNT  = int(sys.argv[1])
    p_OUTPUT_COUNT = int(sys.argv[2])

f= open("vhd_fsm_template.txt", "w")

# Generates bits needed to represent all states
p_STATE_BITS = ceil_log2(p_STATE_COUNT)

# Enumerate the states
for i in range(2**p_STATE_BITS):
    if i < ((2**p_STATE_BITS)-1):
        f.write ("    constant s_STATE" + str(i) + " : " + "std_logic_vector(" + str(p_STATE_BITS-1) + " downto 0) := \"" + int_to_binary(i, p_STATE_BITS) + "\";\n")
    else:
        f.write ("    constant s_STATE" + str(i) + " : " + "std_logic_vector(" + str(p_STATE_BITS-1) + " downto 0) := \"" + int_to_binary(i, p_STATE_BITS) + "\";\n\n")

# Generate current and next state registers
f.write ("    signal r_STATE      : std_logic_vector(" + str(p_STATE_BITS-1) + " downto 0);\n")
f.write ("    signal l_STATE_NEXT : std_logic_vector(" + str(p_STATE_BITS-1) + " downto 0);\n\n")

# Declare the FSM outputs
for i in range(p_OUTPUT_COUNT):
    if i < p_OUTPUT_COUNT-1:
        f.write ("    signal l_OUTPUT_" + str(i) + " : std_logic;\n")
    else:
        f.write ("    signal l_OUTPUT_" + str(i) + " : std_logic;\n\n")

# Current state logic
f.write ("    current_state: process (i_clk, i_rst_n)\n")
f.write ("    begin\n")
f.write ("        if (rising_edge(i_clk)) then\n")
f.write ("            if (i_rst_n = '0') then\n")
f.write ("                r_STATE <= s_STATE0;\n")
f.write ("            else\n")
f.write ("                r_STATE <= l_STATE_NEXT;\n")
f.write ("            end if;\n")
f.write ("        end if;\n")
f.write ("    end process current_state;\n\n")

# Next state logic
f.write ("    next_state_output: process(all)\n")
f.write ("    begin\n")
f.write ("        case (r_STATE) is\n")

# Print primary states w/ output logic
for i in range(p_STATE_COUNT):
     f.write ("            when s_STATE" + str(i) +" =>\n")
     for i in range(p_OUTPUT_COUNT):
        if i < p_OUTPUT_COUNT-1:
            f.write ("                l_OUTPUT_" + str(i) + " <= '0';\n")
        else:
            f.write ("                l_OUTPUT_" + str(i) + " <= '0';\n\n")

# Print safe state w/ output logic
f.write ("            when others =>\n")
for i in range(p_OUTPUT_COUNT):
    if i < p_OUTPUT_COUNT-1:
        f.write ("                l_OUTPUT_" + str(i) + " <= '0';\n")
    else:
        f.write ("                l_OUTPUT_" + str(i) + " <= '0';\n\n")
f.write ("        end case;\n")
f.write ("    end process next_state_output;\n")

f.close()
