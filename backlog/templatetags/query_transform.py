from django import template

register = template.Library()


# додаємо до пагінації параметри пошуку у строці(щоб при перемиканні в строці залишався запит
@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)

    return updated.urlencode()
