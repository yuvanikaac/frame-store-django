from django.db import models


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

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return (
            f"{self.frame.name} - "
            f"{self.size} - "
            f"{self.orientation}"
        )