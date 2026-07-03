classroom = ["sanjay", "parithi", "vihnu", "arun"]

print("parithi:", "present" if "parithi" in classroom else "absent",
      "| ram:", "absent" if "ram" not in classroom else "present")

classroom = ["sanjay", "parithi", "vihnu", "arun"]

# check parithi (using in)
if "parithi" in classroom:
    print("present")
else:
    print("absent")

# check ram (using not in)
if "ram" not in classroom:
    print("absent")
else:
    print("present")