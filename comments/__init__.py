# TO-DO
# 因为 django 的各大第三方评论拓展库或多或少有各种不能满足需求的地方，
# 而且代码比较多，没有太多精力研究其源码，所以不知道如何拓展，
# 考虑到曾经仔细研究过一遍 django-contrib-comments 的源码，因此考虑从其中拓展
# 除了 django comments 自身的特性外，需要满足以下额外的需求：

# （finished）1. 允许二级评论。（暂不考虑树状结构，因为对一般站点二级就够了，多级反而体验不好。后续会将多级作为一个额外选项，例如设置 MAX_LEVEL）
# 2. 增加是否允许匿名用户的评论设置，如果设为否，将不能接受非登录用户的提交（而 django-contrib-comments 是允许任何人提交评论的，只要其
#    正确填写了相关的字段）
# 3. 允许评论作者编辑和删除评论
# 4. 关键动作均由 ajax 提交，例如发表评论，删除评论，编辑评论


def get_model():
    from comments.models import CommentWithParent
    return CommentWithParent


def get_form():
    from comments.forms import CommentWithParentForm
    return CommentWithParentForm
