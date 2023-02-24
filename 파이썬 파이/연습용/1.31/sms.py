#우리가 메시징 서비스를 구축한다. 모델링을 해보자
#sms
#1. 수신자, 발신자, 내용

class Sms: 
    def __init__(self, receiver, sender, content):
        self.receiver = receiver
        self.sender = sender
        self.content = content

    def __str__(self):
        return f'SMS 수신자: {self.receiver}, 발신자: {self.sender}, 내용: {self.content}'

    def send(self):
        return f'SMS가 발송되었습니다.'
        


class Lms(Sms): # 자식 클래스
    def __init__(self, receiver, sender, content):
        super().__init__(receiver, sender, content)

    def __str__(self):
        return f'LMS 수신자: {self.receiver}, 발신자: {self.sender}, 내용: {self.content}'

    def send(self):
        return f'LMS가 발송되었습니다.'


m1 = Sms('01012345678', '999999999', '메시지 입니다.')
print(m1)

m2 = Lms('01012345678', '999999999', '장문 메시지 입니다. 장문 메시지 입니다. 장문 메시지 입니다.')
print(m2)
print(m2.send())


#내가 서비스를 구축하는데 유지, 보수를 신경쓰는 입장에서 생각.

#부모: 음료 클래스
#자식: 술, 탄산음료, 물

#이동수단
#자신: 대중교통, 자가용, 몇 인승 / 바퀴 몇 개 / 문이 몇 개인지
