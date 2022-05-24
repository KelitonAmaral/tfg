from athlete import Athlete
from project.video_processing.lift import Lift
from project.video_processing.analysis import Analysis

# New instance of Athlete class. 
# It takes weight, height and age as contructor parameters
new_athlete = Athlete(98, 180, 36)

# Console prompt to input the weight in kg the athlete lift in the video
weight = int(input("Digite o peso em kg levantado pelo atleta: "))

# New instance of Lift class.
# It takes the path to the video file and weight (kg) lifted
new_lift = Lift(r'project\upload\medias\1080_snatch_82.mp4', weight)

my_trajectory = new_lift.find_trajectory()

analysis = Analysis()

analysis.plot_graph(my_trajectory)

# Call the method to calculate relative strength
relative_strength_index = analysis.calculate_relative_strength(new_athlete.body_height, new_lift.bar_weight)

# Print the resulting relative strength index
print("Índice de força relativa do atleta: ", relative_strength_index)