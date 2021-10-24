echo "Run help";
time Task2/code/cmake-build-debug/homework_1;

echo "\nRun test #0"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test00.txt /Programming/Architecture/Task2/tests/out00_1.txt /Programming/Architecture/Task2/tests/out00_2.txt

echo "\nRun test #1"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test01.txt /Programming/Architecture/Task2/tests/out01_1.txt /Programming/Architecture/Task2/tests/out01_2.txt

echo "\nRun test #2"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test02.txt /Programming/Architecture/Task2/tests/out02_1.txt /Programming/Architecture/Task2/tests/out02_2.txt

echo "\nRun test #3"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test03.txt /Programming/Architecture/Task2/tests/out03_1.txt /Programming/Architecture/Task2/tests/out03_2.txt

echo "\nRun test #4"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test04.txt /Programming/Architecture/Task2/tests/out04_1.txt /Programming/Architecture/Task2/tests/out04_2.txt

echo "\nRun test #5"
time Task2/code/cmake-build-debug/homework_1 -f /Programming/Architecture/Task2/tests/test05.txt /Programming/Architecture/Task2/tests/out05_1.txt /Programming/Architecture/Task2/tests/out05_2.txt

echo "\nRun test #6 (random)"
time Task2/code/cmake-build-debug/homework_1 -n 10000 /Programming/Architecture/Task2/tests/outrnd_1.txt /Programming/Architecture/Task2/tests/outrnd_2.txt
