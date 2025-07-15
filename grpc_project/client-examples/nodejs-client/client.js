const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

// Load the proto file
const PROTO_PATH = path.join(__dirname, "../../proto", "user_service.proto");
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const userServiceProto =
  grpc.loadPackageDefinition(packageDefinition).user_service;

function main() {
  // Create a client
  const client = new userServiceProto.UserService(
    "localhost:50052",
    grpc.credentials.createInsecure()
  );

  // Test GetUser
  client.getUser({ user_id: 1 }, (error, response) => {
    if (error) {
      console.error("GetUser error:", error);
    } else {
      console.log("GetUser response:", response);
    }
  });

  // Test ListUsers
  client.listUsers({ page: 1, page_size: 10 }, (error, response) => {
    if (error) {
      console.error("ListUsers error:", error);
    } else {
      console.log("ListUsers response:", response);
    }
  });

  // Test CreateUser
  client.createUser(
    {
      name: "Bob Wilson",
      email: "bob@example.com",
      age: 32,
    },
    (error, response) => {
      if (error) {
        console.error("CreateUser error:", error);
      } else {
        console.log("CreateUser response:", response);
      }
    }
  );
}

main();
