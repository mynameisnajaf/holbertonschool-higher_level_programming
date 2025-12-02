#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    deff_names = dir(hidden_4)
    for i in range(len(deff_names)):
        if deff_names[i][:2] != "__":
            print(deff_names[i])
