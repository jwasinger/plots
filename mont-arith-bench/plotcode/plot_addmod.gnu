set term png
set output "graphs/addmod_large.png"
set key autotitle columnhead

set xlabel "Limb Count"
set ylabel "Gas Price"

set xrange [0:160]
set yrange [0:25]

plot 'data/addmod.csv' using 1:2 with points, 'data/addmod.csv' using 1:3 with lines
