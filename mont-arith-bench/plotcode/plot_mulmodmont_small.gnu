set term png
set output "graphs/mulmodmont_small.png"
set key autotitle columnhead

set xrange [0:20]
set yrange [0:140]

set xlabel "Limb Count"
set ylabel "Gas Price"

plot 'data/mulmodmont.csv' every ::::15 using 1:2 with points, 'data/mulmodmont.csv' using 1:3 with lines
