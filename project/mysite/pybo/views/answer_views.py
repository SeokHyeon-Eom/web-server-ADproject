from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from pybo.forms import AnswerForm, CommentForm
from pybo.models import Question, Answer, Comment


@login_required(login_url='common:login') # 로그인 상태가 아니면 먼저 로그인 화면으로 리다이렉트 해주는 기능
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # 로그인이 되어있는지 확인한다.
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id) # 저장하고 화면 다시그려서 확인
    else:
        form = AnswerForm()
        # return HttpResponseNotAllowed('Only POST is possible.') # 저장하는거 아니면 오류 
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context) # 답변이 몇개있는지 확인


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    # 없어도 돌아간다. 왜냐하면 기본적으로 템플릿에서 검사하기 떄문이다.
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.modify_counter += 1
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')
def answer_vote_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천을 취소할 수 없습니다')
    else:
        answer.voter.remove(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)