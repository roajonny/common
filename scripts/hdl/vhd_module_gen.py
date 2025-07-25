# File :            vhd_module_gen.py
# Title :           vhd_module_gen
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

f = open ("vhd_module_template.vhd", "w")

# Generate the header
f.write ("-- File :            FILE_NAME.vhd\n")
f.write ("-- Title :           FILE_NAME\n")
f.write ("--\n")
f.write ("-- Author(s) :       AUTHOR\n")
f.write ("--\n")
f.write ("-- Description :     DESCRIPTION\n")
f.write ("--\n")
f.write ("--                   RTL source files are broken into sections for\n")
f.write ("--                   better readability and \"ctrl+f\" navigation: \n")
f.write ("--\n")
f.write ("--                       - '(A) DECLARATIONS'\n")
f.write ("--                       - '(B) INSTANTIATES'\n")
f.write ("--                       - '(C) DESIGN LOGIC'\n")
f.write ("--\n")
f.write ("-- Revisions\n")
f.write ("--\n")
f.write ("-- Date        Name            REV#        Description\n")
f.write ("-- ----------  --------------- ----------- --------------------\n")
f.write ("-- (XX/XX/XX)  AUTHOR          1.0         Initial Revision\n\n")

# Declare libraries
f.write ("library IEEE;\n")
f.write ("use IEEE.STD_LOGIC_1164.ALL;\n")
f.write ("-- use IEEE.NUMERIC_STD.ALL;\n\n")

f.write ("-- library UNISIM;\n")
f.write ("-- use UNISIM.VComponents.all;\n\n")

# Generate the module
f.write ("entity FILE_NAME is\n")
f.write ("    generic\n")
f.write ("    (\n")
f.write ("        g_PARAM_0 : integer := 32;\n")
f.write ("        g_PARAM_1 : integer := 32\n")
f.write ("    );\n")
f.write ("    port\n")
f.write ("    (\n")
f.write ("        i_clk   : in std_logic;\n")
f.write ("        i_rst_n : in std_logic;\n\n")
f.write ("        i_sig1 : in  std_logic_vector(g_PARAM_0-1 downto 0);\n")
f.write ("        o_sig2 : out std_logic_vector(g_PARAM_1-1 downto 0)\n")
f.write ("    );\n")
f.write ("end FILE_NAME;\n\n")

f.write ("architecture FILE_NAME_arch of FILE_NAME is\n\n")

f.write ("    -- =========================\n")
f.write ("    -- --  (A) DECLARATIONS   --\n")
f.write ("    -- =========================\n\n")

f.write ("begin\n\n")

# Break the module file into two sections for easier reading

f.write ("    -- =========================\n")
f.write ("    -- --  (B) INSTANTIATES   --\n")
f.write ("    -- =========================\n\n")

f.write ("    -- =========================\n")
f.write ("    -- --  (C) DESIGN LOGIC   --\n")
f.write ("    -- =========================\n\n")

f.write ("end FILE_NAME_arch;\n")

f.close()
