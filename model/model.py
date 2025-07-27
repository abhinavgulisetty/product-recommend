import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Flatten
from tensorflow.keras.optimizers import Adam

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'ratings.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'recommender.h5')


def build_model(num_users: int, num_products: int, embedding_size: int = 8) -> Model:
    user_input = Input(shape=(1,), name='user')
    product_input = Input(shape=(1,), name='product')

    user_embedding = Embedding(input_dim=num_users, output_dim=embedding_size, name='user_emb')(user_input)
    product_embedding = Embedding(input_dim=num_products, output_dim=embedding_size, name='product_emb')(product_input)

    dot_product = Dot(axes=-1)([user_embedding, product_embedding])
    output = Flatten()(dot_product)

    model = Model(inputs=[user_input, product_input], outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
    return model


def load_data():
    data = pd.read_csv(DATA_PATH)
    num_users = data['user_id'].max() + 1
    num_products = data['product_id'].max() + 1
    return data, num_users, num_products


def train():
    data, num_users, num_products = load_data()
    model = build_model(num_users, num_products)
    model.fit([data['user_id'], data['product_id']], data['rating'], epochs=50, verbose=0)
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == '__main__':
    train()
