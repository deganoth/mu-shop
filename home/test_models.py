from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import BannerImage
# Create your tests here.


class TestBannerImageModel(TestCase):
    def test_all_contents_to_be_valid(self):
        banner = BannerImage()
        banner.name = "Create a Name"
        banner.title = "Create a Title"
        banner.tag = "Create a Tag"
        banner.description = "Create some Text"
        banner.image = SimpleUploadedFile(
            "best_file_eva.txt",
            b"these are the file contents!"
        )

        banner.save()
        self.assertEqual(banner.name, "Create a Name")
        self.assertEqual(banner.title, "Create a Title")
        self.assertEqual(banner.tag, "Create a Tag")
        self.assertEqual(banner.description, "Create some Text")
        self.assertEqual(banner.image, "images/best_file_eva.txt")

    def test_banner_name_as_a_string(self):
        banner = BannerImage()
        banner.name = "Create a Name"
        self.assertEqual("Create a Name", str(banner))
