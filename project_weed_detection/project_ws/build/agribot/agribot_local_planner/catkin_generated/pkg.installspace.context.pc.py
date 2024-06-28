# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;tf;dynamic_reconfigure;costmap_2d;geometry_msgs;nav_core;pluginlib".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lagribot_local_planner".split(';') if "-lagribot_local_planner" != "" else []
PROJECT_NAME = "agribot_local_planner"
PROJECT_SPACE_DIR = "/root/project_ws/install"
PROJECT_VERSION = "0.0.0"
