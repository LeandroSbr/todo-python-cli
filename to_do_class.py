import json
from datetime import datetime as d
from datetime import date
from enum import Enum


class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class ToDoList:
    def __init__(self):
        try:
            with open("tasks.json") as f:
                self.data = json.load(f)
                for n in self.data:
                    self.data[n]["expiry"] = d.strptime(self.data[n]
                                                        ["expiry"],
                                                        "%d/%m/%Y").date()
        except (json.JSONDecodeError, FileNotFoundError):
            self.data = {}

    def add_activity(self, name: str, expiry: date, priority: str) -> dict:
        if not isinstance(name, str) or not isinstance(priority, str):
            raise ValueError("activity and priority must be valid strings")
        if not isinstance(expiry, date):
            raise ValueError("expiry must be a valid date object")
        if (not priority == Priority.HIGH.value
            and not priority == Priority.MEDIUM.value
                and not priority == Priority.LOW.value):
            raise ValueError("Piority must be high, medium or low")
        if name in self.data:
            raise ValueError("Activity already registered")
        self.data[name] = {"check": False, "expiry": expiry,
                           "priority": priority}
        return self.data

    def check_activity(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("activity must be a valid string")
        if name not in self.data:
            raise ValueError("This activity is not present on the list")
        if self.data[name]["check"]:
            raise ValueError("This activity already checked")
        self.data[name]["check"] = True

    def uncheck_activity(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("activity must be a valid string")
        if name not in self.data:
            raise ValueError("This activity is not present on the list")
        if not self.data[name]["check"]:
            raise ValueError("This activity already unchecked")
        self.data[name]["check"] = False

    def delete_activity(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("activity must be a valid string")
        if name not in self.data:
            raise ValueError("This activity is not present on the list")
        self.data.pop(name)

    def filter_check_actitivities(self) -> dict:
        return {k: v for k, v in self.data.items() if v["check"]}

    def filter_unchecked_activities(self) -> dict:
        return {k: v for k, v in self.data.items() if not v["check"]}

    def filter_priority(self, data: dict) -> dict:
        filtered = {k: v for k, v in data.items()
                    if v["priority"] == Priority.HIGH.value}
        filtered.update({k: v for k, v in data.items()
                         if v["priority"] == Priority.MEDIUM.value})
        filtered.update({k: v for k, v in data.items()
                         if v["priority"] == Priority.LOW.value})
        return filtered

    def show_activities(self) -> dict:
        return self.data

    def save_activities(self) -> None:
        with open("tasks.json", "w", encoding='utf-8') as f:
            serializable = {
                k: {**v, "expiry": v["expiry"].strftime("%d/%m/%Y")}
                for k, v in self.data.items()
            }
            json.dump(serializable, f, indent=4, ensure_ascii=False)

    def clear_data(self) -> None:
        with open("tasks.json", "w", encoding='utf-8') as f:
            json.dump({}, f, indent=4, ensure_ascii=False)

    def get_data(self) -> dict:
        return self.data
