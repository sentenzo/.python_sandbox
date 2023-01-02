<div align="center"> 

![diagram](diagram.png) </div>

## Description

Decorator allows to add extra functionality to the objects of some interface.

It allows to extend the class capabilities without inheritance.

### Examples

| Component    | `.do()`            | Decorator1    | Decorator2            |
| ------------ | ------------------ | ------------- | --------------------- |
| `Uploader`   | `.upload(file)`    | `Zip(comp)`   | `Encrypt(comp, pass)` |
| `Backupper`  | `.backup(db_name)` | `Zip(comp)`   | `Copy(comp, path)`    |
| `WebHandler` | `.handle(*pars)`   | `Cache(comp)` | `Log(comp, logger)`   |
