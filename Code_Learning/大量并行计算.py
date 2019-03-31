import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from ipyparallel import Client
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='saturnman'),bitrate=2400)
fig = plt.figure()


DPI = fig.get_dpi()
fig.set_size_inches(2048.0/float(DPI),1280.0/float(DPI))

ITERATIONS = 250
#SIZE = lena.shape[0]
#注意:此参数会极大影响计算过程的内存消耗，对于小内存机器可以会让计算进程因内存不够而出错，请自行调节计算
SIZE = 1024
MAX_COLOR = 255.

x_min, x_max = -2.5, 1
y_min, y_max = -1.2, 1.2

xt_min, xt_max = -0.748746707922161, -0.748746697771757
yt_min, yt_max = 0.123640844894862, 0.123640851045266

xt_mid = (xt_min+xt_max)/2
yt_mid = (yt_min+yt_max)/2

x_mid = (x_min+x_max)/2
y_mid = (y_min+y_max)/2



iter = 1
#x_min, x_max = x-width/2, x+width/2
#y_min, y_max = y-height/2, y+height/2
x,y = numpy.meshgrid(numpy.linspace(x_min,x_max,2*SIZE),numpy.linspace(y_min,y_max,SIZE));
c = x + 1j*y
z = c.copy()
fractal = numpy.zeros(z.shape,dtype=numpy.uint8)+MAX_COLOR
#
#for n in range(ITERATIONS):
#    mask = numpy.abs(z) <=10
#    z[mask] = z[mask]**2+c[mask]
#    fractal[(fractal==MAX_COLOR) & (~mask)] = (MAX_COLOR-1)*n/ITERATIONS
# Display the fractal


def compute_frac(iter):
    
    ITERATIONS = 250
    SIZE = 256
    MAX_COLOR = 255.

    x_min, x_max = -2.,2.
    y_min, y_max = -1.2, 1.2

    #x_min, x_max = 0.5, 2.2
    #y_min, y_max = -0.3, 0.3

    xt_min, xt_max = -0.748766707922161, -0.748766697771757
    yt_min, yt_max = 0.128640844894862, 0.128640851045266

    xt_mid = (xt_min+xt_max)/2
    yt_mid = (yt_min+yt_max)/2

    x_mid = (x_min+x_max)/2
    y_mid = (y_min+y_max)/2

    scale = 1.0/((1.0+(iter*iter+iter*iter*iter*0.01)*0.0001)/2.0)
    width = (x_max-x_min)*scale
    height = (y_max-y_min)*scale
    x_mid_tmp = xt_mid + (x_mid-xt_mid)*scale
    y_mid_tmp = yt_mid + (y_mid-yt_mid)*scale

    x_min_tmp = x_mid_tmp-width/2
    x_max_tmp = x_mid_tmp+width/2
    y_min_tmp = y_mid_tmp-height/2
    y_max_tmp = y_mid_tmp+height/2

    box = numpy.zeros(6,numpy.float64)
    box[0] = x_min
    box[1] = x_max
    box[2] = y_min
    box[3] = y_max
    box[4] = -0.67 - (iter)*0.0002
    box[5] = 0.11 

    #print box
    block_size = 64

    x,y = numpy.meshgrid(numpy.linspace(x_min_tmp,x_max_tmp,2*SIZE),numpy.linspace(y_min_tmp,y_max_tmp,SIZE));
    c = x + 1j*y
    z = c.copy()
    frac = numpy.zeros(z.shape,numpy.uint8)+MAX_COLOR
    for n in range(ITERATIONS):
        mask = numpy.abs(z) <= 10
        z[mask] = z[mask]**2+c[mask]
        frac[(frac==MAX_COLOR) & (~mask)] = (MAX_COLOR-1)*n/ITERATIONS
    return frac
frac = compute_frac(1.0)
matplotlib.pyplot.axis('off')
im = plt.imshow(frac,cmap=plt.get_cmap('flag'))
def updatefig(looper):
    global frac_list
    im.set_data(frac_list[looper])
    return im,
c = Client()
v = c[:]
frac_list = v.map_sync(compute_frac,[d for d in numpy.arange(1,801)])

ani = animation.FuncAnimation(fig,updatefig,range(0,800),interval=100, blit=True)
ani.save('parallel_frac.mp4', writer=writer)