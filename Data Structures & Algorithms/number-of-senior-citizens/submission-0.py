class Solution:
    def countSeniors(self, details: List[str]) -> int:
        elders = 0
        for passenger in details:
            age = (int(passenger[-4]) * 10) + (int(passenger[-3]))
            
            if age > 60: 
                elders += 1

        return elders

        