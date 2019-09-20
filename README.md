# mongo-python-backend

Generic backend implementation exposing REST API with auth and state storage via mongoDB.

## Fun in a Shell

```
make shell
>>> from RestApi.serializers import AssaySerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> ass = Assay(code="Foo\nbar\nbaz")
>>> ass.save()
>>> serializer = AssaySerializer(ass)
>>> serializer.data
{'id': 1, 'record_timestamp': '2019-09-20T03:42:06.392784Z', 'title': '', 'code': 'Foo\nbar\nbaz', 'active': False}
>>> print(repr(serializer))
AssaySerializer(<Assay: Assay object (1)>):
    id = IntegerField(read_only=True)
    record_timestamp = DateTimeField(read_only=True)
    title = CharField()
    code = CharField()
    active = BooleanField(
```
