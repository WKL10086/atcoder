AOC_TARGET = adventofcode/2022

# Ready adventofcode files
ready:
	cp -i adventofcode/template/day.py $(AOC_TARGET)/day$(day).py
	cp -i adventofcode/template/day.txt $(AOC_TARGET)/day$(day).txt

# Run adventofcode file
run:
	cd $(AOC_TARGET) && python3 day$(day).py

test:
	cd adventofcode/template && python3 init.py