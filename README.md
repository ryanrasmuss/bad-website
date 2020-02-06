# Bad Login & File Share Website

Work in progress.

* Store user information in database
* Encrypt the user information in database (bcrypt)
* Verify if username is in database
* Verify if username text and password text pass policy
* Session management (make sure user can't go to different url)

### Todo

* Session management

### Reminders

remember: ``sqlite3 login.db < schema.sql``


Table example (schema.sql):

```sql
drop table if exists users;

create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);
```
