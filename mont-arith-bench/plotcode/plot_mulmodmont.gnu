set term png
set output "graphs/mulmodmont_large.png"
set key autotitle columnhead

set xlabel "Limb Count"
set ylabel "Gas Price"

plot 'data/op_bench_mulmont.csv' using 1:2 with points, 'data/mulmont_model.csv' using 1:2 with lines, 'data/op_bench_blstasm384_mulmont.csv' using 1:2 with points
