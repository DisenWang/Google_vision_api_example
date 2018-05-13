# About
This repo is a demo using google vision api to analyze images.

The input should be a csv file listing all images and a folder containing images to be analyzed:
![input](https://pbs.twimg.com/media/DXuniLzVAAA3k_Z.jpg)

The output should be an updated csv file with a new column added - "labels":
![output](https://pbs.twimg.com/media/DXunTq6VoAAWB1j.jpg)

Taking one of the sample images as an example, for this image:
![sample_image](https://pbs.twimg.com/media/DXupS0hU8AE6ay3.jpg)

the detected labels are:['furniture', 'dining room', 'table', 'property', 'room', 'chair', 'interior design', 'floor', 'flooring', 'kitchen & dining room table']

# Before you begin
Please make sure you have a google cloud account and set up a payment method. You can set it up here: https://cloud.google.com

After register, log in to your console:https://console.cloud.google.com, create a project and enable your api:https://cloud.google.com/vision/docs/before-you-begin


# Setup
Because we will call google api locally, first we need to install google cloud sdk.

Enter the following at terminal: `curl https://sdk.cloud.google.com | bash`

Restart terminal and enter: `exec -l $SHELL`

Run gcloud init to initialize the gcloud environment:`gcloud init` You will need to log in your google account. Choose the project you just created.

Install Auth components: `gcloud beta auth application-default login` and create a service account: https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount After this you will have a .json file downloaded, for example I save it as `~/visiontesting.json`

Set environment variables: `export GOOGLE_APPLICATION_CREDENTIALS=~/visiontesting.json  `

# About Python
Google cloud sdk uses Python 2.7, so this demo will also use Python 2.7. Make sure that Python 2.7 is installed on your system:`python -V`

If you have not installed Python yet, please install Python 2.7:https://www.python.org/downloads/

# Run


* Create virtual environment: `$virtualenv venv`

* Activate virtual env: `$source venv/bin/activate`

* install required packages:`pip install -r requirements.txt`

* Run demo: `python label_add.py`

If you meet with error "No module named 'google.cloud'", try to use: `pip install --upgrade google-cloud` and it should work.
