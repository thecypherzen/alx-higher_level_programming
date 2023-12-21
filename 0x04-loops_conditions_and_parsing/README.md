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

# Technologies #
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- Code tested on Ubuntu 20.04 LTS.


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-RSA_public_key.pub](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub) | A public key for future uses. |
| 2. | [1-for_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/1-for_best_school)| A script that displays *Best School* 10 times.<ul><li>must use the *for loop* (while and until are forbidden).</li></ul>|
| 3. | [2-while_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/2-while_best_school)| A script that displays *Best School* 10 times.<ul><li>must use the *while loop* (for and until are forbidden).</li></ul>|
| 4. | [3-until_best_school](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/3-until_best_school)| A script that displays *Best School* 10 times.<ul><li>must use the *until loop* (for and while are forbidden).</li></ul>|
| 5. | [4-if_9_say_hi](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/4-if_9_say_hi)| A Bash script that displays *Best School* 10 times, but for the 9th iteration, displays *Best School* and then *Hi on a new line*.<ul><li>must use the *while loop* (for and until are forbidden).</li><li>must use the *if* statement.</li></ul>|
| 6. | [5-4_bad_luck_8_is_your_chance](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance)| A Bash script that loops from 1 to 10 and:<ul><li>displays **bad luck** for the 4th loop iteration</li><li>displays **good luck** for the 8th loop iteration</li><li>displays **Best School** for the other iterations</li></ul>Requirements:<ul><li>must use the while loop (for and until are forbidden).</li><li>must use the if, elif and else statements</li></ul>|
| 7. | [6-superstitious_numbers](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/6-superstitious_numbers)| A Bash script that displays numbers from 1 to 20 and displays:<ul><li>**4** and then **bad luck from China** for the 4th loop iteration</li><li>**9** and then **bad luck from Japan** for the 9th loop iteration</li><li>**17** and then **bad luck from Italy** for the 17th loop iteration</li></ul>Requirements:<ul><li>must use the while loop (for and until are forbidden).</li><li>must use the case statement</li></ul>|
| 8. | [7-clock](https://github.com/thecypherzen/alx-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/7-clock)| A Bash script that  displays the time for 12 hours and 59 minutes:<ul><li>display hours from 0 to 12</li><li>display minutes from 1 to 59</li><li>for each hour **Hour: <n>** is displayed, where *n* is the *number of hours so far*.</li></ul>Requirements:<ul><li>must use the while loop (for and until are forbidden).</ul>|
