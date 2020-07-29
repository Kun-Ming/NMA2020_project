import a
import os
from GLMCC import glmplot as glm
#%%
def run(PLOT_TARGET_ID = 3, PLOT_REFERENCE_ID = 1, mouse_id=7, ca3_neuron_id=1, ca1_neuron_id=2, dg_neuron_id=3):
    ins = a.a(mouse_id=7, ca3_neuron_id=1, ca1_neuron_id=2, dg_neuron_id=3)

    ins.get_save()
    print('---------------------------')

    bool = glm.glm_plot(data_dir='./GLMCC/datasets/', prefix=glm.params.PREFIX, extension=glm.params.EXTENSION,
             target_id=PLOT_TARGET_ID, reference_id=PLOT_REFERENCE_ID, save_dir='./GLMCC/results/',
             start=glm.params.START, end=glm.params.END, window=glm.params.WINDOW, synaptic_delay=glm.params.SYNAPTIC_DELAY)
    if bool:
        f = open('./GLMCC/results/result.txt', 'a+')
        s = '*****PLOT_REFERENCE_ID='+str(PLOT_REFERENCE_ID)+', PLOT_TARGET_ID='+str(PLOT_TARGET_ID)+', mouse_id='+str(mouse_id)+', ca3_neuron_id='+str(ca3_neuron_id) \
              + ', ca1_neuron_id=' + str(ca1_neuron_id)+', dg_neuron_id='+str(dg_neuron_id)+'*****\n'
        f.write(s)
        print('Write to result.txt successfully')
        f.close()

#%%
for i in range(1):
    run(mouse_id=7, ca3_neuron_id=1, ca1_neuron_id=2, dg_neuron_id=3)