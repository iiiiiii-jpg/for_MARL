************start gazebo, movebase, fleet server one by one****************

------######################Start Gazebo and spawn all robots.******

** [Compile if needed]
cd for_maRL/
colcon build --symlink-install
 
cd for_maRL/
. /opt/ros/foxy/setup.bash
. /usr/share/gazebo-11/setup.sh
. ./install/setup.bash
ros2 launch plannar_mover mymover.launch.xml

-------#######################Send 
. /opt/ros/foxy/setup.bash
. ./install/setup.bash
ros2 run plannar_mover pub_sub_modelstate 



ros2 topic list
ros2 service list
export GAZEBO_MODEL_DATABASE_URI=""


 1985  ros2 service list
 1986  ros2 service info /gazebo/set_entity_state
 1987  ros2 service call /gazebo/get_entity_state gazebo_msgs/GetEntityState '{name: blue_ball, reference_frame: world}'
 1988  colcon build --symlink-install
 1989  ros2 run plannar_mover set_entity 
 1990  colcon build --symlink-install
 1991  ros2 run plannar_mover set_entity 
 1992  colcon build --symlink-install
 1993  . ./install/setup.bash
 1994  ros2 topic list
 1995  ros topic info /gazebo/model_states
 1996  ros2 topic info /gazebo/model_states
 1997  ros2 run plannar_mover set_entity 
 1998  gazebo 
 1999  . ./install/setup.bash
 2000  ros2 launch plannar_gazebo mymover.launch.xml
 2001  . /opt/ros/foxy/setup.bash
 2002  ros2 launch plannar_gazebo mymover.launch.xml
 2003  export GAZEBO_MODEL_DATABASE_URI=""
 2004  ros2 launch plannar_gazebo mymover.launch.xml
 2005  . /usr/share/gazebo-11/setup.sh
 2006  . /usr/share/gazebo/setup.sh
 2007  ros2 launch plannar_gazebo mymover.launch.xml
 2008  export GAZEBO_MODEL_DATABASE_URI=""
 2009  ros2 launch plannar_gazebo mymover.launch.xml
 2010  colcon build --symlink-install
 2011  . ./install/setup.bash
 2012  ros2 launch plannar_gazebo mymover.launch.xml
 2013  colcon build --symlink-install
 2014  . ./install/setup.bash
 2015  ros2 launch plannar_gazebo mymover.launch.xml
 2016  $GAZEBO_MODEL_PATH
 2017  colcon build --symlink-install
 2018  . ./install/setup.bash
 2019  ros2 launch plannar_gazebo mymover.launch.xml
 2020  colcon build --symlink-install
 2021  . ./install/setup.bash
 2022  ros2 launch plannar_gazebo mymover.launch.xml





