import math


def calculate_weeks_to_save_time(time_to_automate, time_to_perform, amount_of_times_done):
    # Convert time to automate to minutes
    time_to_automate *= 60

    # Calculate the minimum amount of times done
    min_times_done = time_to_automate / time_to_perform

    # Calculate the number of weeks
    num_weeks = min_times_done / amount_of_times_done

    return num_weeks

print(calculate_weeks_to_save_time(40, 10, 1))

# time_to_automate = 40  # in hours
# time_to_perform = 10  # in minutes
# amount_of_times_done = 1