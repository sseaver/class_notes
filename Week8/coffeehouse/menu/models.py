from django.db import models


class Special(models.Model):
    created_user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "https://www.dunkindonuts.com/content/dunkindonuts/en/menu/beverages/hotbeverages/specialitycoffee/latte/_jcr_content/block/image.img.png/1466490202242.png"
