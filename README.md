## 🚀 Multithreaded Web Proxy Server

Python-based proxy server with content filtering and LRU caching.


## Team: Titans

### Team Members
1. Harshitha Sajith Menon (24BYB1166)
2. Priyadharshini S (24BYB1068)

---

## Project Description

This project implements a multithreaded web proxy server that performs two major functions:

1. Content Filtering  
Blocks access to unauthorized websites using an Access Control List (ACL).

2. Web Caching  
Implements a Least Recently Used (LRU) caching algorithm to store frequently accessed web resources locally.

---

## Features

• Multithreaded proxy server  
• Website blocking system  
• LRU caching mechanism  
• HTTP request parsing  
• Traffic logging

---

## Technologies Used

Python  
Socket Programming  
Multithreading  
HTTP Protocol

---

## Expected Output

Blocked websites → 403 Forbidden page  
Cached requests → served from proxy cache  
New requests → fetched from remote server
