all: generate_graphs

generate_graphs:
	rm -rf data
	mkdir data
	python3 parse_raw_data.py
	gnuplot plotcode/plot_mcopy.gnu
