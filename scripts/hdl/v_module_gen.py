# File :            v_module_gen.py
# Title :           v_module_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Helper script to generate verilog module
# 
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (12/03/24)  Jonathan Roa    1.0         Initial Revision

f = open ("v_module_template.v", "w")

# Generate the header
f.write ("`timescale 1ns / 1ps\n\n")
f.write ("// File :            FILE_NAME.v\n")
f.write ("// Title :           FILE_NAME\n")
f.write ("//\n")
f.write ("// Author(s) :       AUTHOR\n")
f.write ("//\n")
f.write ("// Description :     DESCRIPTION\n")
f.write ("//\n")
f.write ("//                   RTL source files are broken into sections for\n")
f.write ("//                   better readability and \"ctrl+f\" navigation: \n")
f.write ("//\n")
f.write ("//                       - '(A) DECLARATIONS'\n")
f.write ("//                       - '(B) INSTANTIATES'\n")
f.write ("//                       - '(C) DESIGN LOGIC'\n")
f.write ("//\n")
f.write ("// Revisions\n")
f.write ("//\n")
f.write ("// Date        Name            REV#        Description\n")
f.write ("// ----------  --------------- ----------- --------------------\n")
f.write ("// (XX/XX/XX)  AUTHOR          1.0         Initial Revision\n\n")

# Generate the module
f.write ("module FILE_NAME #\n")
f.write ("    (\n")
f.write ("        parameter p_PARAM_0 = 32,\n")
f.write ("        parameter p_PARAM_1 = 32\n")
f.write ("    )\n")
f.write ("    (\n")
f.write ("        input  wire i_clk,\n")
f.write ("        input  wire i_rst_n,\n\n")
f.write ("        input  wire [p_PARAM_0-1:0] i_sig1,\n")
f.write ("        output wire [p_PARAM_1-1:0] o_sig2\n")
f.write ("    );\n\n")

# Break the module file into two sections for easier reading
f.write ("    // =========================\n")
f.write ("    // --  (A) DECLARATIONS   --\n")
f.write ("    // =========================\n\n")

f.write ("    // =========================\n")
f.write ("    // --  (B) INSTANTIATES   --\n")
f.write ("    // =========================\n\n")

f.write ("    // =========================\n")
f.write ("    // --  (C) DESIGN LOGIC   --\n")
f.write ("    // =========================\n\n")

f.write ("endmodule\n")

f.close()
