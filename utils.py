import os
from kaggle_secrets import UserSecretsClient
import ee
from openai import OpenAI

def print_hello():
    print("hello")


def load_secret(name):
    """Loads secret from Colab/Kaggle."""

    if 'KAGGLE_KERNEL_RUN_TYPE' in os.environ:
        try:
            from kaggle_secrets import UserSecretsClient
            return UserSecretsClient().get_secret(name)
        except Exception:
            pass 
    else:
        try:
            from google.colab import userdata
            return userdata.get(name)
        except Exception: 
            pass

    return 'Secret not found'

def initialize_ee():
    credentials_json = load_secret('google_ee_credentials')
    os.makedirs('/root/.config/earthengine', exist_ok=True)

    with open('/root/.config/earthengine/credentials', 'w') as f:
        f.write(credentials_json)    
    ee.Initialize(project="openaitozchallenge")

def initialize_openai():
    openai_key = load_secret('openai_key_2025')
    client = OpenAI( api_key=openai_key )
    return client