import unittest
from unittest.mock import patch
from github_api import get_user_repositories, get_repo_commits, get_user_repo_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')
    def test_get_user_repositories(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}]'
        mock_get.return_value = mock_response
        self.assertEqual(get_user_repositories("test_user"), ["repo1", "repo2"])

    @patch('github_api.requests.get')
    def test_get_user_repositories_error(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response
        self.assertEqual(get_user_repositories("test_user"), [])

    @patch('github_api.requests.get')
    def test_get_repo_commits(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '[{"commit": {"message": "commit 1"}}, {"commit": {"message": "commit 2"}}]'
        mock_get.return_value = mock_response
        self.assertEqual(get_repo_commits("test_user", "test_repo"), 2)

    @patch('github_api.requests.get')
    def test_get_repo_commits_error(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response
        self.assertEqual(get_repo_commits("test_user", "test_repo"), 0)

    @patch('github_api.get_user_repositories')
    @patch('github_api.get_repo_commits')
    def test_get_user_repo_commits(self, mock_get_repo_commits, mock_get_user_repositories):
        mock_get_user_repositories.return_value = ["repo1", "repo2"]
        mock_get_repo_commits.side_effect = [3, 5]
        self.assertEqual(get_user_repo_commits("test_user"), [("repo1", 3), ("repo2", 5)])

if __name__ == '__main__':
    unittest.main()
