from charactercreator.models import Character
import time
from django.core.cache import cache

def run():
  time.perf_counter()
  print(Character.objects.count())
  time.perf_counter()    
  cache.clear()
  time.perf_counter()  
  chars = Character.objects.all()
  print(len(chars))
  time.perf_counter()



