from django.db import models


# Create your models here.
class Episode(models.Model):
    title = models.CharField(max_length=48)
    plot = models.CharField(max_length=5000, default=None)
    language = models.CharField(max_length=8, default=None)
    runtime = models.TimeField(null=True)
    rate = models.IntegerField(null=True)
    season = models.IntegerField(null=True)



    def __str__(self):
        return "Title :  " + self.title

################################################################################################

class Kind(models.Model):
    kind = models.CharField(max_length=48)


    def __str__(self):
        return "Kind :  " + self.kind


################################################################################################
class Country(models.Model):
    country = models.CharField(max_length=8)


    def __str__(self):
        return "Country :  " + self.country

################################################################################################
class Job(models.Model):
    job = models.CharField(max_length=48)


    def __str__(self):
        return "Job :  " + self.job

################################################################################################
class MovieSerieDetails(models.Model):
    type = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    plot = models.CharField(max_length=500)
    id_api = models.IntegerField(null=False)
    release = models.DateField(null=True)
    language = models.CharField(max_length=8,null=True)
    runtime = models.TimeField(null=True)
    rate = models.IntegerField(null=True)
    videoFormat = models.CharField(max_length=5, null=True)

    episodes = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True)

    country = models.ManyToManyField(Country, through='MovieSerieCountry')

    kind = models.ManyToManyField(Kind, through='MovieKind')

    def __str__(self):
        return "title :  " + self.title

################################################################################################
class Human(models.Model):
    name = models.CharField(max_length=48)
    firstname = models.CharField(max_length=48)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    birthdayPlace = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=500, null=True)

    job = models.ManyToManyField(Job, through='HumanJob')
    playing = models.ManyToManyField(MovieSerieDetails, through='HumanMovie')
    nationality = models.ManyToManyField(Country, through='HumanCountry')

    def __str__(self):
        return "Name :  " + self.name + "Firstname : " + self.firstname

################################################################################################

class MovieKind(models.Model):
    kind = models.ForeignKey(Kind)
    movieSerie = models.ForeignKey(MovieSerieDetails)

    def __str__(self):
        return self.kind.kind + " : " + self.movieSerie.title

class HumanJob(models.Model):
    human = models.ForeignKey(Human)
    job = models.ForeignKey(Job)

    def __str__(self):
        return self.human.firstname + self.human.name + " : " + self.job.job

class HumanCountry(models.Model):
    human = models.ForeignKey(Human)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.human.firstname + self.human.name + " : " + self.country.country

class MovieSerieCountry(models.Model):
    movieSerie = models.ForeignKey(MovieSerieDetails)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.movieSerie.title + " : " + self.country.country

class HumanMovie(models.Model):
    human = models.ForeignKey(Human)
    movieSerie = models.ForeignKey(MovieSerieDetails)

    def __str__(self):
        return self.human.firstname + self.human.name + " : " + self.movieSerie.title