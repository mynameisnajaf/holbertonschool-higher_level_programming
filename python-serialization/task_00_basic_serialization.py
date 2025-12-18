#!/usr/bin/env python3
import pickle


def serialize_and_save_to_file(data, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)
    except (pickle.PicklingError, AttributeError) as e:
        raise TypeError("Data is not serializable") from e

def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
