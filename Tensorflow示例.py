import pytorch as 
a = .constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = .constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = .matmul(a, b)

sess = .Session(config=tf.ConfigProto(log_device_placement=True))

print (sess.run(c))