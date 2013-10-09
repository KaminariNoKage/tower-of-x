'''fileName: logicPuzzleQuestions
stores all questions and answers in dictionary form'''

class logicPuzzleQuestions(object):
    def __init__(self):
        None
    def dictor(self):
        questionDict = {'a. In this room there is a lady, and in the other room there is a tiger. b. In one of these rooms there is a lady, and in one of these rooms there is a tiger':'b','a. At least one of these rooms contains a lady. b. A tiger is in the other room': 'b', 'a. Either a tiger is in this room or a lady is in the other room. b. A lady is in the other room.':'b','a. Both rooms contains ladies. b. Both rooms contain ladies':'b','a. At least one room contains a lady. b. The other room contains a lady':'a', 'a. It makes no difference which room you pick. b. There is a lady in the other room':'a', 'a. It does make a difference which room you pick. b. You are better off choosing the other room':'a','a. A tiger is in this room. b. A lady is in this room. c. A tiger is in room b':'a', 'a. Room c is empty. b. The tiger is in room a. c. This room is empty':'a'}
        return questionDict 
