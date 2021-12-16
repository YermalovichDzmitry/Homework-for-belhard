from dataclasses import dataclass
import pickle


@dataclass
class Car:
    speed: int
    color: str

    def get_time_to_goal(self, s):
        return s / self.speed

    def start_the_car(self):
        print("The car is started")


audi = Car(90, "blue")
serialized_object = pickle.dumps(audi)
derialized_object = pickle.loads(serialized_object)

derialized_object.start_the_car()
print(derialized_object.get_time_to_goal(200))
