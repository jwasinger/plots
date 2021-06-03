import re
import numpy as np

# parse a line like:
#	BenchmarkAddMod/num_limbs=26            32510698                36.60 ns/op
# return (bench_type, num_limbs, bench_time)
def parse_go_benchmark_line(line: str) -> (str, int, float):
	m = re.match(r"Benchmark(.*)/(\d+)_bytes .* (.*) ns/op", line)
	if m and len(m.groups()) == 3:
		result = m.group(1), int(m.group(2)), float(m.group(3))
		return result
	else:
		return None

def parse_dataset(dataset_file: str) -> [(str, int, float)]:
	results = []
	with open(dataset_file) as f:
		lines = f.readlines()
		for line in lines:
			result = parse_go_benchmark_line(line)
			if result:
				results.append(result)

	return results

def format_model(points, slope, intercept) -> [int]:
	return [(point - 256, point * slope + intercept) for point in points]

# 3 column format 
# copy_size | fitted_x | fitted_y
def format_model_csv(dataset: []) -> str:
	result = ["Model, Model"]
	xs = np.array([int(x_val) for (_, x_val, _) in dataset])
	ys = np.array([int(y_val) for (_, _, y_val) in dataset])

	slope, _ = np.polyfit(xs, ys, 1)
	intercept = ys[0] # make sure the model doesn't have negative values :)
	import pdb; pdb.set_trace()

	model_points = format_model(range(256, int(dataset[-1][1]), 256), slope, intercept)

	for (i, (x, y)) in enumerate(model_points):
		result.append("{}, {}".format(x, y))

	return "\n".join(result)

def format_mcopy_perf_csv(dataset: []) -> str:
	result = ["\"MCOPY Performance\", \"MCOPY Performance\""]
	for (_, copy_size, performance) in dataset:
		performance_gas = round(performance / 10)
		result.append("{}, {}".format(copy_size, performance))
	
	return "\n".join(result)

dataset = parse_dataset('raw_data.txt')[:312]
# format_graph_csv(dataset)
model_csv = format_model_csv(dataset)
perf_csv = format_mcopy_perf_csv(dataset)

with open('data/model.csv', 'w') as f:
	f.write(model_csv)

with open('data/mcopy_perf.csv', 'w') as f:
	f.write(perf_csv)
