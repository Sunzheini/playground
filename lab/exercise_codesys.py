from opcua import Client


# Define the endpoint
url = "opc.tcp://localhost:4840"

# Initialize the OPC UA Client
client = Client(url)

try:
    # Connect to the OPC UA Server
    client.connect()

    # Get a specific node using its node id
    # node_id should be replaced by the actual node id
    node = client.get_node("node_id")

    # Print the value of the node
    print("Node value: ", node.get_value())

    # Set a new value for the node
    # new_value should be replaced with the desired value


    node.set_value(new_value)

    # Disconnect the client
    client.disconnect()

except Exception as e:
    print(e)
