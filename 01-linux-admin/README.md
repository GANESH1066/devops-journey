# Linux Administration Scenarios
## 1. Disk Full Troubleshooting
- Used `df -h` to identify the full partition.
- Used `du -sh * | sort -h` to locate the largest files.
- Learned difference between tmpfs and actual disk storage.

## 2. LVM Management
- Checked volumes using `pvs`, `vgs`, `lvs`.
- Extended disk space using `lvextend` and `xfs_growfs`.
