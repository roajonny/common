# File :            sv_module_gen.py
# Title :           sv_module_gen
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Helper script to generate verilog testbench 
#                   module
# 
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (12/08/24)  Jonathan Roa    1.0         Initial Revision

##################
# TESTBENCH PROPER
##################

tb = open ("sv_tb_template.sv", "w")

# Generate the header
tb.write ("`timescale 1ns / 1ps\n\n")
tb.write ("// File :            FILE_NAME_tb.sv\n")
tb.write ("// Title :           FILE_NAME_tb\n")
tb.write ("//\n")
tb.write ("// Author(s) :       AUTHOR\n")
tb.write ("//\n")
tb.write ("// Description :     DESCRIPTION\n")
tb.write ("//\n")
tb.write ("//                   Hex stimulus data is pulled from the local text file\n")
tb.write ("//                   \"tb_stim.txt\" which is read into memory \"l_tb_stim\"\n")
tb.write ("//                   whose depth and width are defined by localparams: \n")
tb.write ("//\n")
tb.write ("//                       - 'p_STIM_CNT'   (MEMORY DEPTH)\n")
tb.write ("//                       - 'p_STIM_WIDTH' (MEMORY WIDTH)\n")
tb.write ("//\n")
tb.write ("//                   A memory with STIM_CNT=4 / p_STIM_WIDTH=32 can\n")
tb.write ("//                   be visualized as follows:\n")
tb.write ("//\n")
tb.write ("//                         |---------- 32 ---------|\n")
tb.write ("//\n")
tb.write ("//                   ---   -------------------------\n")
tb.write ("//                    |    | B3  | B2  | B1  | B0  | (l_tb_stim[0])\n")
tb.write ("//                    |    -------------------------\n")
tb.write ("//                    |    | B7  | B6  | B5  | B4  | (l_tb_stim[1])\n")
tb.write ("//                    4    -------------------------\n")
tb.write ("//                    |    | ..  | ..  | ..  | ..  | (l_tb_stim[2])\n")
tb.write ("//                    |    -------------------------\n")
tb.write ("//                    |    | B15 | ..  | ..  | ..  | (l_tb_stim[3])\n")
tb.write ("//                   ---   -------------------------\n")
tb.write ("//\n")
tb.write ("//                   Lastly, RTL testbench files are broken into sections\n")
tb.write ("//                   for better readability and \"ctrl+f\" navigation: \n")
tb.write ("//\n")
tb.write ("//                       - '(A) DECLARATIONS'\n")
tb.write ("//                       - '(B) INSTANTIATES'\n")
tb.write ("//                       - '(C) STIMULUS GEN'\n")
tb.write ("//                       - '(D) HELPER TASKS'\n")
tb.write ("//\n")
tb.write ("// Revisions\n")
tb.write ("//\n")
tb.write ("// Date        Name            REV#        Description\n")
tb.write ("// ----------  --------------- ----------- --------------------\n")
tb.write ("// (XX/XX/XX)  AUTHOR          1.0         Initial Revision\n\n")
tb.write ("module FILE_NAME_tb ();\n\n")

# Declare the clock, reset, and error count parameters
tb.write ("    // =========================\n")
tb.write ("    // --  (A) DECLARATIONS   --\n")
tb.write ("    // =========================\n\n")
tb.write ("    // Configurable sim parameters\n")
tb.write ("    localparam p_CLK_PERIOD    = 10;          // Value x Timescale, E.G. 10 x 1ns = 10ns period\n")
tb.write ("    localparam p_STIM_CNT      = 10;          // Number of stimulus entries in the text file\n")
tb.write ("    localparam p_STIM_WIDTH    = 32;          // Width of the stimulus data in the text file\n\n")

tb.write ("    localparam p_MEM_WIDTH = p_STIM_WIDTH;\n")
tb.write ("    localparam p_MEM_DEPTH = p_STIM_CNT;\n\n")
tb.write ("    integer int_ERR_COUNT;\n\n")
tb.write ("    logic l_clk;\n")
tb.write ("    logic l_rst_n;\n\n")

# Declare the memory used for storing the stimulus input from the local text file
tb.write ("    logic [p_MEM_WIDTH-1:0] l_tb_stim [p_MEM_DEPTH-1:0];\n\n")

# Give user a section to create their DUT testbench lines
tb.write ("    // Declare your DUT wires/registers\n")
tb.write ("    // and initialize them in \"init();\"\n\n")

