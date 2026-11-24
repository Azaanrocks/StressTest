import subprocess
import sys
from pathlib import Path

from helpers.local_utils import init_local_context
from python_modules.ml_pipelines import load_vision_tensor, train_classifier_stub
from python_modules.web_scraper import fetch_mock_payload, parse_yaml_config
from python_modules.data_legacy import sanitize_legacy_records, verify_fallback_module


def main():
    init_local_context()
    load_vision_tensor()
    train_classifier_stub()
    fetch_mock_payload()
    parse_yaml_config()
    sanitize_legacy_records()
    verify_fallback_module()

    node_dir = Path(__file__).parent / "node_modules_test"
    subprocess.run(["node", str(node_dir / "api_client.js")], check=True)
    subprocess.run(["node", str(node_dir / "stream_worker.js")], check=True)


if __name__ == "__main__":
    main()
