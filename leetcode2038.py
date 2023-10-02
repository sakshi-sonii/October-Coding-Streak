# class Solution:
#     def winnerOfGame(self, colors: str) -> bool:
#         alice =0
#         bobby =0
#         if(colors.count('A')<3):
#             return 'false'
#         for i in range(1,len(colors)-1):
#             if(colors[i-1]=='A' and colors[i+1]=='A' and colors[i]=='A'):
#                 alice +=1
#             elif(colors[i-1]=='B' and colors[i+1]=='B' and colors[i]=='B'):
#                 bobby+=1
#         if(alice<=bobby):
#             return 'false'
#         return 'true'

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice = bobby = 0
        
        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bobby += 1
                    
        return alice>bobby