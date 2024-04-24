import os
import re


class valve:
    def __init__(self, name, flow_rate, connections, state=False):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections
        self.state = state


test_data = True
puzzle_input = open(os.path.dirname(__file__)+"/day_16_test_data.txt").readlines() if test_data else open(os.path.dirname(__file__)+"/day_16_data.txt").readlines()

valve_list = []
for line in puzzle_input:
    results = re.search(r"Valve (..) has flow rate=(\d+); tunnels lead to valves (.*)", line)
    valve_list.append(valve(results[1], results[2], results[3]))
