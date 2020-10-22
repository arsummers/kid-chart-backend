from django.db import models

# Create your models here.
from django.db import models
# from django.forms import ModelForm
from django.urls import reverse
# from django.views.generic.base import HttpResponseRedirect
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Rule(models.Model):
    """
    Model representing a base class for rules. Weight field is how much you want the rule to be worth. The same rule can be applied to multiple kids, and a single kid can be assigned multiple rules.
    """
    name = models.CharField(max_length=50, help_text='Enter rule', default=None)
    weight = models.IntegerField(default=0)
    description = models.TextField(max_length=250, help_text='Enter description of rule')

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'{self.name} \n Points worth: {self.weight} \n Description: {self.description}'

    def get_absolute_url(self):
        """
        url to gain access to one Rule
        """

        return reverse('rule-detail', args=[str(self.id)])


class RuleInstance(models.Model):
    """
    Model representing instances of rules. Instances should be assigned to kids. New rules instances can now be assigned to kids.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this rule')
    rule = models.ForeignKey(Rule, on_delete=models.SET_NULL, null=True)
    kid = models.ForeignKey('Kid', related_name='rules', on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False, help_text='Is this rule completed?')

    def __str__(self):
        return f'{self.rule.name}, Assigned to: {self.kid.name}, Completed: {self.completed}'



class Kid(models.Model):
    """
    Model representing a base class for kids. Each kid will be represented by name with a primary key. Rules can be assigned to individual kids.
    """
    name = models.CharField(max_length=20, help_text='Enter kid name', default=None)
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    # methods
    def __str__(self):
        return f'Name: {self.name}\n Points total: {self.points} \n Rules assigned: {self.rules}'

    def get_absolute_url(self):
        """
        url to gain access to one Kid
        """
    
        return reverse('kid-detail', args=[str(self.id)])

class Reward(models.Model):
    name = models.CharField(max_length=50, help_text='Enter reward', default=None)
    points_needed = models.IntegerField(default=0)
    description = models.TextField(max_length=250, help_text='Enter description of reward')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Name: {self.name} \n Unlocks at: {self.points_needed} points \n Description: {self.description}'

