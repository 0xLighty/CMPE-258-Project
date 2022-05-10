# CMPE 258 Project - Image Captioning Using CNN

### Steps to run GUI on a local machine. <br>
1. Download zip folder and locate 'gui.py' python  file. <br>
2. Make sure that 'tokenizer.p' is located in the data folder and 'model_29.h5' under Models folder <br>
3. Run the gui.py file <br>
4. Choose the image to evaluate the model and GUI.

### Steps to run Image Captioning.ipynb on local machine: <br>
1. Open notebook file in Jupyter or Google Colab. <br>
2. Run the following sections to build the model: 
<ul style="list-style-type:disc;">
  <li>Download data - Downloads the dataset and unzips.</li>
  <li>Import Libraries - Imports required libraries and tools</li>
  <li>Cleaning Captions - For preprocessing descripitons.</li>
  <li>Feature extraction - Extracts features from images using Xception Model. (Run this to extract features)</li>
  <li>(Optional) Loading Saved Features - Load the saved features if already extracted. </li>
  <li>Building Vocabulary - Tokenizing  the captions.</li>
</ul>  

### Build, Train and Evaluate Mode: Run this for implementing data generator, building model, training and evaluating. 
### Demo: Run this section for model demo. Change tokenizer, model and validation data path. Run section 1 to make sure Flicker8k_Dataset is downloaded to the root directory for testing Validation images. (Or enter new image path for predicting captions)
