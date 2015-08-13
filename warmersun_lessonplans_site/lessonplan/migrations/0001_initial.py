# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonPlanPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('theme', wagtail.wagtailcore.fields.RichTextField(help_text='Set the theme or topic for the lesson. Is it about space and colonizing a planet? Is it dinosaurs? What is it?', blank=True)),
                ('exponential_technology', models.CharField(max_length=10, choices=[('3D', '3D Printing'), ('robot', 'Robots'), ('bitcoin', 'Bitcoin'), ('ai', 'AI'), ('diybio', 'DIYbio'), ('iot', 'IoT')])),
                ('introduction', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(help_text='How will you introduce the lesson to the kids?', icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Introductory image', icon='image / picture')), ('video_embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Introductory video', icon='media')), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to intorductiontory video or other content', icon='link')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(help_text='Any document you want to show during introduction', icon='doc-empty'))])),
                ('introduction_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('new_tool', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Describe the new tool the kids will learn and use in this lesson.', icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Picture about the new tool', icon='image / picture')), ('video_embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Introduce the new tool in a video', icon='media')), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to videos, webpages etc. to introducethe new tool', icon='link')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(help_text='Any document such as a users guide for instance.', icon='doc-empty'))])),
                ('design_challenge', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Describe the design challenge. Pose open ended questions or better yet write a short story.', icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Images used in design challenge', icon='image / picture')), ('video_embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Embed a video that will pose the design challenge', icon='media')), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text="Link to any video or webpage ... though I don't see why you would here...", icon='link')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(help_text='Upload any document such as story cards', icon='doc-empty'))])),
                ('empathize_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('define_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('ideate_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('prototype_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('test_length', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('link_with_real_life', wagtail.wagtailcore.fields.StreamField([('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Describe how what the kids did actually looks in real life.', icon='edit')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Images for how this looks in real life', icon='image / picture')), ('video_embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Embed a video that shows real life applications', icon='media')), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to any video or webpage of real life applications', icon='link')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(help_text='Upload any document that shows real life use cases', icon='doc-empty'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MethodCardPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('why', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('how', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('picture', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='lessonplanpage',
            name='method',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='lessonplan.MethodCardPage', null=True),
        ),
    ]
