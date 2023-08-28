# API Read Me

python3 -m venv myenvapi
bash: source myenvapi/bin/activate
powershell: .\myenvapi\Scripts\Activate
pip install -r requirements.txt

python app.py


# Build the Docker image
docker build -t bookwise-api .

# Run the Docker container, mapping port 5000 on the host to port 5000 in the container
docker run -p 5000:5000 bookwise-api