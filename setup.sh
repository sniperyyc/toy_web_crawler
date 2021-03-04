# THIS SCRIPT IS CREATED FOR LINUX
# TESTED ON UBUNTU 18.04

# install latest stable Chrome version
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

# install Chrome driver
wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

# install selenium
pip3 install selenium