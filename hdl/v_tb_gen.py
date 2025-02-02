# File :            v_module_gen.py
# Title :           v_module_gen
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

f = open ("v_tb_template.v", "w")

# Generate the header
f.write ("`timescale 1ns / 1ps\n\n")
f.write ("// File :            FILE_NAME_tb.v\n")
f.write ("// Title :           FILE_NAME_tb\n")
f.write ("//\n")
f.write ("// Author(s) :       AUTHOR\n")
f.write ("//\n")
f.write ("// Description :     DESCRIPTION\n")
f.write ("//\n")
f.write ("//                   Hex stimulus data is pulled from the local text file\n")
f.write ("//                   \"tb_stim.txt\" which is read into memory \"r_tb_stim\"\n")
f.write ("//                   whose depth and width are defined by localparams: \n")
f.write ("//\n")
f.write ("//                       - 'p_STIM_CNT'   (MEMORY DEPTH)\n")
f.write ("//                       - 'p_STIM_WIDTH' (MEMORY WIDTH)\n")
f.write ("//\n")
f.write ("//                   A memory with STIM_CNT=4 / p_STIM_WIDTH=32 can\n")
f.write ("//                   be visualized as follows:\n")
f.write ("//\n")
f.write ("//                         |---------- 32 ---------|\n")
f.write ("//\n")
f.write ("//                   ---   -------------------------\n")
f.write ("//                    |    | B3  | B2  | B1  | B0  | (r_tb_stim[0])\n")
f.write ("//                    |    -------------------------\n")
f.write ("//                    |    | B7  | B6  | B5  | B4  | (r_tb_stim[1])\n")
f.write ("//                    4    -------------------------\n")
f.write ("//                    |    | ..  | ..  | ..  | ..  | (r_tb_stim[2])\n")
f.write ("//                    |    -------------------------\n")
f.write ("//                    |    | B15 | ..  | ..  | ..  | (r_tb_stim[3])\n")
f.write ("//                   ---   -------------------------\n")
f.write ("//\n")
f.write ("//                   Lastly, RTL testbench files are broken into sections\n")
f.write ("//                   for better readability and \"ctrl+f\" navigation: \n")
f.write ("//\n")
f.write ("//                       - '(A) DECLARATIONS'\n")
f.write ("//                       - '(B) INSTANTIATES'\n")
f.write ("//                       - '(C) STIMULUS GEN'\n")
f.write ("//                       - '(D) HELPER TASKS'\n")
f.write ("//\n")
f.write ("// Revisions\n")
f.write ("//\n")
f.write ("// Date        Name            REV#        Description\n")
f.write ("// ----------  --------------- ----------- --------------------\n")
f.write ("// (XX/XX/XX)  AUTHOR          1.0         Initial Revision\n\n")
f.write ("module FILE_NAME_tb ();\n\n")

# Declare the clock, reset, and error count parameters
f.write ("    // =========================\n")
f.write ("    // --  (A) DECLARATIONS   --\n")
f.write ("    // =========================\n\n")
f.write ("    // Configurable sim parameters\n")
f.write ("    localparam p_CLK_PERIOD    = 10;          // Value x Timescale, E.G. 10 x 1ns = 10ns period\n")
f.write ("    localparam p_STIM_CNT      = 10;          // Number of stimulus entries in the text file\n")
f.write ("    localparam p_STIM_WIDTH    = 10;          // Width of the stimulus data in the text file\n\n")

f.write ("    localparam p_MEM_WIDTH = p_STIM_WIDTH;\n")
f.write ("    localparam p_MEM_DEPTH = p_STIM_CNT;\n\n")
f.write ("    integer int_ERR_COUNT;\n\n")
f.write ("    reg r_clk;\n")
f.write ("    reg r_rst_n;\n\n")

# Declare the memory used for storing the stimulus input from the local text file
f.write ("    reg [p_MEM_WIDTH-1:0] r_tb_stim [p_MEM_DEPTH-1:0];\n\n")

