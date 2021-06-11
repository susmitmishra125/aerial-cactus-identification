import tensorflow as tf
model = tf.keras.models.load_model('model_epoch_30.h5')
IMAGE_SIZE = 224
# BATCH_SIZE = 32
def _parse_fn_test(filename):
	image_string = tf.io.read_file(filename)
	image_decoded = tf.image.decode_jpeg(image_string)
	image_normalized = (tf.cast(image_decoded, tf.float32)/127.5) - 1
	image_resized = tf.image.resize(image_normalized, (IMAGE_SIZE, IMAGE_SIZE))
	return image_resized

def getPrediction(filename):
	input=tf.data.Dataset.from_tensor_slices(tf.constant([filename]))
	input=(input.map(_parse_fn_test).batch((1)))
	pred=model.predict(input)
	return "The Probability of the image being a cactus image is: "+str(round(pred[0][0],3))
