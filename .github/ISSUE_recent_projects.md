Title: Make Recent Projects dynamic & expose skills_list

Description:
We modified the project listing to make the "Recent Projects" section dynamic and to expose a cleaned list of skills for use in templates.

Files changed:
- app/projects/models.py
  - Added a `skills_list` @property that returns a cleaned list from the comma-separated `skills_required` field.
- app/templates/app/home.html
  - Replaced hardcoded sample project cards with a template loop over `recent_projects`, rendering title, truncated description, budget, and skill tags from `project.skills_list`.
- app/projects/views.py
  - Provide `get_all_projects` and `get_recent_projects` helpers that return QuerySets (used by `app.views.home`).
- app/views.py
  - Collects `all_projects` and `recent_projects` and renders `app/home.html` (wiring between views).

Motivation:
- Make the UI show real data instead of static example cards.
- Provide a convenient `skills_list` in the model for templates to iterate tags.

Acceptance criteria:
- `home.html` displays the recent projects returned by `get_recent_projects`.
- Each project's skills appear as tags from `project.skills_list`.
- No database file (`db.sqlite3`) is committed.

Notes:
- The change assumes `skills_required` is a comma-separated string (e.g., "django, react, api").
- I couldn't create a GitHub issue from this environment; I added this issue file and included it in the branch and PR so maintainers can copy it to GitHub issues if desired.
