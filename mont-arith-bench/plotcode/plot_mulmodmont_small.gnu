set term png
set output "graphs/mulmodmont_small.png"
set key autotitle columnhead

set xlabel "Limb Count"
set ylabel "Gas Price"

set xrange [0:10]
set yrange [0:25]

plot 'data/op_bench_mulmont.csv' every ::::9 using 1:2 with points, 'data/mulmont_model.csv' every ::::9 using 1:2 with lines, 'data/op_bench_blstasm384_mulmont.csv' every ::::9 using 1:2 with points
