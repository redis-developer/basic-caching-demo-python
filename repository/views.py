from django.http import HttpResponse, HttpResponseNotFound
from django.core.cache import cache
from django.utils.decorators import classonlymethod
from django.views import View

import asyncio
import httpx
import json


async def get_repositories_count(response_data, repository_name):
    async with httpx.AsyncClient() as client:
        httpx_request = await client.get(
            f'https://api.github.com/users/{repository_name}'
        )

        try:
            httpx_request.raise_for_status()
        except httpx.HTTPStatusError as exc:
            return HttpResponse(status=exc.response.status_code)

        github_statistic_data = httpx_request.json()
        public_repositories_count = github_statistic_data.get(
            'public_repos'
        )

        if public_repositories_count is not None:
            cache.set(
                repository_name,
                public_repositories_count,
                timeout=3600,
            )
        else:
            return HttpResponseNotFound()

        response_data['repos'] = public_repositories_count

        return response_data


class GetRepositoriesView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, repository_name, *args, **kwargs):
        public_repository_cache = cache.get(repository_name)
        response_data = {
            'username': repository_name,
            'cached': False,
        }

        if public_repository_cache is not None:
            response_data['repos'] = public_repository_cache
            response_data['cached'] = True
        else:
            response_data = await get_repositories_count(response_data, repository_name)

        return HttpResponse(json.dumps(response_data), status=200)
