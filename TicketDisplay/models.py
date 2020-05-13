# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Users(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=256, blank=True, null=True)  # Field name made lowercase.
    authtoken = models.CharField(db_column='AuthToken', max_length=16, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    signature = models.TextField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    freeformcontactinfo = models.TextField(db_column='FreeformContactInfo', blank=True, null=True)  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=200, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=16, blank=True, null=True)  # Field name made lowercase.
    lang = models.CharField(db_column='Lang', max_length=16, blank=True, null=True)  # Field name made lowercase.
    emailencoding = models.CharField(db_column='EmailEncoding', max_length=16, blank=True, null=True)  # Field name made lowercase.
    webencoding = models.CharField(db_column='WebEncoding', max_length=16, blank=True, null=True)  # Field name made lowercase.
    externalcontactinfoid = models.CharField(db_column='ExternalContactInfoId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactinfosystem = models.CharField(db_column='ContactInfoSystem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    externalauthid = models.CharField(db_column='ExternalAuthId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    authsystem = models.CharField(db_column='AuthSystem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gecos = models.CharField(db_column='Gecos', max_length=16, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pagerphone = models.CharField(db_column='PagerPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=16, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(db_column='Timezone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pgpkey = models.TextField(db_column='PGPKey', blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.realname

class Queues(models.Model):
    name = models.CharField(db_column='Name', unique=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    correspondaddress = models.CharField(db_column='CorrespondAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    commentaddress = models.CharField(db_column='CommentAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    lifecycle = models.CharField(db_column='Lifecycle', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subjecttag = models.CharField(db_column='SubjectTag', max_length=120, blank=True, null=True)  # Field name made lowercase.
    initialpriority = models.IntegerField(db_column='InitialPriority')  # Field name made lowercase.
    finalpriority = models.IntegerField(db_column='FinalPriority')  # Field name made lowercase.
    defaultduein = models.IntegerField(db_column='DefaultDueIn')  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    disabled = models.SmallIntegerField(db_column='Disabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Queues'

class Tickets(models.Model):
    effectiveid = models.IntegerField(db_column='EffectiveId')  # Field name made lowercase.
    #queue = models.IntegerField(db_column='Queue')  # Field name made lowercase.
    queue = models.ForeignKey(Queues, on_delete=models.PROTECT, db_column='Queue')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=16, blank=True, null=True)  # Field name made lowercase.
    issuestatement = models.IntegerField(db_column='IssueStatement')  # Field name made lowercase.
    resolution = models.IntegerField(db_column='Resolution')  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    initialpriority = models.IntegerField(db_column='InitialPriority')  # Field name made lowercase.
    finalpriority = models.IntegerField(db_column='FinalPriority')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    timeestimated = models.IntegerField(db_column='TimeEstimated')  # Field name made lowercase.
    timeworked = models.IntegerField(db_column='TimeWorked')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.
    timeleft = models.IntegerField(db_column='TimeLeft')  # Field name made lowercase.
    told = models.DateTimeField(db_column='Told', blank=True, null=True)  # Field name made lowercase.
    starts = models.DateTimeField(db_column='Starts', blank=True, null=True)  # Field name made lowercase.
    started = models.DateTimeField(db_column='Started', blank=True, null=True)  # Field name made lowercase.
    due = models.DateTimeField(db_column='Due', blank=True, null=True)  # Field name made lowercase.
    resolved = models.DateTimeField(db_column='Resolved', blank=True, null=True)  # Field name made lowercase.
    #lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdatedby = models.ForeignKey(Users, on_delete=models.PROTECT, db_column='LastUpdatedBy', related_name='solver')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    #creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    disabled = models.SmallIntegerField(db_column='Disabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tickets'

class Customfields(models.Model):
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rendertype = models.CharField(db_column='RenderType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    maxvalues = models.IntegerField(db_column='MaxValues', blank=True, null=True)  # Field name made lowercase.
    pattern = models.TextField(db_column='Pattern', blank=True, null=True)  # Field name made lowercase.
    repeated = models.SmallIntegerField(db_column='Repeated')  # Field name made lowercase.
    basedon = models.IntegerField(db_column='BasedOn', blank=True, null=True)  # Field name made lowercase.
    valuesclass = models.CharField(db_column='ValuesClass', max_length=64, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    lookuptype = models.CharField(db_column='LookupType', max_length=255)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    disabled = models.SmallIntegerField(db_column='Disabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomFields'

class Customfieldvalues(models.Model):
    customfield = models.IntegerField(db_column='CustomField')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomFieldValues'

class Objectcustomfields(models.Model):
    customfield = models.IntegerField(db_column='CustomField')  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectCustomFields'

class Objectcustomfieldvalues(models.Model):
    #customfield = models.IntegerField(db_column='CustomField')  # Field name made lowercase.
    customfield = models.ForeignKey(Customfields, on_delete=models.PROTECT, db_column='CustomField')  # Field name made lowercase.
    objecttype = models.CharField(db_column='ObjectType', max_length=255)  # Field name made lowercase.
    #objectid = models.IntegerField(db_column='ObjectId')  # Field name made lowercase.
    objectid = models.ForeignKey(Tickets, on_delete=models.CASCADE, db_column='ObjectId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    largecontent = models.TextField(db_column='LargeContent', blank=True, null=True)  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=80, blank=True, null=True)  # Field name made lowercase.
    contentencoding = models.CharField(db_column='ContentEncoding', max_length=80, blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.IntegerField(db_column='LastUpdatedBy')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    disabled = models.SmallIntegerField(db_column='Disabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectCustomFieldValues'

class Transactions(models.Model):
    objecttype = models.CharField(db_column='ObjectType', max_length=64)  # Field name made lowercase.
    #objectid = models.IntegerField(db_column='ObjectId')  # Field name made lowercase.
    objectid = models.ForeignKey(Tickets, on_delete=models.CASCADE, db_column='ObjectId')  # Field name made lowercase.
    timetaken = models.IntegerField(db_column='TimeTaken')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=40, blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.CharField(db_column='OldValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.CharField(db_column='NewValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    referencetype = models.CharField(db_column='ReferenceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oldreference = models.IntegerField(db_column='OldReference', blank=True, null=True)  # Field name made lowercase.
    newreference = models.IntegerField(db_column='NewReference', blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'

class Attachments(models.Model):
    #transactionid = models.IntegerField(db_column='TransactionId')  # Field name made lowercase.
    transactionid = models.ForeignKey(Transactions, on_delete=models.CASCADE, db_column='TransactionId')  # Field name made lowercase.
    parent = models.IntegerField(db_column='Parent')  # Field name made lowercase.
    messageid = models.CharField(db_column='MessageId', max_length=160, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='Filename', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=80, blank=True, null=True)  # Field name made lowercase.
    contentencoding = models.CharField(db_column='ContentEncoding', max_length=80, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    headers = models.TextField(db_column='Headers', blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='Creator')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attachments'

    def __str__(self):
        return self.content