from django.db import models
from django.conf import settings


class Frame(models.Model):

    name = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='frames/'
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class FrameVariant(models.Model):

    ORIENTATION_CHOICES = (
        ('VERTICAL', 'Vertical'),
        ('HORIZONTAL', 'Horizontal'),
    )

    frame = models.ForeignKey(
        Frame,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    size = models.CharField(
        max_length=50
    )

    orientation = models.CharField(
        max_length=20,
        choices=ORIENTATION_CHOICES
    )
    
    thickness = models.CharField(
    max_length=10,
    blank=True,
    null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
    upload_to='frame_variants/',
    blank=True,
    null=True
    )

    photo_top = models.IntegerField(
    default=0
    )

    photo_left = models.IntegerField(
    default=0
    )

    photo_width = models.IntegerField(
    default=0
    )

    photo_height = models.IntegerField(
    default=0
    )

    def __str__(self):

        return (
            f"{self.frame.name} - "
            f"{self.size} - "
            f"{self.orientation}"
        )
class CustomerUpload(models.Model):

    STATUS_CHOICES = (
        ('TEMP', 'Temporary'),
        ('FINAL', 'Final'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    frame_variant = models.ForeignKey(
        FrameVariant,
        on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to='customer_uploads/'
    )

    position_x = models.IntegerField(
    default=0
    )

    position_y = models.IntegerField(
        default=0
    )

    zoom_level = models.FloatField(
        default=1.0
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='TEMP'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.user.email} - "
            f"{self.frame_variant}"
        )