all: generate_graphs

generate_graphs:
	rm -rf data/*
	cp raw_data/evmcurves.dat data/
	python3 parse_raw_data.py
	gnuplot plotcode/plot_mulmodmont.gnu
# 	gnuplot plotcode/plot_addmod.gnu && gnuplot plotcode/plot_mulmodmont.gnu
	gnuplot plotcode/plot_addmod.gnu
	gnuplot plotcode/plot_mulmodmont_small.gnu
	gnuplot plotcode/plot_submont.gnu
	gnuplot plotcode/plot_evmcurves.gnu
