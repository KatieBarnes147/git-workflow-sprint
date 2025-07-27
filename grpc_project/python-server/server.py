from concurrent import futures
import grpc
import time
import sys
import os

# Add proto folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../proto'))
import user_service_pb2
import user_service_pb2_grpc

class UserService(user_service_pb2_grpc.UserServiceServicer):

    def ValidateCoordinates(self, request, context):
        is_valid = -90 <= request.latitude <= 90 and -180 <= request.longitude <= 180
        return user_service_pb2.ValidationResponse(is_valid=is_valid)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC Python server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
