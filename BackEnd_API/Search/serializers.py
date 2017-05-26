from rest_framework import serializers
import BackEnd_API.Search.models as DB

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.Episode
        fields = ('id','title', 'plot', 'language', 'runtime', 'rate')

class KindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.Kind
        fields = '__all__'


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.Country
        fields = '__all__'

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.Job
        fields = '__all__'

class MovieSerieDetailsSerializer(serializers.HyperlinkedModelSerializer):
    episodes = EpisodeSerializer()

    class Meta:
        model = DB.MovieSerieDetails
        fields = ('id','type', 'title', 'plot', 'release', 'language', 'runtime', 'rate', 'videoFormat', 'episodes','country', 'kind')

class HumanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.Human
        fields = ('id','name', 'firstname', 'birthday','deathday','birthdayPlace','description','job','playing','nationality')

class MovieKindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.MovieKind
        fields = ('kind','movieSerie')

class HumanJobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.HumanJob
        fields = ('human','job')

class HumanCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.HumanCountry
        fields = ('human','country')

class MovieSerieCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.MovieSerieCountry
        fields = ('movieSerie','country')

class HumanMovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DB.HumanMovie
        fields = ('human','movieSerie')
