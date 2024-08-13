# Face Positioning Prediction

This script uses the `PIL` library and the `landingai` package to make predictions on images using a specific endpoint. It is designed to predict the position of human faces within the images.

## Installation

Before running the script, make sure you have installed the necessary Python packages:

```bash
pip install landingai 
```
## Usage
This script processes images located in the ./images directory and sends them to a machine learning model endpoint for predictions.

## Description
The script loads images from the specified directory.

It then uses the landingai library to send these images to a machine learning model endpoint defined by the endpoint_id and api_key.

Predictions are printed for each image.

Only the first 50 images from the directory are processed.





