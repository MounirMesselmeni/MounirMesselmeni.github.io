Title: Enable Asciifolding in Elasticsearch/Haystack
Date: 2015-12-13 21:04
Category: Web Development
Tags: Django, Python, Haystack, elasticsearch
Summary: Enable ascii folding for your elasticsearch indexing
Keywords: python
          django
          haystack
          elasticsearch
          ascii
          folding
          asciifolding


Haystack is a great tool which add a lot of simplicity to use full text search on your Django project.

I used it with elasticsearch but I encountered search results which does not ignore ascii 
characters differences. E.g. searching for '

In fact as mentionned in [Elasticsearch Docs][1], token filter of type asciifolding are used toconverts 
alphabetic, numeric, and symbolic Unicode characters which are not in the first 127 ASCII characters 
(the "Basic Latin" Unicode block) into their ASCII equivalents, if one exists.

To do so, we will add custom `ascii_analyser` to the default elasticsearch backend by overriding it.

```python
	
	from haystack import indexes
    from haystack.backends import elasticsearch_backend as es_backend
    
    
    class AsciifoldingElasticBackend(es_backend.ElasticsearchSearchBackend):
    
        def __init__(self, *args, **kwargs):
            super(AsciifoldingElasticBackend, self).__init__(*args, **kwargs)
            analyzer = {
                "ascii_analyser" : {
                    "tokenizer" : "standard",
                    "filter" : ["standard", "asciifolding", "lowercase"]
                },
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_ngram", "asciifolding"]
                },
                "edgengram_analyzer": {
                    "type": "custom",
                    "tokenizer": "lowercase",
                    "filter": ["haystack_edgengram", "asciifolding"]
                }
            }
            self.DEFAULT_SETTINGS['settings']['analysis']['analyzer'] = analyzer
    
        def build_schema(self, fields):
            content_field_name, mapping = super(AsciifoldingElasticBackend,
                                                self).build_schema(fields)
    
            for field_name, field_class in fields.items():
                field_mapping = mapping[field_class.index_fieldname]
    
                if field_mapping['type'] == 'string' and field_class.indexed:
                    if not hasattr(field_class, 'facet_for') and not field_class.field_type in('ngram', 'edge_ngram'):
                        field_mapping['analyzer'] = "ascii_analyser"
    
                mapping.update({field_class.index_fieldname: field_mapping})
            return (content_field_name, mapping)
    
    
    class AsciifoldingElasticSearchEngine(es_backend.ElasticsearchSearchEngine):
        backend = AsciifoldingElasticBackend

```

The last thing, we need to specify this backend on `settings.py`

```python

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_custom_backend.AsciifoldingElasticSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        },
    }

```


[1]: https://www.elastic.co/guide/en/elasticsearch/reference/1.4/analysis-asciifolding-tokenfilter.html
