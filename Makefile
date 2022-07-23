.PHONY: clean
clean:
	find . -name .mypy_cache -or -name .vscode -or -name __pycache__ -or -name .DS_Store | xargs rm -rf

.PHONY: win-clean
win-clean:
	 rmdir /s /q .vscode .mypy_cache
