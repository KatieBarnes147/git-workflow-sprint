# Week 2 GRPC Project
## Running servers
docker compose up --build (only use --build if you want to rebuild the image)

# Running the Client files

## Go Client Code
## Run from within the client-examples/go-client directory


protoc --go_out=generated --go_opt=paths=source_relative \
       --go-grpc_out=generated --go-grpc_opt=paths=source_relative \
       --proto_path=../../proto \
       ../../proto/user_service.proto

go mod tidy

## Run the main.go client file
go run main.go



# Python Client Code
## Run from within the client-examples/python-client directory

## Create a virtual environment
python -m venv .venv
source .venv/bin/activate
(If you are using VSCode make sure you are using the correct python interpreter)
pip install -r requirements.txt

python -m grpc_tools.protoc \
--proto_path=../../proto \
--python_out=generated/ \
--grpc_python_out=generated/ \
../../proto/user_service.proto

## Run the python client file
python client.py


# Node Client Code
## Run from within the client-examples/nodejs-client

Run the following commands:

npm install
npm run generate

# To run the client file
npm run start