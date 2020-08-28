from django.db import models

class Petition(models.Model):

    title = models.CharField(max_length=120, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name='작성자')
    date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    accept_count = models.IntegerField(
      default=0
    )
    agree_count = models.IntegerField(
      default=0

    )
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'simu_petition'
        verbose_name = '건국 시무 청원'

        verbose_name_plural = '건국 시무 청원'


