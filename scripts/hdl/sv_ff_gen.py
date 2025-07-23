# File :            sv_ff_gen.py
# Title :           sv_ff_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates a programmable-width D-FF w/ enable
#                    
#                   E.G. Creating a FF template for 3-bit width signal in
#                   command line:
#
#                   1) python3 sv_ff_gen.py 3
#                   2) check sv_ff_template.txt file
#
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (01/29/25)  Jonathan Roa    1.0         Initial Revision

import sys

f= open("sv_ff_template.txt", "w")

if len (sys.argv) == 1:
    p_DATA_WIDTH = 0;
else:
    p_DATA_WIDTH = int(sys.argv[1])

# Generate declarations for D and Q
f.write ("    localparam WIDTH = " + str(p_DATA_WIDTH) + ";\n\n")
f.write ("    wire [WIDTH-1:0] w_d;\n")
f.write ("    reg  [WIDTH-1:0] r_q;\n\n")
f.write ("    wire w_en;\n\n")

# Generate flip-flop logic
f.write ("    always_ff @ (posedge i_clk) begin\n")
f.write ("        if (!i_rst_n) begin\n")
f.write ("            r_q <= {WIDTH{1'b0}};\n")
f.write ("        end else if (w_en) begin\n")
f.write ("            r_q <= w_d;\n")
f.write ("        end\n")
f.write ("    end\n\n")

f.close()
