from qsp_opt import QSP
import sys
import numpy as np
from matplotlib import pyplot as plt
import pickle

# example run:
model = QSP(argv = sys.argv)#, quick_check=True, verbose=False)
model.run()
exit()87

samples_f = []
n_step = model.parameters['n_step']
T = model.parameters['T']
L = model.parameters['L']
fname = 'fidelitySamples_L=%i_T=%.2f_nStep=%i.pkl'%(L, T, n_step)

for i in range(1000000):
    if i%10000 == 0:
        print(i)
    p = model.random_protocol()
    samples_f.append(model.evaluate_protocol(p))

fwrite = open(fname,'wb')
pickle.dump(samples_f, fwrite) 

exit()
hist_info = []
for n_step in [50,100,200,400,800]:
    fname = 'fidelitySamples_L=%i_T=%.2f_nStep=%i.pkl'%(L, T, n_step)

    fread = open(fname,'rb')
    samples_f = pickle.load(fread)

    n_sample = len(samples_f)
    hist_y, hist_x, _ = plt.hist(samples_f,bins=80)
    mid_x = [0.5*(hist_x[i+1]+hist_x[i]) for i in range(len(hist_x)-1)]
    hist_info.append([mid_x,np.log(hist_y*(1/n_sample))])
    ''' plt.clf()
    plt.scatter(mid_x, np.log(hist_y*(1/n_sample)))
    '''

#print(hist_info)

plt.clf()
for i, n_step in enumerate([50,100,200,400,800]):
    plt.scatter(hist_info[i][0],hist_info[i][1],label='$N=%i$'%n_step)

plt.legend()
plt.show()
exit()
plt.show()
exit()
model.run()
exit()
np.random.seed(0)
p = model.random_protocol()
print(p)
f=model.evaluate_protocol(p)
print(f)
print('------')
p2 = model.flip(p,0)
print(model.evaluate_protocol(p2))
print(p2)
print('------')
p3 = model.flip(p2,2)
print(model.evaluate_protocol(p3))
print(p3)
print('--------')
p4 = model.flip(p3,5)
print(model.evaluate_protocol(p4))
print(p4)
print('--------')
p5 = model.flip(p4,6)
print(model.evaluate_protocol(p5))
print(p5)
print('--------')
