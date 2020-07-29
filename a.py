#%%
import matplotlib.pyplot as plt
import numpy as np

alldat = np.array([])
for j in range(3):
    alldat = np.hstack((alldat, np.load('steinmetz_part%d.npz' % j, allow_pickle=True)['dat']))
print('Data has loaded')
#%%function defination

class a:
    def show_singel_neuron_trial_spike(ca1_spike_time):
            for i in range(50):
                plt.axvline(i, 0, 2500, color="black", linestyle='--', alpha=0.2)
                for j in range(250):
                    if ca1_spike_time[i, j] == 0:
                        continue
                    plt.scatter(i, ca1_spike_time[i, j], s=np.pi * 2 ** 2)
            plt.xlabel('trial')
            plt.ylabel('spike time')
            plt.savefig('trial.png')
            plt.show()

    def get_data(self):

            dat = alldat[self.mouse_id]
            area = dat['brain_area']
            spks = dat['spks']

            ca1 = np.argwhere(area == 'CA1')
            ca3 = np.argwhere(area == 'CA3')
            dg = np.argwhere(area == 'DG')

            ca1_spike_time = np.zeros((spks.shape[1], spks.shape[2]))
            ca3_spike_time = np.zeros((spks.shape[1], spks.shape[2]))
            dg_spike_time = np.zeros((spks.shape[1], spks.shape[2]))
            area_name = {0:'ca1', 1:'ca3', 2:'dg'}
            spike_time_matrix_name = {0:'ca1_spike_time', 1:'ca3_spike_time', 2:'dg_spike_time'}
            neuron_id = {0: self.ca1_neuron_id, 1: self.ca3_neuron_id, 2: self.dg_neuron_id}

            for num, current_area in enumerate([ca1, ca3, dg]):
                current_area_name = locals()[area_name[num]]
                current_area_matrix = locals()[spike_time_matrix_name[num]]
                for i in range(spks.shape[1]):  #trial
                    for j in range(spks.shape[2]):  #spike
                        if spks[current_area_name[neuron_id[num]], i, j] != 0:
                            current_area_matrix[i, j] = (10 * j)
                        else:
                            current_area_matrix[i, j] = 0
                print('From mouse', self.mouse_id, ', in', area_name[num], ', neuron ', neuron_id[num] )
                print(spike_time_matrix_name[num],'has generated.', )
            return ca1_spike_time, ca3_spike_time, dg_spike_time

    def change_spike_matrix_2_1d(self, matrix):
        m1d = matrix.ravel()
        for i in range(len(m1d)):
            if m1d[i] != 0:
                m1d[i] = i * 10
        print('Matrix has transformed to 1d')
        return m1d

    def loda_data(self):
        for j in range(3):
            self.alldat = np.hstack((self.alldat, np.load('steinmetz_part%d.npz' % j, allow_pickle=True)['dat']))
        print('Data has loaded')

    def __init__(self, mouse_id=7, ca1_neuron_id=0, ca3_neuron_id=0, dg_neuron_id=0):
        self.mouse_id = mouse_id
        self.ca1_neuron_id = ca1_neuron_id
        self.ca3_neuron_id = ca3_neuron_id
        self.dg_neuron_id = dg_neuron_id

    def get_save(self):
        ca1_spike_time, ca3_spike_time, dg_spike_time = self.get_data()
        ca1_spike_time_1d = self.change_spike_matrix_2_1d(ca1_spike_time)
        ca3_spike_time_1d = self.change_spike_matrix_2_1d(ca3_spike_time)
        dg_spike_time_1d = self.change_spike_matrix_2_1d(dg_spike_time)
        for i, a in enumerate(['ca1_spike_time_1d', 'ca3_spike_time_1d', 'dg_spike_time_1d']):
            a = filter(lambda x: x != 0, locals()[a])
            a = list(a)
            np.savetxt('./GLMCC/datasets/cell' + str(i + 1) + '.txt', a, fmt="%.2f")

    def main(self):
        # check which data can be used
        for i in range(39):
            dat = alldat[i]

            spike = dat['spks']
            area = dat['brain_area']
            # print(len(dat['mouse_name']))

            ca1 = np.argwhere(area == 'CA1')
            ca3 = np.argwhere(area == 'CA3')
            dg = np.argwhere(area == 'DG')
            # print(area)
            # print(np.shape(area))
            # print(np.shape(ca3))
            if np.shape(ca3) != (0, 1) and np.shape(ca1) != (0, 1) and np.shape(dg) != (0, 1):
                print(i)

        # get spike array
        mouse_id = 7

        ca1_spike_time, ca3_spike_time, dg_spike_time = self.get_data()
        # show_singel_neuron_trial_spike(ca1_spike_time)
        ca1_spike_time_1d = self.change_spike_matrix_2_1d(ca1_spike_time)
        ca3_spike_time_1d = self.change_spike_matrix_2_1d(ca3_spike_time)
        dg_spike_time_1d = self.change_spike_matrix_2_1d(dg_spike_time)

        # save spike array to GLMCC fold
        for i, a in enumerate(['ca1_spike_time_1d', 'ca3_spike_time_1d', 'dg_spike_time_1d']):
            a = filter(lambda x: x != 0, locals()[a])
            a = list(a)
            np.savetxt('./GLMCC/datasets/cell' + str(i + 1) + '.txt', a, fmt="%.2f")


#%%
if __name__ == '__main__':
   ins = a()
   ins.main()