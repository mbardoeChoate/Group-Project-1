import pytest

from drivetrain import Drivetrain

# Sample tests for Drivetrain class
class TestDrivetrain:
    @pytest.fixture
    def drivetrain(self):
        return Drivetrain(wheel_base=0.5, wheel_radius=0.1, gearing_ratio=1.5)

    def test_init(self, drivetrain):
        assert drivetrain.wheel_base == 0.5
        assert drivetrain.wheel_radius == 0.1
        assert drivetrain.gearing_ratio == 1.5
        assert drivetrain.get_left_speed() == 0
        assert drivetrain.get_right_speed() == 0

    def test_set_speeds(self, drivetrain):
        drivetrain.set_speeds(0.5, 0.7)
        assert drivetrain.get_left_speed() == 0.5
        assert drivetrain.get_right_speed() == 0.7

    def test_stop(self, drivetrain):
        drivetrain.set_speeds(0.5, 0.7)
        drivetrain.stop()
        assert drivetrain.get_left_speed() == 0
        assert drivetrain.get_right_speed() == 0

    def test_get_linear_speed(self, drivetrain):
        drivetrain.set_speeds(0.5, 0.7)
        assert drivetrain.get_linear_speed() != 0

    # Add more tests for other methods


