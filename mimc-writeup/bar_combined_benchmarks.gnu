reset
set term png font "Times,10"    #set terminal and output file
set output "bar_combined_benchmarks.png"

set style data histogram
set style histogram cluster gap 1

set style fill solid border rgb "black"
set auto x
set yrange [0:*]
plot 'bar_combined_benchmarks.dat' using 2:xtic(1) title col, \
        '' using 3:xtic(1) title col