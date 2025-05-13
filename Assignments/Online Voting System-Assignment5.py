from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_basic_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    @abstractmethod
    def retrieve_role(self):
        pass

# Voter class
class Voter(Person):
    def __init__(self, name, age, voter_id):
        super().__init__(name, age)
        self._voter_id = voter_id
        self._has_voted = False

    def retrieve_role(self):
        return "Voter"

    def vote(self):
        self._has_voted = True

    def has_voted(self):
        return self._has_voted

    def display_info(self):
        return f"{self.get_basic_info()}, Role: {self.retrieve_role()}, Voter ID: {self._voter_id}"

# Candidate class
class Candidate(Person):
    def __init__(self, name, age, candidate_id, party):
        super().__init__(name, age)
        self._candidate_id = candidate_id
        self._party = party
        self._votes = 0

    def retrieve_role(self):
        return "Candidate"

    def receive_vote(self):
        self._votes += 1

    def get_votes(self):
        return self._votes

    def display_info(self):
        return f"{self.get_basic_info()}, Role: {self.retrieve_role()}, ID: {self._candidate_id}, Party: {self._party}, Votes: {self._votes}"

# Election class
class Election:
    election_name = "National Election 2025"

    def __init__(self):
        self._candidates = []
        self._voters = []
        self._votes_cast = 0

    def add_candidate(self, candidate: Candidate):
        self._candidates.append(candidate)

    def add_voter(self, voter: Voter):
        self._voters.append(voter)

    def cast_vote(self, voter_id, candidate_id):
        
        voter = None
        for v in self._voters:
            if v._voter_id == voter_id:
                voter = v
                break

       
        candidate = None
        for c in self._candidates:
            if c._candidate_id == candidate_id:
                candidate = c
                break

        if voter is None:
            print("Invalid Voter ID.")
            return

        if voter.has_voted():
            print("Voter has already voted.")
            return

        if candidate is None:
            print("Invalid Candidate ID.")
            return

        candidate.receive_vote()
        voter.vote()
        self._votes_cast += 1
        print(f"Vote cast successfully for {candidate._name} by {voter._name}.")

    def display_results(self):
        print("\n--- Election Results ---")
      
        for candidate in self._candidates:
            print(f"{candidate._name} ({candidate._party}): {candidate.get_votes()} votes")

        winner = None
        highest_votes = -1
        for c in self._candidates:
            if c.get_votes() > highest_votes:
                highest_votes = c.get_votes()
                winner = c

        if winner:
            print(f"\nWinner: {winner._name} from {winner._party} with {winner.get_votes()} votes.")

    @classmethod
    def election_info(cls):
        return f"Election Name: {cls.election_name}"

    @staticmethod
    def welcome_message():
        return "Welcome to the Online Voting System"
    
print(Election.welcome_message())
print(Election.election_info())
   
e = Election()
c1 = Candidate("Alice", 40, "C101", "Party A")
c2 = Candidate("Bob", 50, "C102", "Party B")
e.add_candidate(c1)
e.add_candidate(c2)
 
v1 = Voter("Charlie", 30, "V201")
v2 = Voter("Daisy", 22, "V202")
v3 = Voter("Ethan", 35, "V203")
e.add_voter(v1)
e.add_voter(v2)
e.add_voter(v3)

e.cast_vote("V201", "C101")
e.cast_vote("V202", "C102")
e.cast_vote("V203", "C101")

e.cast_vote("V201", "C102")
e.display_results()