# Give user a section to create their DUT testbench lines
f.write ("    // Declare your DUT wires/registers\n")
f.write ("    // and initialize them in \"init();\"\n\n")

# Instantiate the DUT
f.write ("    // =========================\n")
f.write ("    // --  (B) INSTANTIATES   --\n")
f.write ("    // =========================\n\n")
f.write ("    // Instantiate your DUT\n")
f.write ("    // FILE_NAME #\n")
f.write ("    // (\n")
f.write ("    //      .p_PARAM1 (),\n")
f.write ("    //      .p_PARAM2 ()\n")
f.write ("    // )\n")
f.write ("    // inst_FILE_NAME\n")
f.write ("    // (\n")
f.write ("    //      .PORT1    (),\n")
f.write ("    //      .PORT2    ()\n")
f.write ("    // );\n\n")

# Generate the clock and stimulus blocks
f.write ("    // =========================\n")
f.write ("    // --  (C) STIMULUS GEN   --\n")
f.write ("    // =========================\n\n")
f.write ("    // Clock generator\n")
f.write ("    always begin\n")
f.write ("        #(p_CLK_PERIOD/2); r_clk <= ~r_clk;\n")
f.write ("    end\n\n")

f.write ("    // Stimulus generator\n")
f.write ("    initial begin\n\n")
f.write ("        // Initialization sequence\n")
f.write ("        init();\n")
f.write ("        strobe_rst_n();\n\n")
f.write ("        // Perform your testbench operations\n")
f.write ("        // DUT_INPUT_PORT <= r_tb_stim[0]; (pseudo)\n")
f.write ("    end\n\n")

# Generate the init function and give the tasks their own section
f.write ("    // =========================\n")
f.write ("    // --  (D) HELPER TASKS   --\n")
f.write ("    // =========================\n\n")
f.write ("    // The first function called during the init sequence for setting \n")
f.write ("    // up simulation values\n")
f.write ("    task init(); begin\n\n")
f.write ("        // Reads in the stimulus input from the local text file\n")
f.write ("        $readmemh(\"tb_stim.txt\", r_tb_stim, 0, p_STIM_CNT-1);\n\n")
f.write ("        int_ERR_COUNT        <= 0;\n")
f.write ("        r_clk                <= 1'b1;\n")
f.write ("        r_rst_n              <= 1'b1;\n\n")
f.write ("        // Insert your testbench DUT register initial values\n\n")
f.write ("    end\n")
f.write ("    endtask\n\n")

# Generate the reset strobe function
f.write ("    // The second function called during the init sequence, setting\n")
f.write ("    // up stimulus data to be applied a 1/2-cycle before the clock's rising edge\n")
f.write ("    task strobe_rst_n(); begin\n")
f.write ("        r_rst_n <= 1'b0;\n")
f.write ("        #(p_CLK_PERIOD*500);\n")
f.write ("        r_rst_n <= 1'b1;\n")
f.write ("        #((p_CLK_PERIOD*500)-(p_CLK_PERIOD/2));\n")
f.write ("    end\n")
f.write ("    endtask\n\n")

# Generate an assert function template
f.write ("    // A (very) useful checker for creating a self-checking testbench\n")
f.write ("    // task assert_CONDITION(); begin\n")
f.write ("    //     if (CONDITION) begin\n")
f.write ("    //         $display (\"ERROR\");\n")
f.write ("    //         int_ERR_COUNT <= int_ERR_COUNT + 1;\n")
f.write ("    //     end else begin\n")
f.write ("    //         $display (\"PASS\");\n")
f.write ("    //     end\n")
f.write ("    // end\n")
f.write ("    // endtask\n\n")

# Generate a wait statement
f.write ("    task wait_TIME(); begin\n")
f.write ("        #(p_CLK_PERIOD*500);\n")
f.write ("    end\n")
f.write ("    endtask\n\n")

f.write ("endmodule\n")

f.close()
