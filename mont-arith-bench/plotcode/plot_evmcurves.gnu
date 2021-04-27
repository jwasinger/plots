set term png
set output "graphs/evmcurves.png"

set ylabel "Performance (ms)"

set style data histogram
set style histogram cluster gap 1

set style fill solid border rgb "black"

set yrange [0:4]

plot 'data/evmcurves.dat' using 2:xtic(1) title col, \
        '' using 3:xtic(1) title col
