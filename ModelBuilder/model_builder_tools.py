import Keras
from keras.models import Model
from keras.layers import Dense, Dropout

"Load the Inception Base Model from the Keras Library"
def load_base_model(img_size):
    input_shape = (img_size, img_size, 3)
    model = keras.applications.inception_v3.InceptionV3(weights='imagenet', include_top=False)
    return model
    
"Add Transfer Learning Layers"
def create_model(img_size):
    dropout_rate = 0.5
    base_model   = load_base_model(img_size)  
    model = Model() 
    model.add(Dense(base_model[-1].shape(), output_shape=base_model[-1].shape() // 2))
    model.add(Dropout(dropout_rate))
    model.add(Dense(base_model[-1].shape // 2, output_shape=base_model.shape() // 2))
    model.add(Dropout(dropout_rate))
    model = model.compile()
    return model