set term png
set output "graphs/mcopy.png"
set key autotitle columnhead

set xlabel "Bytes"
set ylabel "Gas Price (10ns / gas)"

set xrange [0:160]
set yrange [0:25]

plot 'data/mcopy.csv' using 1:2 with points, 'data/mcopy.csv' using 1:3 with lines
