from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from pybo.models import Question, Answer, Comment


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 조회
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    for que in page_obj:
        cnt = 0
        answer_list = Answer.objects.filter(question=que.pk)
        for ans in answer_list:
            comment_list = Comment.objects.filter(answer=ans.pk)
            cnt += comment_list.count()
        que.answer_comment = cnt
        que.save()
    
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)