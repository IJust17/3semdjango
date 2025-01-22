from django.core.management.base import BaseCommand
from core.models import File


class Command(BaseCommand):
    help = "Reorder files by created date (or any other logic)."

    def handle(self, *args, **options):
        """
       , сортируем по created_at (по возрастанию)
        и в соответствии с порядком обновляем поле 'sort_index'.
        """

        files = File.objects.all().order_by('sort_index')
        # sort_index = порядковый номер
        for i, f in enumerate(files, start=1):
            f.sort_index = i
            f.save()

        self.stdout.write(self.style.SUCCESS(
            f"Successfully reordered {files.count()} files by created_at"
        ))
