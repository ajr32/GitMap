import os
from pathlib import Path


def create_sync_lock(repository_name):
    """Create a synchronization lock for the current process."""

    SYNC_LOCK_PATH.write_text(
        f"repository={repository_name}\npid={os.getpid()}\n",
        encoding="utf-8",
    )


def read_sync_lock():
    """Read the current synchronization lock."""

    if not SYNC_LOCK_PATH.exists():
        return None

    values = {}

    for line in SYNC_LOCK_PATH.read_text(encoding="utf-8").splitlines():
        key, _, value = line.partition("=")

        if key and value:
            values[key] = value

    if "repository" not in values or "pid" not in values:
        return None

    try:
        pid = int(values["pid"])
    except ValueError:
        return None

    return {
        "repository": values["repository"],
        "pid": pid,
    }


def is_process_running(pid):
    """Return True if a process with the given PID is still running."""

    try:
        os.kill(pid, 0)
    except OSError:
        return False

    return True


def acquire_sync_lock(repository_name):
    """Acquire the synchronization lock if no active sync owns it."""

    lock = read_sync_lock()

    if lock is not None:
        if lock["repository"] == repository_name and is_process_running(lock["pid"]):
            return False, lock

        # Existing lock is stale.
        SYNC_LOCK_PATH.unlink(missing_ok=True)

    create_sync_lock(repository_name)

    return True, None


def release_sync_lock():
    """Release the synchronization lock."""

    SYNC_LOCK_PATH.unlink(missing_ok=True)


SYNC_LOCK_PATH = Path(".gitmap-sync.lock")
