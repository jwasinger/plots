set term png
set output "graphs/mcopy.png"
set key autotitle columnhead

set xlabel "Bytes"
set ylabel "Execution Time (ns)"

plot 'data/model.csv' using 1:2 with lines, 'data/mcopy_perf.csv' using 1:2 with lines
