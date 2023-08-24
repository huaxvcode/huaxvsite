import sys
from os import system
from time import time, sleep
import threading

cp_map = {
    "cpp":  "g++ -w -std=c++20 -O2 .check/{0}.cpp -o .check/{0}.out",
    "c": "gcc -w -std=c99 -O2 .check/{0}.c -o .check/{0}.out",
    "java": "javac .check/{0}.java",
    "py": ""
}

r_map = {
    "cpp": ".check/{0}.out ",
    "c": ".check/{0}.out ",
    "java": "java -cp .check {0} ",
    "py": "python3 -u .check/{0}.py "
}

def put_check(name):
    system("cp {0} .check/{0}".format(name))
    
def compiler(name, mode):
    start = time()
    t = system(cp_map[mode].format(name))
    end = time()
    if t:
        print("Compiler Error")
        exit()
    return end - start
    
def run(name, mode, end_cmd):
    cmd = "ulimit -s {} && ".format(512 * 1024) + r_map[mode].format(name) + end_cmd 
    start = time()
    system(cmd)
    end = time()
    return end - start

space = set(['\n', ' ', '\r', '\f', '\b', '\t'])

def deal_line(s):
    res = ""
    now = ""
    for c in s:
        if c in space:
            if now != "":
                res += now + ' '
            now = ""
        else:
            now += c 
    if now != "":
        res += now + ' '
    return res
        
        
def equal(o, r):
    line = 0
    with open(o, mode='r') as out, open(r, mode='r') as res:
        while True:
            line += 1
            s1 = out.readline()
            s2 = res.readline()
            if not s1 and not s2:
                return 0
            if deal_line(s1) != deal_line(s2):
                return line

def run_single(name, mode):
    system('if test -e ./out.txt; then rm ./out.txt; fi; touch ./out.txt')
    end_cmd = "<./.check/in.txt >./.check/out.txt"
    t = compiler(name, mode)
    print("cpl %.3f s" % (t, ))
    t = run(name, mode, end_cmd)
    print("run %.3f s" % (t, ))
    t = equal('./.check/out.txt', './.check/res.txt')
    if not t:
        print("Accept")
        system('cp ./.check/out.txt ./out.txt')
    else:
        print("Error in %d" % (t, ))
        system('cp ./.check/out.txt ./out.txt')

def oj(rand = 'Random', rmo = 'cpp', answer = 'Answer', amo = 'cpp', main = 'Main', mmo = 'cpp', ts = 10):
    system('if test -e ./out.txt; then rm ./out.txt; fi; touch ./out.txt')
    ths = [
        threading.Thread(target=compiler, args=(rand, rmo)),
        threading.Thread(target=compiler, args=(answer, amo)),
        threading.Thread(target=compiler, args=(main, mmo))
    ]
    start = time()
    for i in ths: i.start()
    for i in ths: i.join() # 只有所有线程都结束，循环才能终止
    end = time()
    t = end - start
    print("cpl %.3f s" % (t, ))
    print('================')
    res_t = 0
    out_t = 0
    run_ts = 0
    for i in range(ts):
        run_ts += 1
        t = run(rand, rmo, ">./.check/in.txt")
        print("Random %.3f s" % (t, ))
        t = run(answer, amo, "<./.check/in.txt >./.check/res.txt")
        print("Answer %.3f s" % (t, ))
        res_t += t
        t = run(main, mmo, "<./.check/in.txt >./.check/out.txt")
        print("Main %.3f s" % (t, ))
        out_t += t
        t = equal('./.check/out.txt', './.check/res.txt')
        if not t:
            print("Accept")
            print('================')
        else:
            # print('================')
            print("Error in %d" % (t, ))
            print('================')
            break
    if run_ts == ts:
        print('All Accept %.3f / %.3f' % (out_t / run_ts, res_t / run_ts))
    else:
        system('cp ./.check/in.txt ./in.txt')
        system('cp ./.check/out.txt ./out.txt')
        system('cp ./.check/res.txt ./res.txt')
        print('Error %.3f / %.3f' % (out_t / run_ts, res_t / run_ts))

def init():
    cmd = '''
    if test -d ".check"; then rm -r ".check"; fi; mkdir ".check"; 
    '''
    system(cmd)
    system("touch ./.check/in.txt ./.check/out.txt ./.check/res.txt")
    cmd = '''
        for i in `ls -A`; do if test "$i" != ".check"; then cp -r "$i" "./.check/$i"; fi done
    '''
    system(cmd)

def deal_name(name):
    n = len(name)
    m = -1;
    for i in range(n - 1, -1, -1):
        if name[i] == '.':
            m = i
            break
    if m == -1 or m >= n - 1 or name[m + 1:] not in cp_map:
        print("Can not run")
        exit()
    return [name[:m], name[m + 1:]]

if __name__ == '__main__':
    init()
    args = list(sys.argv)[1:]
    argn = len(args)
    if argn == 0:
        oj()
    elif argn == 1:
        if args[0].isdigit():
            oj(ts=int(args[0]))
        else:
            run_single(*deal_name(args[0]))    
    elif argn == 3:
        ln = []
        for i in args:
            ln += deal_name(i)
        oj(*ln)
    elif argn == 4:
        ln = []
        for i in args[:-1]:
            ln += deal_name(i)
        oj(*ln, int(args[-1]))