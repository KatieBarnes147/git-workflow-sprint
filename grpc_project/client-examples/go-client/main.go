package main

import (
	"context"
	"log"
	"time"

	pb "grpc-go-client/generated"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	// Connect to the server using the new NewClient method
	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("Failed to connect: %v", err)
	}
	defer conn.Close()

	// Create a client
	client := pb.NewUserServiceClient(conn)

	// Create a context with timeout (increased for better reliability)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	log.Println("Testing gRPC client...")

	// Test GetUser
	log.Println("Testing GetUser...")
	getUserResp, err := client.GetUser(ctx, &pb.GetUserRequest{UserId: 1})
	if err != nil {
		log.Fatalf("GetUser failed: %v", err)
	}
	log.Printf("GetUser response: %+v", getUserResp)

	// Test ListUsers
	log.Println("Testing ListUsers...")
	listUsersResp, err := client.ListUsers(ctx, &pb.ListUsersRequest{Page: 1, PageSize: 10})
	if err != nil {
		log.Fatalf("ListUsers failed: %v", err)
	}
	log.Printf("ListUsers response: %+v", listUsersResp)

	// Test CreateUser
	log.Println("Testing CreateUser...")
	createUserResp, err := client.CreateUser(ctx, &pb.CreateUserRequest{
		Name:  "Alice Johnson",
		Email: "alice@example.com",
		Age:   28,
	})
	if err != nil {
		log.Fatalf("CreateUser failed: %v", err)
	}
	log.Printf("CreateUser response: %+v", createUserResp)

	log.Println("All tests completed successfully!")
}
