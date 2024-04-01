import pytest

from odometry import Odometry

# Sample tests for Odometry class
class TestOdometry:
    @pytest.fixture
    def odometry(self):
        drivetrain = Drivetrain(wheel_base=0.5, wheel_radius=0.1, gearing_ratio=1.5)
        return Odometry(x=0, y=0, drivetrain=drivetrain)

    def test_init(self, odometry):
        assert odometry.x == 0
        assert odometry.y == 0
        assert odometry.theta == 0

    def test_update(self, odometry):
        # Assuming some values for left and right speeds
        odometry.drivetrain.set_speeds(0.5, 0.7)
        initial_x, initial_y, initial_theta = odometry.get_position()
        odometry.update()
        new_x, new_y, new_theta = odometry.get_position()
        assert (new_x, new_y) != (initial_x, initial_y)  # Position should change
        assert new_theta != initial_theta  # Orientation should change

    # Add more tests for other methods


