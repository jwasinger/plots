set term png
set output "graphs/addmod_large.png"
set key autotitle columnhead

set xlabel "Limb Count"
set ylabel "Gas Price"

set xrange [0:130]
set yrange [0:40]

plot 'data/op_bench_addmont.csv' using 1:2 with points, 'data/addmont_model.csv' using 1:2 with lines
