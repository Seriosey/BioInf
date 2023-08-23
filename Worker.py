import os

file_name = str(input())
valid_files = []
workers = {}
expl_duration = {}

def Check(worker):
    if worker[4].count(worker[4][0]) != len(worker[4]):
        if worker[1] in workers:
            workers[worker[1]] += 1
        else:
            workers[worker[1]] = 1
        if worker[3] in expl_duration:
            if worker[2] in expl_duration[worker[3]]:
                expl_duration[worker[3]][worker[2]] += 1
            else:
                expl_duration[worker[3]][worker[2]] = 1
        else:
            expl_duration[worker[3]] = { worker[2]:1 }
    return


def file_search(dir):
    files = os.listdir(dir)
    for path in files:
        if '.' in path:
            if path.endswith('.txt'):
                valid_files.append(dir + '/' + path)
        else:
            file_search(dir+'/'+path)

file_search(file_name)


for file_name in valid_files:
    f = open(file_name)
    list_lines = f.readlines()
    if (len(list_lines) < 53 ):
        for line in list_lines[1:]:
            worker = line.strip('\n').split('\t')
            Check(worker)
    f.close

expl_duration = sorted(expl_duration.items(), key = lambda x: x[0])
for (machine, hours) in expl_duration:
    peak_load = max(hours.items(), key=lambda p: p[1])
    print(machine + ':' + peak_load[0])

best_worker = max(workers.items(), key = lambda p: p[1])
print(best_worker[0] + ':' + str(best_worker[1]))




