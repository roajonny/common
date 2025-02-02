# File :            v_ff_gen.py
# Title :           v_ff_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates a programmable-width D-FF w/ enable
#                    
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (01/29/25)  Jonathan Roa    1.0         Initial Revision

f= open("v_ff_template.txt", "w")

# Generate declarations for D and Q
f.write ("    wire [WIDTH-1:0] w_d;\n")
f.write ("    reg  [WIDTH-1:0] r_q;\n\n")
f.write ("    wire w_en;\n\n")

# Generate flip-flop logic
f.write ("    always @ (posedge i_clk) begin\n")
f.write ("        if (!i_rst_n) begin\n")
f.write ("            r_q <= {WIDTH{1'b0}};\n")
f.write ("        end else if (w_en) begin\n")
f.write ("            r_q <= w_d;\n")
f.write ("        end\n")
f.write ("    end\n\n")

f.close()
