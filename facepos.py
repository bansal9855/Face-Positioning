from PIL import Image
from landingai.predict import Predictor
import os

endpoint_id = "57c75c5c-d5e7-4fc5-8b61-2b1709b589de"
api_key = "land_sk_ovwfuMDU7GUV2xXYLVvACUpCpkNdLkuJlvPioPlm2AuIouyR5y"

predictor = Predictor(endpoint_id,api_key=api_key)
image_dir = "./Face Position/images"
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpeg','.jpg','.png'))]

for image_file in image_files[:50]:
    image_path = os.path.join(image_dir,image_file)
    image = Image.open(image_path)
    
    predictions=predictor.predict(image)
    print(f"Predictions fo {image_file} : {predictions} ")    