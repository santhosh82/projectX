from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


class TJob(models.Model):
    companyName = models.CharField(max_length=50)
    appliedOn = models.DateField(help_text="Please use the following format:  YYYY-MM-DD")
    source = models.CharField(max_length=50)
    jobId = models.CharField(max_length=50, blank=True)
    jobDesc = models.CharField(max_length=200, blank=True)
    statusLink = models.URLField(max_length=200, blank=True)
    ACCEPT = "A"
    REJECT = "R"
    UNKNOWN = "U"
    myChoice = (
        (ACCEPT, 'accept'),
        (REJECT, "reject"),
        (UNKNOWN, "unknown")

    )

    result = models.CharField(max_length=1, choices=myChoice, default=UNKNOWN)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.companyName + " \nresult: " + str(self.result) + " \nappliedOn: " + str(
            self.appliedOn) + " \njobDesc: " + self.jobDesc




class JobShareTable(models.Model):
    fromUserId = models.ForeignKey(User , related_name="%(app_label)s_%(class)s_related")
    toUserId = models.ForeignKey(User)
    jobId = models.ForeignKey(TJob)


    def __str__(self):
        return "from user id : " + self.fromUserId.username + " to user id : " + self.toUserId.username + " job id : " + str(self.jobId);


# The friends table is not implemeneted efficiently as there is normalization
# as some rows have same values
# Also one of my constraint is user_first_id is less than user_second_id
class FriendsTable(models.Model):
    user_first_id =  models.ForeignKey(User , related_name="%(app_label)s_%(class)s_related")
    user_second_id = models.ForeignKey(User)
    myChoice = (
        (0, 'friend'),
        (1, "pending1"),
        (2, "pending2")

    )

    reltype = models.CharField(max_length = 10)

    def __str__(self):
        return "user1 : " + self.user_first_id.username + " user2 : " + self.user_second_id.username + " type : " + self.reltype;
