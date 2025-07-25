# File :            vhd_ff_gen.py
# Title :           vhd_ff_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates a programmable-width D-FF w/ enable
#                    
#                   E.G. Creating a FF template for 3-bit width signal in
#                   command line:
#
#                   1) python3 vhd_ff_gen.py 3
#                   2) check vhd_ff_template.txt file
#
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (01/29/25)  Jonathan Roa    1.0         Initial Revision

import sys

f= open("vhd_ff_template.txt", "w")

if len (sys.argv) == 1:
    p_DATA_WIDTH = 0;
else:
    p_DATA_WIDTH = int(sys.argv[1])

# Generate declarations for D and Q
f.write ("    constant WIDTH : integer := " + str(p_DATA_WIDTH) + ";\n\n")
f.write ("    signal w_d : std_logic_vector(WIDTH-1 downto 0);\n")
f.write ("    signal r_q : std_logic_vector(WIDTH-1 downto 0);\n\n")
f.write ("    signal w_en : std_logic;\n\n")

# Generate flip-flop logic
f.write ("    process (i_clk, i_rst_n)\n")
f.write ("    begin\n")
f.write ("        if (rising_edge(i_clk)) then\n")
f.write ("            if (i_rst_n = '0') then\n")
f.write ("                r_q <= (others => '0');\n")
f.write ("            elsif (w_en) then\n")
f.write ("                r_q <= w_d;\n")
f.write ("            end if;\n")
f.write ("        end if;\n")
f.write ("    end process;\n\n")

f.close()
