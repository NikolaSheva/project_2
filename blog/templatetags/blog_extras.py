# from django import template
#
# register = template.Library()
#
# @register.filter
# def pluralize_ru(count, forms="статья,статьи,статей"):
#     one, few, many = forms.split(',')
#     count = abs(int(count))
#     if 11 <= count % 100 <= 14:
#         return many
#     if count % 10 == 1:
#         return one
#         if 2 <= count % 10 <= 4:
#             return few
#         return many


from django import template

register = template.Library()

@register.filter
def pluralize_ru(count):
    count = int(count)
    if 11 <= count % 100 <= 14:
        return "статей"
    elif count % 10 == 1:
        return "статья"
    elif 2 <= count % 10 <= 4:
        return "статьи"
    else:
        return "статей"