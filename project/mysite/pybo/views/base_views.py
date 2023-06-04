from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from pybo.models import Question, Answer, Comment


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # answer
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recent')

    answer_list = Answer.objects.filter(question=question_id)
    if so == 'recommend':
        answer_list = answer_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        answer_list = answer_list.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:
        answer_list = answer_list.order_by('-create_date')
    
    paginator = Paginator(answer_list, 5)
    page_obj = paginator.get_page(page)

    # comment
    page_cmt = request.GET.get('page_cmt', '1')
    so_cmt = request.GET.get('so_cmt', 'recent')

    comment_list = Comment.objects.filter(question=question_id)
    if so_cmt == 'recommend':
        comment_list = comment_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else:
        comment_list = comment_list.order_by('-create_date')

    paginator_cmt = Paginator(comment_list, 5)
    page_cmt_obj = paginator_cmt.get_page(page_cmt)
    
    context = {'question': question, 'answer_list': page_obj, 'page': page, 'so': so, 'comment_list': page_cmt_obj, 'page_cmt': page_cmt, 'so_cmt': so_cmt}
    return render(request, 'pybo/question_detail.html', context)