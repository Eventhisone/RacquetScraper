class Racquet:
    """A tennis racquet class"""
    def __init__(self, name, tension, length, pattern, skip_main, tie_main, start_cross, tie_cross):
         self.name = name # Racquet Name
         self.tension = tension # Tension
         self.length = length # Mains Length
         self.pattern = pattern # Pattern
         self.skip_main = skip_main # Skip Main Holes
         self.tie_main = tie_main # Tie Off Main Holes
         self.start_cross = start_cross # Start Crosses
         self.tie_cross = tie_cross # Tie Off Crosses
