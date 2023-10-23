import rclpy
from gazebo_msgs.srv import SetEntityState

def call_set_entity_state_service():
    rclpy.init()
    node = rclpy.create_node('set_entity_state_client')

    # Create a client for the service
    client = node.create_client(SetEntityState, '/gazebo/set_entity_state')

    # Wait for the service to become available
    if not client.wait_for_service(timeout_sec=10.0):
        node.get_logger().info('Service /gazebo/set_entity_state is not available.')
        return

    # Create a request
    request = SetEntityState.Request()
    request.state.name = 'person_walking'
    #request.state.pose.position.x = 10.5
    #request.state.pose.position.y = 0.0
    #request.state.pose.position.z = 0.0

    request.state.twist.linear.x = 0.5
    request.state.pose.position.y = 0.0
    request.state.pose.position.z = 0.0
    request.state.reference_frame = 'world'

    # Call the service
    future = client.call(request)

    #rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info('Service call was successful.')
    else:
        node.get_logger().info('Service call failed.')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    call_set_entity_state_service()
