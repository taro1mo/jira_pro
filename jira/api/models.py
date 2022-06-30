from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid

def upload_avatar_path(instance, filename):
  ext = filename.split('.')[-1]
  return '/'.join(['avatars', str(instance.user_profile.id)+str(".")+str(ext)])

class Profile(models.Model):
  user_profile = models.OneToOneField(
    User, related_name='user_profile',
    on_delete=models.CASCADE #Userモデルが削除されたとき、関連されたProfileオブジェクト（このクラスで作られたインスタンス）も削除される
  )
  img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

  def __str__(self):
    return self.user_profile.username

class Category(models.Model):
  item = models.CharField(max_length=100)

  def __str__(self):
    return self.item
    
class Task(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  task = models.CharField(max_length=100)
  discription = models.CharField(max_length=300)
  criteria = models.CharField(max_length=100)