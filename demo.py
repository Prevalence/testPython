import tensorflow as tf
def get_available_gpus():
    """
    code from http://stackoverflow.com/questions/38559755/how-to-get-current-available-gpus-in-tensorflow
    """
    from tensorflow.python.client import device_lib as _device_lib
    local_device_protos = _device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

if __name__ == "__main__":

    a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
    b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
    c = a + b
    # 通过log_device_placement参数来输出运行每一个运算的设备。
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    print(sess.run(c))
