from django.contrib.postgres.search import SearchVector, SearchHeadline, SearchQuery, SearchRank

from projects.models import Project


def q_search(query):
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    result = Project.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>',
        )
    )
    return result