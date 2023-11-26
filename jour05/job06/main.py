def distance_walked_per_week(steps, height):
    height_m = height / 100
    total = (steps * height) * 10 * 7 / 100
    print(f"Pour {steps} marches de {height} cm, le gardien parcourt {total} m par semaine.")
    
distance_walked_per_week(200,60)