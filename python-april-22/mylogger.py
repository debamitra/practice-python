# 🧩 Challenge: log_event Logger

# Write a function called log_event that takes:
#	•	a required event_name (str)
#	•	an optional category (default: "general")
#	•	any number of tags (via *args)
#	•	and any number of metadata key-value pairs (via **kwargs)

# Your function should return a string like this:
# log_event(
#     "user_login",
#     "auth",
#     "successful",
#     "mobile",
#     user="deb",
#     location="India"
# )
# should return
# Event: user_login [auth]
# Tags: successful, mobile
# Metadata: user=deb, location=India

# Requirements:
# 	1.	Use *args and **kwargs
# 	2.	Handle optional arguments cleanly (even if no tags or metadata are passed)
# 	3.	Output should be clean and readable


def log_event(event_name, category='general', *args, **kwargs):
    if event_name or len(event_name) != 0:
        print("Event: ", event_name,'[',category,']')
    if len(args) != 0:
        print("Tags: ", ','.join(args))
    if len(kwargs) != 0:
        print("Metadata: ", ", ".join(f"{k}={v}" for k, v in kwargs.items()))

log_event(
    "user_login",
    "auth",
    "successful",
    "mobile",
    user="deb",
    location="India"
)

log_event("error")