AOC_TARGET = adventofcode/2022

# Run adventofcode file
run:
	cd $(AOC_TARGET) && python3 day$(d).py

# Init adventofcode file
init:
	cd adventofcode/init && python3 init.py