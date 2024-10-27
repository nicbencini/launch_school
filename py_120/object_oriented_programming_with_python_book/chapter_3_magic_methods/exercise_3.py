

class Candidate:

    vote_count = 0
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def __iadd__(self,number):

        if not isinstance(number,int):
            return NotImplemented
        
        self.vote_count += number
        


class Election:
    
    @classmethod
    def get_votes(cls,candidate):
        return candidate.vote_count

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):

        for candidate in self.candidates:
            print(f'{candidate}: {candidate.vote_count} votes')
        
        winning_candidate = sorted(candidates, key=self.get_votes, reverse=True)[0]

        total_votes = sum([candidate.vote_count for candidate in candidates])

        print(f'{winning_candidate} won: {(winning_candidate.vote_count/total_votes) * 100} of votes')




mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()