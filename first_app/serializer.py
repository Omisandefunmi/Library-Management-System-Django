from rest_framework import serializers

from first_app.models import Book, Publisher


# exclude = []


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'email', 'url']
        # field = '__all__'
        # exclude = []

class BookSerializer(serializers.ModelSerializer):  # noqa
    book_title = serializers.CharField(max_length=255, source='title')
    publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='first_app:publisher-detail'
    # )

    class Meta:
        model = Book
        fields = ['book_title', 'description', 'isbn', 'price', 'publisher']
