#测试压平层Flatten
import tensorflow as tf
from tensorflow import keras
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28))
])
print('原始数据，篇幅有限，每条训练数据包含28个一维张量，我们只显示第一条训练数据的前两个一维张量：')
print(x_train[0][0:2])
print('压平后的数据，篇幅有限，每条训练数据压平后是一个包含784个标量的一维张量，我们只显示前56个:')
print(model.predict(x_train)[0][0:56])
