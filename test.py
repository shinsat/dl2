import tensorflow as tf

a = tf.constant(120, name='a')
b = tf.constant(130, name='b')
c = tf.constant(140, name='c')
v = tf.Variable(0, name = 'v')

calc_op = a + b + c
assign_op = tf.assign(v, calc_op)
sess = tf.Session()
sess.run(assign_op)
print(sess.run(v))

aa = tf.placeholder(tf.int32, [3])
b = tf.constant(2)
x2_op = a * b
sesss = tf.Session()

r1 = sesss.run(x2_op, feed_dict={ aa:[1,2,3] })
print(r1)
r2 = sesss.run(x2_op, feed_dict={ aa:[10,20,10] })
print(r2)