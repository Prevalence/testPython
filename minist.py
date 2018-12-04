# -*- coding: utf-8 -*-
import tensorflow as tf
# 下载input_data.py源代码,运行然后下载数据集
from tensorflow.examples.tutorials.mnist import input_data
#做一下修改，再修改
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
# 放置占位符
x = tf.placeholder("float", [None, 784])
# 创建两个变量
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# 使用TensorFlow自带的softmax回归线性模型
y = tf.nn.softmax(tf.matmul(x, w) + b)
# 为了进行训练，需要把正确值一并传入网络
y_ = tf.placeholder("float", [None, 10])
# 计算交叉墒
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# 使用梯度下降算法以0.01的学习率最小化交叉墒
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
# 初始化之前创建的变量的操作
init = tf.initialize_all_variables()
# 启动初始化
sess = tf.Session()
sess.run(init)
# 开始训练模型，循环1000次，每次都会随机抓取训练数据中的100条数据，然后作为参数替换之前的占位符来进行train_step
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
# 评估模型，tf.argmax能给出某个tensor对象在某一纬度上数据的最大索引，因为标签是由0,1组成，返回的索引就是数值为1的位置
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 计算正确预测项的比例，因为tf.equal返回的是布尔值,相等表示真，真的用ture,假的用false，使用tf.cast可以把布尔值转换成浮点数，tf.reduce_mean是求平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# 在session中启动accuracy，输入是MNIST中的测试集
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
