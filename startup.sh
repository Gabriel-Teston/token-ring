# Install or update needed software
apt-get update
apt-get install -yq git supervisor python3-pip python3-venv jq

# Fetch source code
mkdir /opt/app
git clone https://github.com/Gabriel-Teston/token-ring.git /opt/app

# Python environment setup
python3 -m venv /opt/app/env
pip3 install -r /opt/app/requirements.txt

export INSTANCE_A_ADRESS=$(sudo curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/instance_a_address" -H "Metadata-Flavor: Google")
export INSTANCE_B_ADRESS=$(sudo curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/instance_b_address" -H "Metadata-Flavor: Google")
export INSTANCE_C_ADRESS=$(sudo curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/instance_c_address" -H "Metadata-Flavor: Google")


# Start application
cd /opt/app/
flask --app=server run --host=0.0.0.0 --port=80
echo "" > sudo tee /DONE