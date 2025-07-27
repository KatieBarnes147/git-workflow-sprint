import grpc
import sys
import os

# Add the generated directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'generated'))

import user_service_pb2
import user_service_pb2_grpc

def run():
    # Create a gRPC channel
    with grpc.insecure_channel('localhost:50053') as channel:
        # Create a stub (client)
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        
        # Test GetUser
        try:
            get_user_response = stub.GetUser(user_service_pb2.GetUserRequest(user_id=1))
            print(f"GetUser response: {get_user_response}")
        except grpc.RpcError as e:
            print(f"GetUser error: {e}")
        
        # Test ListUsers
        try:
            list_users_response = stub.ListUsers(user_service_pb2.ListUsersRequest(page=1, page_size=10))
            print(f"ListUsers response: {list_users_response}")
        except grpc.RpcError as e:
            print(f"ListUsers error: {e}")
        
        # Test CreateUser
        try:
            create_user_response = stub.CreateUser(user_service_pb2.CreateUserRequest(
                name="Charlie Brown",
                email="charlie@example.com",
                age=26
            ))
            print(f"CreateUser response: {create_user_response}")
        except grpc.RpcError as e:
            print(f"CreateUser error: {e}")

if __name__ == '__main__':
    run()

