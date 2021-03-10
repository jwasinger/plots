reset
set term png font "Times,18"    #set terminal and output file
set output "arith_benchmarks.png"
# set xlabel "x value"    #set x and y label
set ylabel "Execution Time (ns)"
set xrange [-0.5:5]    #set x and y range
set yrange [0:300]
# set xtics 0,1,4    #set xtics
set style fill solid    #set plot style
set boxwidth 0.5
unset key    #legend not plotted
set xtics font ", 10"
set xtics rotate by -45
plot "bar_arith_benchmarks.dat" using 1:3:xtic(2) with boxes,\
	"bar_arith_benchmarks.dat" using 1:($3 + 10):3 with labels font ",10"

#plot bar chart and the value labels on the bars
