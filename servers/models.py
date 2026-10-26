from django.db import models

class Port(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"#{self.number} - {self.name}"


class ScannedPorts(models.Model):
    ip = models.CharField(max_length=255)
    ports = models.ManyToManyField(Port, blank=True)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        names = ", ".join(str(p) for p in self.ports.all())
        return f"{self.ip} - {names or 'no open ports'} [{(str(self.scanned_at))[:-13]}]"