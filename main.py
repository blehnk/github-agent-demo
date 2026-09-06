#!/usr/bin/env python3
"""
GitHub Agent Demo CLI.
Run simulated agent workflows from your terminal.
"""

import argparse
import json
import os
from src.agent import GitHubAgent


def main():
    parser = argparse.ArgumentParser(description="GitHub Agent Demo CLI")
    parser.add_argument(
        "--action",
        choices=["review", "health", "release", "all"],
        default="all",
        help="Action to execute with the agent (default: all)",
    )
    parser.add_argument(
        "--name",
        default="OctoAgent",
        help="Custom name for the agent",
    )
    args = parser.parse_args()

    agent = GitHubAgent(agent_name=args.name)
    print(f"[Agent] Initialized {agent.agent_name} (Model: {agent.model})\n")

    if args.action in ("health", "all"):
        print("=" * 50)
        print("[Health] Running Repository Health Check...")
        local_files = [f for f in os.listdir(".") if os.path.isfile(f)]
        health = agent.check_repo_health(local_files)
        print(f"Score: {health['score']}% - Status: {health['status']}")
        print(f"Recommendations: {', '.join(health['recommendations'])}\n")

    if args.action in ("review", "all"):
        print("=" * 50)
        print("[Review] Simulating Pull Request Review...")
        dummy_diff = """
+ def calculate_metrics():
+     # TODO: optimize query performance
+     print("calculating...")
+     return 42
"""
        review = agent.review_pull_request(
            pr_title="feat: add metric calculations", diff_text=dummy_diff
        )
        print(f"Status: {review['status']}")
        print(f"Summary: {review['summary']}")
        if review["issues_found"]:
            print("Issues detected:")
            for issue in review["issues_found"]:
                print(f"  - {issue}")
        print()

    if args.action in ("release", "all"):
        print("=" * 50)
        print("[Release] Simulating Automated Release Notes...")
        sample_commits = [
            "feat: add GitHubAgent class and core methods",
            "feat: add CLI support via main.py",
            "fix: resolve edge case with empty diff reviews",
            "docs: update README with usage guide",
        ]
        release = agent.generate_release_notes("v0.1.0", sample_commits)
        print(release["formatted_markdown"])
        print()

    print("=" * 50)
    print("[Success] Demo finished successfully!")


if __name__ == "__main__":
    main()
