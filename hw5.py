import requests
import json
import unittest
from unittest.mock import patch, MagicMock

def get_user_repositories(user_id):
    url = f"https://github.com/1deeppanwala/hw4a"
    response = requests.get(url)
    if response.status_code == 200:
        repos = json.loads(response.text)
        return [repo["name"] for repo in repos]
    else:
        print("Error fetching repositories:", response.text)
        return []

def get_repo_commits(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = json.loads(response.text)
        return len(commits)
    else:
        print("Error fetching commits:", response.text)
        return 0

def get_user_repo_commits(user_id):
    repos = get_user_repositories(user_id)
    user_commits = []
    for repo in repos:
        commits = get_repo_commits(user_id, repo)
        user_commits.append((repo, commits))
    return user_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_repositories(self, mock_get):
        user_id = "test_user"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps([{"name": "test_repo"}])
        mock_get.return_value = mock_response
        repos = get_user_repositories(user_id)
        self.assertEqual(repos, ["test_repo"])

    @patch('requests.get')
    def test_get_repo_commits(self, mock_get):
        user_id = "test_user"
        repo_name = "test_repo"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps([{"commit": {"message": "Test commit"}}])
        mock_get.return_value = mock_response
        commits = get_repo_commits(user_id, repo_name)
        self.assertEqual(commits, 1)

if __name__ == "__main__":
    unittest.main()
