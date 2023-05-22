from django.urls import path

from .views import base_views, question_views, answer_views, comment_question_views, comment_answer_views

app_name = 'pybo'

urlpatterns = [
    # base
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('question/vote/delete/<int:question_id>/', question_views.question_vote_delete, name='question_vote_delete'),

    # commnet_question
    path('comment/create/question/<int:question_id>/', comment_question_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_question_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_question_views.comment_delete_question, name='comment_delete_question'),
    path('comment/question/vote/<int:comment_id>/', comment_question_views.comment_question_vote, name='comment_question_vote'),
    path('comment/question/vote/delete/<int:comment_id>/', comment_question_views.comment_question_vote_delete, name='comment_question_vote_delete'),

    # answer
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
    path('answer/vote/delete/<int:answer_id>/', answer_views.answer_vote_delete, name='answer_vote_delete'),

    # comment_answer
    path('comment/create/answer/<int:answer_id>/', comment_answer_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_answer_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_answer_views.comment_delete_answer, name='comment_delete_answer'),
    path('comment/answer/vote/<int:comment_id>/', comment_answer_views.comment_answer_vote, name='comment_answer_vote'),
    path('comment/answer/vote/delete/<int:comment_id>/', comment_answer_views.comment_answer_vote_delete, name='comment_answer_vote_delete'),
]