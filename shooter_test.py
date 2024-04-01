import pytest

from shooter import Shooter

# Sample tests for Shooter class
class TestShooter:
    @pytest.fixture
    def shooter(self):
        return Shooter()

    def test_init(self, shooter):
        assert shooter.flywheel_speed == 0
        assert shooter.angle == 0
        assert shooter.feeder_speed == 0
        assert not shooter.loaded

    def test_set_flywheel_speed(self, shooter):
        shooter.set_flywheel_speed(0.8)
        assert shooter.flywheel_speed == 0.8

    def test_set_angle(self, shooter):
        shooter.set_angle(45)
        assert shooter.angle == 45

    def test_set_feeder_speed(self, shooter):
        shooter.set_feeder_speed(0.5)
        assert shooter.feeder_speed == 0.5

    def test_set_loaded(self, shooter):
        shooter.set_loaded()
        assert shooter.loaded

    def test_set_unloaded(self, shooter):
        shooter.set_loaded()
        shooter.set_unloaded()
        assert not shooter.loaded

    # Add more tests for other methods

