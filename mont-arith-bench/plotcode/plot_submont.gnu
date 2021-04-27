set term png
set output "graphs/submont_large.png"
set key autotitle columnhead

set xlabel "Limb Count (64-bit limbs)"
set ylabel "Gas Price"

set xrange [0:130]
set yrange [0:40]

plot 'data/op_bench_submont.csv' using 1:2 with points, 'data/addmont_model.csv' using 1:2 with lines
