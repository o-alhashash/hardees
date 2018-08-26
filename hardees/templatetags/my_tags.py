from django import template

register = template.Library()


@register.simple_tag
def item_liked(burger, user_id):
    if burger.likes.filter(id=user_id).exists():
        return '<span name="' + str(burger.id) + '" onclick="like_item(' + str(
            burger.id) + ')"><i class="fas fa-heart"></i></span>'
    return '<span name="' + str(burger.id) + '" onclick="like_item(' + str(
        burger.id) + ')"><i class="far fa-heart"></i></span>'
