from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def drive_truck(self):
        pass

    @abstractmethod
    def work_on_software_project(self):
        pass

    @abstractmethod
    def attend_meeting(self):
        pass


class TruckDriver(Worker):
    def drive_truck(self):
        return "Driving the truck."

    # TruckDriver does not implement work_on_software_project or attend_meeting


class SoftwareEngineer(Worker):
    def work_on_software_project(self):
        return "Working on the software project."

    def attend_meeting(self):
        return "Attending a meeting."

        # SoftwareEngineer does not implement drive_truck

        """_summary_
        So we have a violation of the Interface Segregation Principle (ISP)
        because both classes are forced to implement methods they do not use.
        """
