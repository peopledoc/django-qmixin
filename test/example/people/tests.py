# -*- coding: utf-8 -*-

from django.db import models
from django.test import TestCase

from people.models import Group, Person


class SimpleTest(TestCase):
    
    fixtures = ['testing']
    
    def test_manager(self):
        self.failUnless(isinstance(
            Person.objects.minors(),
            models.query.QuerySet))
        
        self.failUnlessEqual(
            pks(Person.objects.minors()),
            pks(Person.objects.filter(age__lt=18)))
        
        self.failUnless(isinstance(
            Person.objects.adults(),
            models.query.QuerySet))
        
        self.failUnlessEqual(
            pks(Person.objects.adults()),
            pks(Person.objects.filter(age__gte=18)))
    
    def test_qset(self):
        self.failUnless(isinstance(
            Person.objects.all().minors(),
            models.query.QuerySet))
        
        self.failUnlessEqual(
            pks(Person.objects.all().minors()),
            pks(Person.objects.filter(age__lt=18)))
        
        self.failUnless(isinstance(
            Person.objects.all().adults(),
            models.query.QuerySet))
        
        self.failUnlessEqual(
            pks(Person.objects.all().adults()),
            pks(Person.objects.filter(age__gte=18)))


class RelationTest(TestCase):
    
    fixtures = ['testing']
    
    def test(self):
        for group in Group.objects.all():
            self.failUnless(isinstance(
                group.people.all(),
                models.query.QuerySet))
            
            self.failUnless(isinstance(
                group.people.minors(),
                models.query.QuerySet))
            
            self.failUnlessEqual(
                pks(group.people.minors()),
                pks(group.people.filter(age__lt=18)))
            
            self.failUnless(isinstance(
                group.people.adults(),
                models.query.QuerySet))
            
            self.failUnlessEqual(
                pks(group.people.adults()),
                pks(group.people.filter(age__gte=18)))


def pks(qset):
    """Return the list of primary keys for the results of a QuerySet."""
    
    return sorted(tuple(qset.values_list('pk', flat=True)))
