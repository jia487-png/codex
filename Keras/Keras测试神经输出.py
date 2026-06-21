#测试训练前后的神经网络输出
import graphviz
import tensorflow as tf
from tensorflow import keras
import json
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
print('训练前的神经网络对第一条训练数据的预测：')
print(model.predict(x_train)[0])
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
print('训练后的神经网络对第一条训练数据的预测：')
print(model.predict(x_train)[0])

print('\n模型结构：')
model.summary()
print(f'\n输入形状: {model.input_shape}')
print(f'输出形状: {model.output_shape}')
print(f'参数量: {model.count_params():,}')
print(f'\n各层配置:')
for i, layer in enumerate(model.layers):
    print(f'  [{i}] {layer.name} ({layer.__class__.__name__})')
    if hasattr(layer, 'input_shape') and layer.input_shape:
        print(f'      输入: {layer.input_shape}')
    if hasattr(layer, 'output_shape') and layer.output_shape:
        print(f'      输出: {layer.output_shape}')
    if hasattr(layer, 'units'):
        print(f'      神经元: {layer.units}')

try:
   # keras.utils.plot_model(model, "模型结构图.png", show_shapes=True)
    print('\n模型结构图已保存到 模型结构图.png')
except ImportError:
    print('\n[提示] graphviz 未安装，无法生成图片。可手动下载安装:')
    print('  https://graphviz.gitlab.io/download/')
    print('  或: pip install graphviz')
except Exception as e:
    print(f'\n[提示] 生成模型图片失败: {e}')
