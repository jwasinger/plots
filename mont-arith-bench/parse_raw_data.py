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
	m = re.match(r"Benchmark(.*)/.*=(\d+) .* (.*) ns/op", line)
	if m and len(m.groups()) == 3:
		result = m.group(1), int(m.group(2)), float(m.group(3))
		return result
	else:
		return None

def parse_dataset(dataset_file: str) -> [(str, int, float)]:
	results = []
	# parse_go_benchmark_line("BenchmarkMulModMont/num_limbs=98          236150              4771 ns/op")
	with open(dataset_file) as f:
		lines = f.readlines()
		for line in lines:
			result = parse_go_benchmark_line(line)
			if result:
				results.append(result)

	return results

def create_addmod_large_csv():
	title = '"Modular Addition", "mont-arith", "model"'
	result = [title]
	addmod_dataset = parse_dataset('raw_data/mont_arith_addmod.txt')
	for (op_name, limb_count, performance) in addmod_dataset:
		performance_gas = round(performance / 10)
		result.append("{}, {}, {}".format(limb_count, performance_gas, paul_addmod_submod_cost(limb_count)))
	
	return "\n".join(result)

def create_mulmod_large_csv():
	title = '"Montgomery Modular Multiplication", "mont-arith", "model"'
	result = [title]
	addmod_dataset = parse_dataset('raw_data/mont_arith_mulmodmont.txt')
	for (op_name, limb_count, performance) in addmod_dataset:
		performance_gas = round(performance / 10)
		result.append("{}, {}, {}".format(limb_count, performance_gas, paul_mulmodmont_cost(limb_count)))
	
	return "\n".join(result)
	
# 4 column graph dataset
# index | op_cost | paul_model_cost | geth_opcode_cost | blst_asm_opcode_cost
def format_csv():
	pass

addmod_csv = create_addmod_large_csv()

with open("addmod.csv", "w") as f:
	f.write(addmod_csv)

mulmodmont_csv = create_mulmod_large_csv()
with open("mulmodmont.csv", "w") as f:
	f.write(mulmodmont_csv)
