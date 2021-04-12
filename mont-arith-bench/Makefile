all: generate_graphs

generate_graphs:
	python3 parse_raw_data.py
	rm -rf data
	mkdir data
	mv addmod.csv data/ && mv mulmodmont.csv data/
	gnuplot plotcode/plot_addmod.gnu && gnuplot plotcode/plot_mulmodmont.gnu
	gnuplot plotcode/plot_mulmodmont_small.gnu
