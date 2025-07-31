from abc import ABC, abstractmethod


class SoftwareEngineer(ABC):
    @abstractmethod
    def write_code(self):
        pass

    @abstractmethod
    def debug_code(self):
        pass


class Driver(ABC):
    @abstractmethod
    def drive_vehicle(self):
        pass

    @abstractmethod
    def deliver_package(self):
        pass


class MeetingParticipant(ABC):
    @abstractmethod
    def attend_meeting(self):
        pass


class JuniorSoftwareEngineer(SoftwareEngineer, MeetingParticipant):
    def write_code(self):
        return "Writing code as a junior software engineer."

    def debug_code(self):
        return "Debugging code as a junior software engineer."

    def attend_meeting(self):
        return "Attending a meeting as a junior software engineer."


class DeliveryDriver(Driver):
    def drive_vehicle(self):
        return "Driving the delivery vehicle."

    def deliver_package(self):
        return "Delivering a package."


if __name__ == "__main__":
    # Usage
    dev = JuniorSoftwareEngineer()
    dev.write_code()
    dev.attend_meeting()

    driver = DeliveryDriver()
    driver.drive_vehicle()
    driver.deliver_package()
