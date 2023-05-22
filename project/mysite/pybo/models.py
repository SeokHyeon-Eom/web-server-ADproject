from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# make migration => 테이블을 준비하는 파일
# create migration => 테이블을 만든다
# 여러 DB를 표준화해서 쉽게 쓸 수 있게 만든다.
# 아이디 자동으로 만들어준다.

class Question(models.Model):
    # 질문 model에 로그인 하지 질문을 달 수 없게 한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateField(null=True, blank=True)
    modify_counter = models.IntegerField(default=0)
    answer_comment = models.IntegerField(default=0)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # 위와 동일
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #related_name이 별명같은 것이다. 자동적으로 만들어지는데 이상하게 나는 안 되서 이름을 만들어주었다.
    #question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ans')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateField(null=True, blank=True)
    modify_counter = models.IntegerField(default=0)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    modify_counter = models.IntegerField(default=0)
    # 댓글은 질문과 답변 모두에 추가할 수 있기 때문에 FK를 2개 가지지만 실제로 값이 들어가는 FK는 하나이다.
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    voter = models.ManyToManyField(User, related_name='voter_commnet')