from requests import Session
from retry import retry
from typing import Generator, List, Dict, Optional
import time
from tqdm import tqdm

from src.utils.helpers import batched

def get_paper_batch(session: Session, ids: List[str], S2_API_KEY: Optional[str], fields: str = "paperId,title", **kwargs) -> List[Dict]:
    params = {"fields": fields, **kwargs}
    headers = {"X-API-KEY": S2_API_KEY} if S2_API_KEY else {}
    body = {"ids": ids}

    with session.post(
        "https://api.semanticscholar.org/graph/v1/paper/batch",
        params=params,
        headers=headers,
        json=body,
    ) as response:
        response.raise_for_status()
        return response.json()

def get_author_batch(session: Session, ids: List[str], S2_API_KEY: Optional[str], fields: str = "name,hIndex,citationCount", **kwargs) -> List[Dict]:
    params = {"fields": fields, **kwargs}
    headers = {"X-API-KEY": S2_API_KEY} if S2_API_KEY else {}
    body = {"ids": ids}

    with session.post(
        "https://api.semanticscholar.org/graph/v1/author/batch",
        params=params,
        headers=headers,
        json=body,
    ) as response:
        response.raise_for_status()
        return response.json()

@retry(tries=3, delay=2.0)
def get_one_author(session: Session, author: str, S2_API_KEY: Optional[str]) -> Optional[List[Dict]]:
    params = {"query": author, "fields": "authorId,name,hIndex", "limit": "10"}
    headers = {"X-API-KEY": S2_API_KEY} if S2_API_KEY else {}

    with session.get(
        "https://api.semanticscholar.org/graph/v1/author/search",
        params=params,
        headers=headers,
    ) as response:
        try:
            response.raise_for_status()
            response_json = response.json()
            if len(response_json.get("data", [])) >= 1:
                return response_json["data"]
            return None
        except Exception as ex:
            print(f"Exception fetching author: {ex}")
            return None

def get_papers(ids: List[str], S2_API_KEY: Optional[str], batch_size: int = 100, **kwargs) -> Generator[Dict, None, None]:
    with Session() as session:
        for ids_batch in batched(ids, batch_size=batch_size):
            yield from get_paper_batch(session, ids_batch, S2_API_KEY, **kwargs)

def get_authors(all_authors: List[str], S2_API_KEY: Optional[str], batch_size: int = 100, **kwargs) -> Dict[str, List[Dict]]:
    author_metadata_dict = {}
    with Session() as session:
        for author in tqdm(all_authors, desc="Fetching author metadata"):
            auth_map = get_one_author(session, author, S2_API_KEY)
            if auth_map is not None:
                author_metadata_dict[author] = auth_map
            
            # Rate limiting
            time.sleep(0.02 if S2_API_KEY else 1.0)
            
    return author_metadata_dict
