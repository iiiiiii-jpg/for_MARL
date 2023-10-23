import rclpy
from rclpy.node import Node
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose, Twist
from gazebo_msgs.srv import SetEntityState
import math


class Pub_sub_modelstate(Node):

    def __init__(self):
        super().__init__('pub_sub_modelstate')
        
        self.subscription = self.create_subscription(ModelStates,'/gazebo/model_states',self.model_state_callback,10)    
        self.state_pub = self.create_publisher(ModelState, '/gazebo/set_model_state', 10)      
        self.poss = ModelState()
        self.timer = self.create_timer(1, self.timer_callback) 
        self.model_state = ModelState()

        self.client = self.create_client(SetEntityState, '/gazebo/set_entity_state')

        # Wait for the service to become available
        if not self.client.wait_for_service(timeout_sec=10.0):
            node.get_logger().info('Service /gazebo/set_entity_state is not available.')
            return

        # Create a request
        self.request = SetEntityState.Request()

    def model_state_callback(self, data):
        self.get_logger().info('Received model state data')
        for i in range(len(data.name)):
            if data.name[i] == "red_box1": #"blue_ball":
                x = data.pose[i].position.x
                y = data.pose[i].position.y
                self.poss.pose = data.pose[i]
                #self.get_logger().info('Got Destination_request: "%s"' % destination_request)
                print("Position of blue_ball (x, y): ({}, {})".format(x, y))
    
    def move_blue_ball(self):

        self.model_state.twist = Twist()
        vel_msg = self.model_state.twist

        vel_msg.linear.x=0.0
        vel_msg.linear.y=0.0
        vel_msg.linear.z=1.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0
        vx=0.0
        vy=0.0;v=0.5;theta=0.0;r=4.0
        w=v/(r*10)
        while True:
            # Create a ModelState message to set the new position
            self.model_state.reference_frame = "world"
            self.model_state.model_name = "red_box1" #"blue_ball"
            #model_state.pose.position.x = 5.0  # Replace with your desired x-coordinate
            #model_state.pose.position.y = 3.0  # Replace with your desired y-coordinate
            #model_state.pose.position.z = 0.0
            self.model_state.pose = self.poss.pose
            #model_state.pose.orientation.x = 0.0
            #model_state.pose.orientation.y = 0.0
            #model_state.pose.orientation.z = 0.0
            #model_state.pose.orientation.w = 0.0
            vx=-v*math.sin(theta)
            vy=v*math.cos(theta)
            vel_msg.linear.x=vx
            vel_msg.linear.y=vy
            # Publish the new position
            self.state_pub.publish(self.model_state)
            theta=theta+w
               	                                
    def timer_callback(self):

        self.request.state.name = 'red_box1'# person_walking
        #self.request.state.pose.position.x = 10.5
        #self.request.state.pose.position.y = 0.0
        #self.request.state.pose.position.z = 0.0

        self.request.state.pose = self.poss.pose

        self.request.state.twist.linear.x = -1.0
        self.request.state.pose.position.y = 0.0
        self.request.state.pose.position.z = 0.0
        self.request.state.reference_frame = 'world'
      
    
        # Call the service
        self.get_logger().info('calling service...')
        future = self.client.call_async(self.request)
        if future.done():#result() is not None:
            self.get_logger().info('Service call was successful.')
        else:
            self.get_logger().info('Service call failed.')

def main(args=None):
    rclpy.init(args=args)
    pub_sub_modelstate = Pub_sub_modelstate()
    #pub_sub_modelstate.move_blue_ball()
    rclpy.spin(pub_sub_modelstate)
    pub_sub_modelstate.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    





