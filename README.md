⚠️ *DEPRECATED* ⚠️ This connector is now built in to [opsdroid core](https://opsdroid.readthedocs.io/en/stable/databases/mongo/). This repository only exists for backward compatibility and will be removed.

# opsdroid database mongo

A database module for [opsdroid](https://github.com/opsdroid/opsdroid) to persist memory in a [mongo database](https://www.mongodb.com/).

## Requirements

None.

## Configuration

```yaml
databases:
  mongo:
    host:       "my host"     # (optional) default "localhost"
    port:       "12345"       # (optional) default "27017"
    database:   "mydatabase"  # (optional) default "opsdroid"
```
