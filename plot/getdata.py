import subprocess
import time
import signal
import datetime
time_before_launch = time.time()
howlong = 60*60
p = subprocess.Popen(["ping", "-D", "-c 100", "vg.no"], stdout=subprocess.PIPE,)
print("## Process: {} \t Scheduled to run for {} seconds ## ".format(p.pid,howlong))
# print "Process ID of subprocess %s" % p.pid

elapsed = int(time.time()-time_before_launch)
while(elapsed != howlong):
    elapsed = int(time.time()-time_before_launch)
    if(elapsed==howlong):
        print("been waiting for {}".format(howlong))

# Send SIGTER (on Linux)
p.send_signal(signal.SIGINT)
# p.communicate()
# Wait for process to terminate
returncode = p.wait()

x = p.communicate()[0].split('\n')

writefile = open('log','w')
for f in x:
    d = f.split(' ')
    # print(d)
    if d[0].startswith('['):
        val = d[0][1:len(d[0])-1]
        t = datetime.datetime.fromtimestamp(
        float(val)).strftime('%d-%m-%Y %H:%M:%S')
        print("{} \t {} {}".format(t,d[4], d[8]))
        # writefile.write("{} \t {} \t {} \n".format(t,d[4], d[8].split('=')[1]))
        writefile.write("{} \t {} \n".format(t,d[8].split('=')[1]))
    else:
        print(f)
writefile.close()
import test
