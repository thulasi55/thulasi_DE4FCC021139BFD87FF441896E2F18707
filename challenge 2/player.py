# Define the base class player
class Player:
    def play(self):
        print("The player is playing cricket.")


# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("the batsman is batting.")


# Define the derivid class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")


# Create abjects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for eacn object
batsman.play()
bowler.play()