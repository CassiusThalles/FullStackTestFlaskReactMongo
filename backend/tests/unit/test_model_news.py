from models.news import News
from datetime import datetime

def test_news():
    """
    GIVEN a News model
    WHEN a new registry is created
    THEN check te title, content and publish date
    """
    today_str = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    input_data = {'title': 'Um título de teste', 'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec facilisis purus ligula, tristique pharetra massa feugiat id. Nam in molestie enim, et mattis turpis. Etiam rutrum, mi sit amet egestas iaculis, dui nisi semper ipsum, sed interdum tellus lacus id risus. Aenean egestas facilisis euismod. Quisque sit amet neque vitae erat convallis sagittis. Aliquam quis dui convallis, placerat nulla commodo, mattis ex. Quisque nunc nulla, efficitur at libero ac, feugiat ultricies risus. Suspendisse lacinia quam sem, ut dapibus quam luctus a. Quisque accumsan viverra eros, et pulvinar massa maximus et. Aliquam erat volutpat. Etiam lacinia elit quis libero suscipit, ut consequat enim tristique. Donec eu purus et lacus tempor aliquet id malesuada nibh. Sed felis nunc, commodo in metus venenatis, laoreet pretium mauris. Nam tempus at mi et congue.", 'publish': today_str}
    news = News(**input_data)
    assert news.title == 'Um título de teste'
    assert news.content == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec facilisis purus ligula, tristique pharetra massa feugiat id. Nam in molestie enim, et mattis turpis. Etiam rutrum, mi sit amet egestas iaculis, dui nisi semper ipsum, sed interdum tellus lacus id risus. Aenean egestas facilisis euismod. Quisque sit amet neque vitae erat convallis sagittis. Aliquam quis dui convallis, placerat nulla commodo, mattis ex. Quisque nunc nulla, efficitur at libero ac, feugiat ultricies risus. Suspendisse lacinia quam sem, ut dapibus quam luctus a. Quisque accumsan viverra eros, et pulvinar massa maximus et. Aliquam erat volutpat. Etiam lacinia elit quis libero suscipit, ut consequat enim tristique. Donec eu purus et lacus tempor aliquet id malesuada nibh. Sed felis nunc, commodo in metus venenatis, laoreet pretium mauris. Nam tempus at mi et congue.'
    assert news.publish == today_str
