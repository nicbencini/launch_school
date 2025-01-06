
class Candidate:

    def __init__(self, name):
        self._name = name
        self._vote_count = 0

    @property
    def name(self):
        return self._name
    
    @property
    def vote_count(self):
        return self._vote_count

    def __iadd__(self, value):
        self._vote_count += value

        return self

class Election:

    def __init__(self, candidates):

        self._candidates = candidates
    
    def results(self):
        for candidate in self._candidates:

            name = candidate.name
            votes = candidate.vote_count
            print(f'{name}: {votes} votes')

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

