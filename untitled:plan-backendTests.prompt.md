## Plan: Add FastAPI backend tests

TL;DR - Create a new `tests/` directory and add Pytest backend tests for the FastAPI app in `src/app.py`. Use `TestClient` to validate the current API behavior and keep tests focused on the backend.

**Steps**
1. Add a new directory `tests/` at the repository root.
2. Create `tests/test_app.py` containing FastAPI backend tests.
   - Import `app` from `src.app` and build a `TestClient`.
   - Add tests for:
     - `GET /activities` returns the activity payload.
     - `POST /activities/{activity_name}/signup` successfully registers a new participant.
     - `POST /activities/{activity_name}/signup` returns 400 for duplicate signups.
     - `POST /activities/{activity_name}/signup` returns 404 for unknown activity names.
3. Optionally add `tests/conftest.py` if a reusable `client` fixture is preferred.
4. Ensure the existing `pytest.ini` at repo root is used by pytest.
5. If dependencies are missing, include `pytest` in `requirements.txt` or install it separately for the test environment.

**Relevant files**
- `/workspaces/skills-getting-started-with-github-copilot/src/app.py` — backend API under test.
- `/workspaces/skills-getting-started-with-github-copilot/pytest.ini` — existing pytest config.
- `/workspaces/skills-getting-started-with-github-copilot/requirements.txt` — may need a test dependency entry for `pytest`.

**Verification**
1. Run `pytest` from the repository root.
2. Confirm tests pass for API responses and duplicate signup behavior.
3. Optionally test with `python -m pytest tests/test_app.py`.

**Decisions**
- Use FastAPI `TestClient` instead of browser-based integration tests, since the request is specifically for backend tests.
- Keep tests in a dedicated `tests/` directory to separate them from application code.
- Do not change the API behavior in this plan; tests should validate the current routes and existing signup logic.
