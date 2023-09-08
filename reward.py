def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    # Give higher reward if the speed is fast!
  
    if distance_from_center <= marker_1:
        if speed >= 0.8:
            reward = 1.0
        else:
            reward = 0.75

    elif distance_from_center <= marker_2:
        if speed >= 0.8:
            reward = 0.5
        else:
            reward = 0.35
            
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track

    return float(reward)
