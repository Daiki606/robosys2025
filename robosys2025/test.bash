#!/bin/bash
set -e

ros2 launch mypkg talk_listen.launch.py > test_output.log 2>&1 &
LAUNCH_PID=$!

sleep 5

kill $LAUNCH_PID

if grep -q "Listen" test_output.log; then
    echo "Test PASS"
    exit 0
else
    echo "Test FAIL"
    exit 1
fi

