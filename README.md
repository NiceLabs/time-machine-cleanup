# Fuck Time Machine Cleanup

## Script

- By default, it erases all backups older than 30 days. Adjust as desired.

## Usage

```console
$ ./tm-cleanup.py
This script must be run as root!
$ sudo ./tm-cleanup.py
Removing old Time Machine Backups for older than 30 days, 0:00:00
Deleting: /Volumes/Time Machine Backups/Backups.backupdb/****/2021-01-18-045413
Deleted (349.3M): /Volumes/Time Machine Backups/Backups.backupdb/****/2021-01-18-045413
Total deleted: 349.3M
Elapsed time: 0:28:55.890715
Finished!
```

## References

- <https://gist.github.com/adamstac/1350066>
- <https://gist.github.com/appler1009/adf230249d1f1e983986b95756d37a77>
- <https://gist.github.com/blanboom/014654c2e1b858359fada810ca5215d4>
- <https://gist.github.com/ferthalangur/8e54880ba406e609dec2>
- <https://gist.github.com/linjer/a2da823718de9ba28373>

## LICENSE

[CC-0](LICENSE)
