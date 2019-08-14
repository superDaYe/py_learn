# tensorflow MNIST测试
# 忘记装 显示卡sdk了
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("D:/test", one_hot=True)

print(mnist.train.images.shape, mnist.train.labels.shape)
print(mnist.test.images.shape, mnist.test.labels.shape)
print(mnist.validation.images.shape, mnist.validation.labels.shape)
