from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import URLBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel, PageChooserPanel

class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
    
class MethodCardPage(Page):
	picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
	why = RichTextField(blank=True)
	how = RichTextField(blank=True)
	
MethodCardPage.content_panels = Page.content_panels + [
	ImageChooserPanel('picture'),
	FieldPanel('why'),
	FieldPanel('how'),
]
	
class LessonPlanPage(Page):

	EXPONENTIAL_TECHNOLOGY_CHOICES = (
		('3D', '3D Printing'),
		('robot', 'Robots'),
		('bitcoin', 'Bitcoin'),
		('ai', 'AI'),
		('diybio', 'DIYbio'),
		('iot', 'IoT'),
	)

	theme = RichTextField(blank=True, help_text='Set the theme or topic for the lesson. Is it about space and colonizing a planet? Is it dinosaurs? What is it?')
	
	exponential_technology = models.CharField(max_length=10, choices=EXPONENTIAL_TECHNOLOGY_CHOICES)
	
	introduction = StreamField([
		('paragraph', blocks.RichTextBlock(icon = 'edit', help_text='How will you introduce the lesson to the kids?')),
		('image', ImageChooserBlock(icon='image / picture', help_text='Introductory image')),
		('video_embed', EmbedBlock(icon='media', help_text='Introductory video')),
		('link', URLBlock(icon='link', help_text='Link to intorductiontory video or other content')),
		('document',DocumentChooserBlock(icon='doc-empty', help_text='Any document you want to show during introduction')),
	])
	
	new_tool = StreamField([
		('paragraph', blocks.RichTextBlock(icon = 'edit', help_text='Describe the new tool the kids will learn and use in this lesson.')),
		('image', ImageChooserBlock(icon='image / picture', help_text='Picture about the new tool')),
		('video_embed', EmbedBlock(icon='media', help_text='Introduce the new tool in a video')),
		('link', URLBlock(icon='link', help_text='Link to videos, webpages etc. to introducethe new tool')),
		('document',DocumentChooserBlock(icon='doc-empty', help_text='Any document such as a users guide for instance.')),
	])

	design_challenge = StreamField([
		('paragraph', blocks.RichTextBlock(icon = 'edit', help_text='Describe the design challenge. Pose open ended questions or better yet write a short story.')),
		('image', ImageChooserBlock(icon='image / picture', help_text='Images used in design challenge')),
		('video_embed', EmbedBlock(icon='media', help_text='Embed a video that will pose the design challenge')),
		('link', URLBlock(icon='link', help_text='Link to any video or webpage ... though I don\'t see why you would here...')),
		('document',DocumentChooserBlock(icon='doc-empty', help_text='Upload any document such as story cards')),
	])

	method = models.ForeignKey(
		'MethodCardPage',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
	)

	introduction_length = models.PositiveSmallIntegerField(help_text='in minutes Including introduction of theme, new tool and design challenge')

	def _get_introduction_start(self):
		return 0
	introduction_start = property(_get_introduction_start)	

	# empathize

	empathize_length = models.PositiveSmallIntegerField(help_text='in minutes')
	
	def _get_empathize_start(self):
		return self.introduction_length
	empathize_start = property(_get_empathize_start)

	#define

	define_length = models.PositiveSmallIntegerField(help_text='in minutes')
	
	def _get_define_start(self):
		return self.introduction_length + self.empathize_length
	define_start = property(_get_define_start)

	#ideate
    
	ideate_length = models.PositiveSmallIntegerField(help_text='in minutes')

	def _get_ideate_start(self):
		return self.introduction_length + self.empathize_length + self.define_length
	ideate_start = property(_get_ideate_start)	
    #prototype
    
	prototype_length = models.PositiveSmallIntegerField(help_text='in minutes')
    
	def _get_prototype_start(self):
		return self.introduction_length + self.empathize_length + self.define_length + self.ideate_length
	prototype_start = property(_get_prototype_start)
    	
    #test

	test_length = models.PositiveSmallIntegerField(help_text='in minutes')
   
   	def _get_test_start(self):
   		return self.introduction_length + self.empathize_length + self.define_length + self.ideate_length + self.prototype_length
	test_start = property(_get_test_start)
       
	def _get_total_length(self):
		return self.introduction_length + self.empathize_length + self.define_length + self.ideate_length + self.prototype_length + self.test_length
	total_length = property(_get_total_length)
    
	link_with_real_life = StreamField([
		('paragraph', blocks.RichTextBlock(icon = 'edit', help_text='Describe how what the kids did actually looks in real life.')),
		('image', ImageChooserBlock(icon='image / picture', help_text='Images for how this looks in real life')),
		('video_embed', EmbedBlock(icon='media', help_text='Embed a video that shows real life applications')),
		('link', URLBlock(icon='link', help_text='Link to any video or webpage of real life applications')),
		('document',DocumentChooserBlock(icon='doc-empty', help_text='Upload any document that shows real life use cases')),
	])
   
   
LessonPlanPage.content_panels = Page.content_panels + [
    FieldPanel('theme'),
    FieldPanel('exponential_technology'),
    StreamFieldPanel('introduction'),
    StreamFieldPanel('new_tool'),
    StreamFieldPanel('design_challenge'),
    PageChooserPanel('method'),
    MultiFieldPanel(
    	children=[
    		FieldPanel('introduction_length'), 
	    	FieldPanel('empathize_length'),
    		FieldPanel('define_length'),
    		FieldPanel('ideate_length'),
    		FieldPanel('prototype_length'),
    		FieldPanel('test_length')],
    	heading='Timing'),
    StreamFieldPanel('link_with_real_life'),
]