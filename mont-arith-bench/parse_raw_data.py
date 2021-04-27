import re
import sys

def paul_addmod_submod_cost(limb_count: int) -> int:
	return 2 + ((limb_count - 1) // 8)

def paul_mulmodmont_cost(limb_count: int) -> int:
	return 2 + (limb_count ** 2) // 8

# parse a line like:
#	BenchmarkAddMod/num_limbs=26            32510698                36.60 ns/op
# return (bench_type, num_limbs, bench_time)
def parse_go_benchmark_line(line: str) -> (str, int, float):
	m = re.match(r"Benchmark(.*)/(\d+)-bit .* (.*) ns/op.*", line)
	if m and len(m.groups()) == 3:
		result = m.group(1), int(m.group(2)), float(m.group(3))
		return result
	else:
		return None

def parse_tracefile(dataset_file: str) -> [(str, int, float)]:
	results = []
	# parse_go_benchmark_line("BenchmarkMulModMont/num_limbs=98          236150              4771 ns/op")
	with open(dataset_file) as f:
		lines = f.readlines()
		for line in lines:
			result = parse_go_benchmark_line(line)
			if result:
				results.append(result)

	return results

def create_csv(geth_trace, title, col_title):
	result = ['"{}", "{}"'.format(title, col_title)]
	for (op_name, limb_count, performance) in geth_trace:
		result.append("{}, {}".format(limb_count, performance))
	
	return "\n".join(result)

def create_and_write_csv(name, col_name, input_file, output_file):
	trace = parse_tracefile(input_file)
	csv_content = create_csv(trace, name, col_name)
	with open(output_file, 'w') as f:
		f.write(csv_content)

create_and_write_csv("addmont", "addmont-go", "raw_data/op_bench_addmont.txt", "data/op_bench_addmont.csv")
create_and_write_csv("submont", "submont-go", "raw_data/op_bench_submont.txt", "data/op_bench_submont.csv")
create_and_write_csv("mulmont", "mulmont-go", "raw_data/op_bench_mulmont.txt", "data/op_bench_mulmont.csv")

create_and_write_csv("mulmont", "mulmont-asm", "raw_data/op_bench_blstasm384_mulmont.txt", "data/op_bench_blstasm384_mulmont.csv")
create_and_write_csv("addmont", "addmont-asm", "raw_data/op_bench_blstasm384_addmont.txt", "data/op_bench_blstasm384_addmont.csv")
create_and_write_csv("submont", "submont-asm", "raw_data/op_bench_blstasm384_submont.txt", "data/op_bench_blstasm384_submont.csv")
