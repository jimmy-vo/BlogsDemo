# BlogsDemo
## Description
This is a demonstration of deploying a CRUD Sites using SQLLite Database and Flask Framework using Python.

## Features
```
* Login, registration.
* List of articles is available on any page.
* Create, read, update and delete posts:
  * Anyone (include guest users) is able to read posts.
  * Admin user is able to modify their posts or by normal user's posts.
  * Normal user is able to modify their posts but not other's posts.
```

## Demonstration:
* Main page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Main.JPG)
* Edit page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Edit.JPG)
* Login page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Login.JPG)
* Full-post page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Full.JPG)

## Non-functional requirements
```
* Implemented using PHP, CSS, Jquery, SQL- Relational Database.
* Deployed by MyPhpAdmin and XAMPP.
* Using Ajax on registration page for available usernames.
* Cookies or Sessions
* Implemented validation rules that are used on the data provided when creating and updating pages.
* Sanitized and validated the numericality of all ids retrieved from GET or POST parameters used in SQL queries.
* Sanitized all strings retrieved from GET or POST parameters to prevent HTML injection attacks.
```

## Relational Database
![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_ERD.png)

## Deployment Instruction
### Prerequisites
 * Download and install the latest version of XAMPP: [Download](https://www.apachefriends.org/download.html) 
 
### Deployment
 * Run XAMPP 
   * Start Apache
   * Start MySQL
 * On PhpMyAdmin (http://localhost/phpmyadmin/)
   * Create new database: "serverside"
   * Create new user:
     * username: "root"
     * password: ""
     * Global privileges: ALL PRIVILEGES
   * Execute the give database schema under [doc/setup.sql](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/setup.sql) 
 * Copy this project to C:\xampp\htdocs
 * Open http://localhost/RrcNews
