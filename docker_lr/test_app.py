import subprocess
import sys
from pathlib import Path


def test_app_prints_success_message():
	app_path = Path(__file__).with_name("app.py")
	result = subprocess.run(
		[sys.executable, str(app_path)],
		capture_output=True,
		text=True,
		check=True,
	)

	assert result.stdout.strip() == "DevOps Pipeline Debug Success"
