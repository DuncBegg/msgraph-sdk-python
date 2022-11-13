from enum import Enum

class ImportedWindowsAutopilotDeviceIdentityUploadStatus(Enum):
    # No upload status.
    NoUpload = "noUpload",
    # Pending status.
    Pending = "pending",
    # Complete status.
    Complete = "complete",
    # Error status.
    Error = "error",

