from ..forms import AddListingForm

from django import forms
from string import Template
from django.utils.safestring import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile


class PictureWidget(forms.widgets.ClearableFileInput):
	def render(self, name, value, attrs=None, renderer = None):
		html = ""

		# if the imageField has not an image yet
		if not value :
			html += """
			Currently empty<br>
			Add :
			"""
		# else show the current
		else:
			html += """
			<img height="200px" width="200px" src="$link" alt="$link_name">
			<input type="checkbox" name="image-clear" id="image-clear_id">
			<label for="image-clear_id">Clear</label><br>
			Change:
		"""

		html += """
			<input type="file" name="image" class="form-control" id="id_image">
		"""


		if value:
			html = Template(html)	
			# if listing has already an image uploaded, then the file is stored under a different class
			if isinstance(value, InMemoryUploadedFile):
				html = html.substitute(link = value.file,link_name = value.name.replace('media/',''))			
			else:
				html = html.substitute(link = value.url,link_name = value.url.replace('media/',''))

		return mark_safe(html)


class UpdateListingForm(AddListingForm):

	class Meta(AddListingForm.Meta):
		fields = ['title', 'description']


	# by assigning a picture widget, we have a preview of the current image
	image = forms.ImageField(required=False, widget = PictureWidget)







