# ign_moveit2_examples (Modified)

C++ 및 Python 예제를 활용하여 MoveIt 2 기반 로봇 모션을 Gazebosim에서 구현하여 데모 데이터를 저장하고
이후 데모 데이터를 통해 학습된 best_policy를 이용하여 추론을 하는 프로젝트

이는 원본 예제(`ign_moveit2_examples`)를 수정하여 커스터마이즈한 버전

C++과 Python 예제 모두 [ros2_control](https://github.com/ros-controls/ros2_control)을 사용하며, Gazebo와의 연동은 [gz_ros2_control](https://github.com/ros-controls/gz_ros2_control)을 통해 수행
추가적으로, Python 예제는 공식 MoveIt 2 Python 바인딩이 없기 때문에 [pymoveit2](https://github.com/AndrejOrsula/pymoveit2) 모듈을 사용

## Dependencies

- ROS 2 Galactic  
- Gazebo Fortress  
- Python: `pymoveit2` (Python 예제용 MoveIt 2 인터페이스)  

---

## Build & Install

```bash
# 원본 예제(`ign_moveit2_examples`) clone
git clone https://github.com/AndrejOrsula/ign_moveit2_examples.git

# Build workspace
colcon build --merge-install --symlink-install --cmake-args "-DCMAKE_BUILD_TYPE=Release"

# Source workspace
source install/local_setup.bash

# 수정파일 clone
git clone https://..

# sdf파일 수정
..tools의 sdf로 수정

# 수정파일 복사 후 build
colcon build --merge-install --symlink-install --cmake-args "-DCMAKE_BUILD_TYPE=Release"
