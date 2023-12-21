# Overview #

The **Loops, conditions and parsing** project introduces very important devops concepts using bash, useful for server/data centre config, management and security. Its objectives are:
- Mastering how to create SSH keys.
- Understanding the advantage of using **#!/usr/bin/env bash** over **#!/bin/bash**.
- Understanding how to **while, until** and **for** loops.
- Mastering to use **if, else, elif** and **case** condition statements.
- Understanding how to use the **cut** command, and
- Knowing what are files and other comparison operators, and how to use them.


## Folder Details ###
- **Date Created:** Thur Dec 21 2023.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Thur Dec. 21, 2023 - 6am.
  - **1st Deadline:** Fri Dec. 22, 2023 - 6am.
  - **Duration:** 1 days.
  - **Month** 4, **Week** 3, **Day** 4.

<<<<<<< HEAD
# Technologies #
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- Code tested on Ubuntu 20.04 LTS.


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-RSA_public_key.pub](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub) | A public key for future uses. |
| 2. | [1-for_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/1-for_best_school)| A script that displays `Best School` 10 times.<ul><li>must use the `for loop` (`while` and `until` are forbidden).</li></ul>|
| 3. | [2-while_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/2-while_best_school)| A script that displays `Best School` 10 times.<ul><li>must use the `while loop`(`for` and `until` are forbidden).</li></ul>|
| 4. | [3-until_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/3-until_best_school)| A script that displays `Best School` 10 times.<ul><li>must use the *until loop* (`for` and `while` are forbidden).</li></ul>|
| 5. | [4-if_9_say_hi](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/4-if_9_say_hi)| A Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` *on a new line*.<ul><li>must use the `while loop` (`for` and `until` are forbidden).</li><li>must also use the `if `statement.</li></ul>|
| 6. | [5-4_bad_luck_8_is_your_chance](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance)| A Bash script that loops from 1 to 10 and:<ul><li>displays **`bad luck`** for the 4th loop iteration</li><li>displays **`good luck`** for the 8th loop iteration</li><li>displays **`Best School`** for the other iterations</li></ul>Requirements:<ul><li>must use the while loop (for and until are forbidden).</li><li>must use the if, elif and else statements</li></ul>|
| 7. | [6-superstitious_numbers](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/6-superstitious_numbers)| A Bash script that displays numbers from 1 to 20 and displays:<ul><li>**`4`** and then **`bad luck from China`** for the 4th loop iteration</li><li>**`9`** and then **`bad luck from Japan`** for the 9th loop iteration</li><li>**`17`** and then **`bad luck from Italy`** for the 17th loop iteration</li></ul>Requirements:<ul><li>must use the `while loop` (`for` and `until` are forbidden).</li><li>must use the `case` statement</li></ul>|
| 8. | [7-clock](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/7-clock)| A Bash script that displays the time for 12 hours and 59 minutes:<ul><li>displays hours from 0 to 12</li><li>displays minutes from 1 to 59</li><li>for each hour `Hour: n`is displayed, where `n` is the *number of hours so far*.</li></ul>Requirements:<ul><li>must use the `while loop` (`for` and `until` are forbidden).</ul>|
| 9. | [8-for_ls](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/8-for_ls)| A Bash script that displays: <ul><li>The content of the current directory *in list format(one line at a time)*</li><li>Where only the part of the name after the first dash('-') is displayed.<ul><li>e.g. **`1-for_best_school`** is displayed as **`for_best_school`** and **`file-for-test`** is displayed as **`for-test`**.</li></ul></li></ul>Requirements:<ul><li> must use the `for loop` (`while` and `until` are forbidden).<li>does not display hidden files.</li></ul>|
| 10. | [9-to_file_or_not_to_file](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/9-to_file_or_not_to_file)| A Bash  script that gives information about the *school* file.</br> Requirements:<ul><li>must use `if` and, `else` (`case` is forbidden).<li>the script checks if the file exists and prints:<ul><li>if the file exists: `school file exists`</li><li>if the file does not exist: `school file does not exist`.</li></ul></li><li>If the file exists, it prints: <ul><li>if the file is empty: `school file is empty`</li><li>if the file is not empty: s`chool file is not empty`</li><li>if the file is a regular file: `school is a regular file`</li><li>if the file is not a regular file, prints nothing.</li></ul></li></ul>|
| 11. | [10-fizzbuzz](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/10-fizzbuzz)| A Bash script that displays numbers from 1 to 100.Requirements:<ul><li>Displays *FizzBuzz* when the number is a **multiple of 3 and 5**<li>Displays *Fizz* when the number is a **multiple of 3**</li><li>Displays *Buzz* when the number is a **multiple of 5**</li><li>Otherwise displays the number</li><li>prints in a list format *(one number per line)*</li></ul>|
| 12. | [100-read_and_cut](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/100-read_and_cut)| A Bash script that script that displays the content of the `/etc/passwd` file.<ul><li>prints only the `<username>`, `<user_id>` and `<home_directory_path_of_user>`.</li></ul>Requirements:<ul><li>must use the while loop (for and until are forbidden)</li></ul>|
| 13. | [101-tell_the_story_of_passwd](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/101-tell_the_story_of_passwd)| A Bash script that script that displays the content of the file /etc/passwd, using the **while loop + IFS**.</br></br>Format:</br>```The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO```</br></br>Requirements:<ul><li>must use the while loop (for and until are forbidden)</li></ul>|
| 14. | [102-lets_parse_apache_logs](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/102-lets_parse_apache_logs)| A Bash script that script that displays the *visitor IP* along with the *HTTP status code* from the Apache log file.</br></br>Format:</br>`<ip_address> <status_code>`</br></br>Requirements:<ul><li>display is to be in *list* format *(one line at a time)*</li><li>must use the `awk` command</li><li>use of *while*, *for*, *until* and *cut* commands not allowed.</li><li>The file to be used is [apache-access.log file](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/apache-access.log)</li></ul>|
| 15. | [103-dig_the-data](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/103-dig_the-data)| A Bash script that script that groups visitors by IP and HTTP status code, and displays this data..</br></br>Format:</br>`<occurence_count> <ip_address> <status_code>`</br></br>Requirements:<ul><li></li>sort entries according to `<occurence_count`, in descending order.<li>display is to be in *list* format *(one line at a time)*</li><li>must use the `awk` command</li><li>use of `while`, `for`, `until` and `cut` commands not allowed.</li><li>The file to be used is [apache-access.log file](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/apache-access.log)</li></ul>|
=======
## Directories ###
- *Directories listed in order of project release*

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. |  |  |
| 2. | | |
>>>>>>> 71d8d22... docs(0x04): create directory and readme
