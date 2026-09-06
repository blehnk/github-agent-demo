"""
GitHub Agent Demo module.
Simulates basic GitHub automated workflows and agent actions.
"""

from typing import Dict, Any, List
from datetime import datetime, timezone


class GitHubAgent:
    """A simulated GitHub Agent capable of code reviews, health checks, and release notes."""

    def __init__(self, agent_name: str = "OctoBot", model: str = "gemini-flash"):
        self.agent_name = agent_name
        self.model = model

    def review_pull_request(self, pr_title: str, diff_text: str) -> Dict[str, Any]:
        """Simulates automated PR review comments."""
        issues: List[str] = []
        status = "APPROVED"

        if "TODO" in diff_text:
            issues.append("Found unaddressed TODO comments in changes.")
        if "console.log" in diff_text or "print(" in diff_text:
            issues.append("Found leftover debug logging statements.")
        if len(diff_text.strip()) == 0:
            issues.append("Pull request contains empty diff.")
            status = "CHANGES_REQUESTED"
        elif issues:
            status = "COMMENT"

        return {
            "agent": self.agent_name,
            "pr_title": pr_title,
            "status": status,
            "issues_found": issues,
            "summary": (
                f"Reviewed PR '{pr_title}' - {len(issues)} issue(s) flagged."
                if issues
                else f"PR '{pr_title}' looks clean and ready to merge!"
            ),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def check_repo_health(self, files: List[str]) -> Dict[str, Any]:
        """Simulates checking repository health according to open-source best practices."""
        essential_files = ["README.md", ".gitignore", "LICENSE"]
        missing = [f for f in essential_files if f not in files]

        score = int(((len(essential_files) - len(missing)) / len(essential_files)) * 100)

        return {
            "agent": self.agent_name,
            "score": score,
            "missing_files": missing,
            "status": "HEALTHY" if score >= 80 else "NEEDS_ATTENTION",
            "recommendations": (
                [f"Consider adding {f}" for f in missing]
                if missing
                else ["Repository standards met!"]
            ),
        }

    def generate_release_notes(self, version: str, commits: List[str]) -> Dict[str, Any]:
        """Simulates automated release notes generation from commit history."""
        features = [c for c in commits if c.startswith("feat")]
        fixes = [c for c in commits if c.startswith("fix")]
        others = [c for c in commits if not c.startswith("feat") and not c.startswith("fix")]

        return {
            "version": version,
            "agent": self.agent_name,
            "features": features,
            "bug_fixes": fixes,
            "other_changes": others,
            "formatted_markdown": (
                f"## Release {version}\n\n"
                + (f"### Features\n" + "\n".join(f"- {f}" for f in features) + "\n\n" if features else "")
                + (f"### Bug Fixes\n" + "\n".join(f"- {f}" for f in fixes) + "\n\n" if fixes else "")
                + (f"### Other Changes\n" + "\n".join(f"- {o}" for o in others) + "\n" if others else "")
            ).strip(),
        }
