# Service 3: gRPC Server
# This service will implement a gRPC server to receive messages from other services.

import grpc
from fastapi import FastAPI
from concurrent import futures
from grpc_stub.service3 import services_pb2
from grpc_stub.service3 import services_pb2_grpc
import asyncio

app = FastAPI()

# gRPC server class that implements the service
class CommunicationService(services_pb2_grpc.CommunicationServiceServicer):
    def sendMessage(self, request, context):
        print(f"Received gRPC message: {request.message}")
        return services_pb2.Response(message=f"Message received: {request.message}")

# Function to start the gRPC server
def start_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_CommunicationServiceServicer_to_server(CommunicationService(), server)
    server.add_insecure_port('[::]:50051')  # gRPC server listening on port 50051
    server.start()
    print("gRPC server started at port 50051")
    server.wait_for_termination()  # Keep the server running

@app.on_event("startup")
async def grpc_server_start():
    # Run the gRPC server in a separate thread to avoid blocking FastAPI
    loop = asyncio.get_event_loop() 
    loop.run_in_executor(None, start_grpc_server)