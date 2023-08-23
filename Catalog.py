import os

root_name = str(input())
list_valid_file = []

def find_file(dir_name):
    files = os.listdir(dir_name)
    for path in files:
        if '.' in path:
            if path.endswith('.txt'):
                list_valid_file.append(dir_name + '/' + path)
        else:
            find_file(dir_name+'/'+path)

find_file(root_name)

worker_list = {}
machine_time = {}

def workerCheck(worker):
    if worker[4].count(worker[4][0]) != len(worker[4]):
        if worker[1] in worker_list:
            worker_list[worker[1]] += 1
        else:
            worker_list[worker[1]] = 1
        if worker[3] in machine_time:
            if worker[2] in machine_time[worker[3]]:
                machine_time[worker[3]][worker[2]] += 1
            else:
                machine_time[worker[3]][worker[2]] = 1
        else:
            machine_time[worker[3]] = { worker[2]:1 }
    return

for path in list_valid_file:
    f = open(path)
    list_lines = f.readlines()
    if (len(list_lines) < 53 ):
        for line in list_lines[1:]:
            worker = line.strip('\n').split('\t')
            workerCheck(worker)
    f.close

machine_time = sorted(machine_time.items(), key = lambda x: x[0])
for (machine, hours) in machine_time:
    peak_load = max(hours.items(), key=lambda p: p[1])
    print(machine + ':' + peak_load[0])

best_worker = max(worker_list.items(), key = lambda p: p[1])
print(best_worker[0] + ':' + str(best_worker[1]))
