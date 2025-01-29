#!/bin/bash

# Path to check for generated gRPC stubs
#GRPC_STUBS_PATH="grpc---"


# Start the FastAPI app
uvicorn main:app --host 0.0.0.0 --port 8002

# Check if gRPC stubs exist, and if so, run the gRPC server
#if [ -d "$GRPC_STUBS_PATH" ]; then
#    echo "gRPC stubs found. Starting gRPC server..."
#    python3 grpc_server.py &  # or however you start your gRPC server
#else
#    echo "No gRPC stubs found. Running only FastAPI server."
#fi

# Wait for both processes to run
#wait
