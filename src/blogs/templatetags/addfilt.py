from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.filter(name='ctype')
def content_type(obj):
    if not obj:
        return False
    else:
        return ContentType.objects.get_for_model(obj)


class isCurrentNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns

    def render(self, context):
        path = context['request'].path
        for pattern in self.patterns:
            curr_pattern = template.Variable(pattern).resolve(context)
            if path == curr_pattern:
                return "current"
            return ""


@register.tag
def is_current(parser, token):
    """ Check if the browse is currently at this supplied url"""
    args = token.split_contents()
    if len(args) < 2:
        raise (template.TemplateSyntaxError, "%r tag requires at least one argument" % args[0])
    return isCurrentNode(args[1:])
