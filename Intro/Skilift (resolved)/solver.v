module Main;

  reg [63:0] tmp3;
  reg [63:0] tmp2;
  reg [63:0] tmp1;
  reg [63:0] flag;

  initial begin
    tmp3 = 64'h5443474D489DFDD3 + 12345678; // 32'h00BC614E
    $display("El valor de tmp3 es: %h", tmp3);
    tmp2 = tmp3 ^ "HACKERS!"; // 64'h4841434B45525321
    $display("El valor de tmp2 es: %h", tmp2);
    tmp1 = tmp2 >>> 5;
    $display("El valor de tmp1 es: %h", tmp1);
    flag = tmp1 | ~(64'hF0F0F0F0F0F0F0F0);
    $display("El valor de key es: %h", flag);
  end

endmodule

// tmp4 = 64'h5443474D489DFDD3

// tmp4 = tmp3 - 12345678;
// tmp3 = 64'h5443474D489DFDD3 + 12345678 


// tmp2 = 5443474E0E142F21 ^ "HACKERS!"
// tmp2 = 5341434B4552214D


// tmp2 = tmp1 <<< 5;
// tmp1 = 5341434B4552214D >>> 5


// tmp1 = key & 64'hF0F0F0F0F0F0F0F0
// key = tmp1 | ~(64'hF0F0F0F0F0F0F0F0);