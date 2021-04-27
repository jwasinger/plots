set term png
set output "graphs/mulmodmont_large.png"
set key autotitle columnhead

set xlabel "Limb Count"
set ylabel "Gas Price"

plot 'data/mulmodmont.csv' using 1:2 with points, 'data/mulmodmont.csv' using 1:3 with lines, 'data/mulmodmont_blstasm384.csv' using 1:2 with points
