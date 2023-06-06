def check_if_request_user_answered_ranking(request_user, ranking):
    return ranking.filter(author_id=request_user).exists()
