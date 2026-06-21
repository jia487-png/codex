#测试第一个全连接层
import tensorflow as tf
from tensorflow import keras
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu')
])
print('原始数据，篇幅有限，每条训练数据包含28个一维张量，我们只显示第一条训练数据的前两个一维张量：：')
print(x_train[0][0:2])
print('压平后的数据再经过全连接层，每条训练数据经过压平和全连接后，是128个标量，由于全连接层初始权值是随机数，所以未经训练的全连接层输出的也是随机数')
print(model.predict(x_train)[0])