# Instantiate the DUT
tb.write ("    // =========================\n")
tb.write ("    // --  (B) INSTANTIATES   --\n")
tb.write ("    // =========================\n\n")
tb.write ("    // Instantiate your DUT\n")
tb.write ("    // FILE_NAME #\n")
tb.write ("    // (\n")
tb.write ("    //      .p_PARAM1 (),\n")
tb.write ("    //      .p_PARAM2 ()\n")
tb.write ("    // )\n")
tb.write ("    // inst_FILE_NAME\n")
tb.write ("    // (\n")
tb.write ("    //      .PORT1    (),\n")
tb.write ("    //      .PORT2    ()\n")
tb.write ("    // );\n\n")

# Generate the clock and stimulus blocks
tb.write ("    // =========================\n")
tb.write ("    // --  (C) STIMULUS GEN   --\n")
tb.write ("    // =========================\n\n")
tb.write ("    // Clock generator\n")
tb.write ("    always begin\n")
tb.write ("        #(p_CLK_PERIOD/2); l_clk <= ~l_clk;\n")
tb.write ("    end\n\n")

tb.write ("    // Stimulus generator\n")
tb.write ("    initial begin\n\n")
tb.write ("        // Initialization sequence\n")
tb.write ("        init();\n")
tb.write ("        strobe_rst_n();\n\n")
tb.write ("        // Perform your testbench operations\n")
tb.write ("        // DUT_INPUT_PORT <= l_tb_stim[0]; (pseudo)\n")
tb.write ("    end\n\n")

# Generate the init function and give the tasks their own section
tb.write ("    // =========================\n")
tb.write ("    // --  (D) HELPER TASKS   --\n")
tb.write ("    // =========================\n\n")
tb.write ("    // The first function called during the init sequence for setting \n")
tb.write ("    // up simulation values\n")
tb.write ("    task init(); begin\n\n")
tb.write ("        // Reads in the stimulus input from the local text file\n")
tb.write ("        $readmemh(\"tb_stim.txt\", l_tb_stim, 0, p_STIM_CNT-1);\n\n")
tb.write ("        int_ERR_COUNT        <= 0;\n")
tb.write ("        l_clk                <= 1'b1;\n")
tb.write ("        l_rst_n              <= 1'b1;\n\n")
tb.write ("        // Insert your testbench DUT register initial values\n\n")
tb.write ("    end\n")
tb.write ("    endtask\n\n")

# Generate the reset strobe function
tb.write ("    // The second function called during the init sequence, setting\n")
tb.write ("    // up stimulus data to be applied a 1/2-cycle before the clock's rising edge\n")
tb.write ("    task strobe_rst_n(); begin\n")
tb.write ("        l_rst_n <= 1'b0;\n")
tb.write ("        #(p_CLK_PERIOD*500);\n")
tb.write ("        l_rst_n <= 1'b1;\n")
tb.write ("        #((p_CLK_PERIOD*500)-(p_CLK_PERIOD/2));\n")
tb.write ("    end\n")
tb.write ("    endtask\n\n")

# Generate an assert function template
tb.write ("    // A (very) useful checker for creating a self-checking testbench\n")
tb.write ("    // task assert_CONDITION(); begin\n")
tb.write ("    //     if (CONDITION) begin\n")
tb.write ("    //         $display (\"ERROR\");\n")
tb.write ("    //         int_ERR_COUNT <= int_ERR_COUNT + 1;\n")
tb.write ("    //     end else begin\n")
tb.write ("    //         $display (\"PASS\");\n")
tb.write ("    //     end\n")
tb.write ("    // end\n")
tb.write ("    // endtask\n\n")

# Generate a wait statement
tb.write ("    task wait_TIME(); begin\n")
tb.write ("        #(p_CLK_PERIOD*500);\n")
tb.write ("    end\n")
tb.write ("    endtask\n\n")

tb.write ("endmodule\n")

tb.close()

#################
# SAMPLE STIMULUS
#################

# Generate a sample testbench file
tb_stim = open ("tb_stim.txt", "w")

# Populate w/ sample stimulus
tb_stim.write ("00000000\n")
tb_stim.write ("11111111\n")
tb_stim.write ("22222222\n")
tb_stim.write ("33333333\n")
tb_stim.write ("44444444\n")
tb_stim.write ("55555555\n")
tb_stim.write ("66666666\n")
tb_stim.write ("77777777\n")
tb_stim.write ("88888888\n")
tb_stim.write ("99999999\n")

tb_stim.close();
