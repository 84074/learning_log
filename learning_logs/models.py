from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """用户学习的主题。"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识。"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示。"""
        # 练习18 - 2：简短的条目当前，Django在管理网站或shell中显示Entry实例时，模型Entry的方法__str__()
        # 都在其末尾加上省略号。请在方法__str__()中添加一条 if语句，以便仅在条目长度超过
        # 50字符时才添加省略号。使用管理网站添加一个不超过50字符的条目，并核实显示它时没有省略号。
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"

