from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class MenuItems(models.Model):
    title = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True,
        related_name="children"
    )
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.title
