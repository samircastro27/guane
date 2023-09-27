from typing import Any, Callable, Mapping

from fastapi import FastAPI


class DependencyOverrider:
    """
    Allows to override the fastapi dependencies inside a cleanable context.
    Taken from https://github.com/pksol/pytest-fastapi-deps.
    Args:
        app: the fastapi app
        overrides: a dictionary of the override mappings where the key is the
            original function and the value is the replacement function.
    """

    def __init__(self, app: FastAPI, overrides: Mapping[Callable, Callable]) -> None:
        self.overrides = overrides
        self._app = app
        self._old_overrides = {}  # type: ignore

    def __enter__(self):
        for dep, new_dep in self.overrides.items():
            if dep in self._app.dependency_overrides:
                # Save existing overrides
                self._old_overrides[dep] = self._app.dependency_overrides[dep]
            self._app.dependency_overrides[dep] = self._callable_replacement(new_dep)
        return self

    @staticmethod
    def _callable_replacement(new_dep):
        return new_dep if callable(new_dep) else lambda: new_dep

    def __exit__(self, *args: Any) -> None:
        for dep in self.overrides.keys():
            if dep in self._old_overrides:
                # Restore previous overrides
                self._app.dependency_overrides[dep] = self._old_overrides.pop(dep)
            else:
                # Just delete the entry
                del self._app.dependency_overrides[dep]


class FixtureDependencyOverrider:
    def __init__(self, app: FastAPI):
        self.app = app

    def override(self, overrides: Mapping[Callable, Callable]):
        return DependencyOverrider(self.app, overrides)
