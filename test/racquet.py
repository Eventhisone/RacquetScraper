class Racquet:
    """A tennis racquet class"""
    def __init__(self, name, tension_min, tension_max, main_length, cross_length, pattern, skip_main, tie_main, start_cross, tie_cross):
         self.name = name # Racquet Name
         self.tension_min = tension_min # Min Tension
         self.tension_max = tension_max # Max Tension
         self.main_length = main_length # Mains Length
         self.cross_length = cross_length # Crosses Length
         self.pattern = pattern # Pattern
         self.skip_main = skip_main # Skip Main Holes
         self.tie_main = tie_main # Tie Off Main Holes
         self.start_cross = start_cross # Start Crosses
         self.tie_cross = tie_cross # Tie Off Crosses
