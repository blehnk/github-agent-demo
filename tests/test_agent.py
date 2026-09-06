"""Unit tests for GitHubAgent."""

import unittest
from src.agent import GitHubAgent


class TestGitHubAgent(unittest.TestCase):
    def setUp(self):
        self.agent = GitHubAgent(agent_name="TestBot")

    def test_review_pull_request_flags_todo_and_print(self):
        diff = "+ # TODO: clean up\n+ print('debug')"
        result = self.agent.review_pull_request("feat: sample", diff)
        self.assertEqual(result["status"], "COMMENT")
        self.assertEqual(len(result["issues_found"]), 2)

    def test_review_pull_request_empty_diff(self):
        result = self.agent.review_pull_request("chore: empty", "")
        self.assertEqual(result["status"], "CHANGES_REQUESTED")

    def test_review_pull_request_approved(self):
        diff = "+ def add(a, b):\n+     return a + b"
        result = self.agent.review_pull_request("feat: clean function", diff)
        self.assertEqual(result["status"], "APPROVED")
        self.assertEqual(len(result["issues_found"]), 0)

    def test_check_repo_health_full(self):
        files = ["README.md", ".gitignore", "LICENSE"]
        health = self.agent.check_repo_health(files)
        self.assertEqual(health["score"], 100)
        self.assertEqual(health["status"], "HEALTHY")

    def test_check_repo_health_partial(self):
        files = ["README.md"]
        health = self.agent.check_repo_health(files)
        self.assertLess(health["score"], 100)
        self.assertEqual(health["status"], "NEEDS_ATTENTION")

    def test_generate_release_notes(self):
        commits = [
            "feat: add feature X",
            "fix: resolve bug Y",
            "docs: update readme",
        ]
        notes = self.agent.generate_release_notes("v1.0.0", commits)
        self.assertEqual(len(notes["features"]), 1)
        self.assertEqual(len(notes["bug_fixes"]), 1)
        self.assertEqual(len(notes["other_changes"]), 1)
        self.assertIn("## Release v1.0.0", notes["formatted_markdown"])


if __name__ == "__main__":
    unittest.main()
