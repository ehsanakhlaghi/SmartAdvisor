# container_security_checker.py

"""
Base structure for Container Misconfiguration Detection Tool
"""

import os
import json
from typing import List, Dict

class ContainerConfigChecker:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.findings = []

    def load_config(self) -> Dict:
        try:
            with open(self.config_path, 'r') as f:
                config_data = f.read()
            return config_data
        except Exception as e:
            raise FileNotFoundError(f"Error reading config file: {e}")

    def check_base_image(self, dockerfile_lines: List[str]):
        for line in dockerfile_lines:
            if line.startswith("FROM"):
                if "latest" in line.lower():
                    self.findings.append("[WARNING] Base image uses 'latest' tag. Use specific versions.")
                if "scratch" in line.lower():
                    self.findings.append("[INFO] Base image is 'scratch'. Ensure minimal image is needed.")

    def check_user_instruction(self, dockerfile_lines: List[str]):
        if not any("USER" in line for line in dockerfile_lines):
            self.findings.append("[WARNING] No USER instruction found. Containers run as root by default.")

    def check_add_vs_copy(self, dockerfile_lines: List[str]):
        for line in dockerfile_lines:
            if line.strip().startswith("ADD"):
                self.findings.append("[WARNING] 'ADD' used instead of 'COPY'. 'COPY' is preferred unless needed.")

    def run_checks(self):
        dockerfile_content = self.load_config()
        lines = dockerfile_content.splitlines()
        self.check_base_image(lines)
        self.check_user_instruction(lines)
        self.check_add_vs_copy(lines)
        return self.findings

if __name__ == "__main__":
    checker = ContainerConfigChecker("Dockerfile")
    results = checker.run_checks()
    print("\nMisconfiguration Check Report:\n")
    for finding in results:
        print(finding)
