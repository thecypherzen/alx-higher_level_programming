# Overview #

The **Processes and signals** project delves into process management using signals. Its objectives are to understand the following:
- What a PID is.
- What is a process.
- How to find a process' PID.
- How to Kill a process.
- What a signal is, and
- What 2 signals there are that cannot be ignored (or caught).


## Folder Details ###
- **Date Created:** Fri Dec 22 2023.
- **Author:** [William Inyam](https.//github.com/thecypherzen).
- **Project Timeline:**
  - **Released:** Fri Dec. 22, 2023 - 6am.
  - **1st Deadline:** Sat Dec. 23, 2023 - 6am.
  - **Duration:** 1 days.
  - **Month** 4, **Week** 3, **Day** 5.

# Technologies #
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- Code tested on Ubuntu 20.04 LTS.


## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-what-is-my-pid](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/0-what-is-my-pid) | A Bash script that displays its own `PID`. |
| 2. | [1-list_your_processes](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/1-list_your_processes) | A Bash script that displays a list of currently running processes.</br></br>Requirements<ul><li>Must show all processes, for all users, including those which might not have a `TTY`;</li><li>Must display in a user-oriented format; and</li><li>Must show process hierarchy</li></ul>|
| 3. | [2-show_your_bash_pid](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/2-show_your_bash_pid) | A Bash script that displays lines containing the word `bash`, thus allowing us to easily get the `PID` of our Bash process.</br></br>Requirements<ul><li>Must not use pgrep;</li><li>The third line of the script must be `# shellcheck disable=SC2009` (find more info about ignoring shellcheck error [here](https://github.com/koalaman/shellcheck/wiki/Ignore)). As for what the shellcheck code `SC2009` represents, check [here](https://github.com/koalaman/shellcheck/wiki/SC2009)</li></ul>|
| 4. | [3-show_your_bash_pid_made_easy](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/3-show_your_bash_pid_made_easy) | A Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.</br></br>Requirements<ul><li>Cannot use the `ps` command.</li></ul>|
| 5. | [4-to_infinity_and_beyond](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/4-to_infinity_and_beyond) | A Bash script that displays `To infinity and beyond` indefinitely.</br></br>Requirements<ul><li>In between each iteration of the loop, add a `sleep 2` command.</li></ul>|
| 6. | [5-dont_stop_me_now](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/5-dont_stop_me_now) | A Bash script that terminates the process [4-to_infinity_and_beyond](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/4-to_infinity_and_beyond) using the `kill` command.|
| 7. | [6-stop_me_if_you_can](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/6-stop_me_if_you_can) | A Bash script that terminates the process [4-to_infinity_and_beyond](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/4-to_infinity_and_beyond) without having to use the `kill` or `killall` commands. |
| 8. | [7-highlander](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/7-highlander) | A Bash script that:<ul><li>displays `To infinity and beyond` indefinitely with a `sleep 2` between each iteration;</li><li>displays `I am invincible!!!` when receiving a `SIGTERM` signal.</li></ul>|
| 9. | [67-stop_me_if_you_can](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/67-stop_me_if_you_can) | It's basically a copy of the script [6-stop_me_if_you_can](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/6-stop_me_if_you_can), but it sends a `SIGTERM` signal to [7-highlander](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/7-highlander) instead.|
| 10. | [8-beheaded_process](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/8-beheaded_process) | A Bash script that actually kills the process [7-highlander](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/7-highlander).|
| 11. | [100-process_and_pid_file](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/100-process_and_pid_file) | A Bash script that <ul><li>Creates the file /`var/run/myscript.pid` containing its `PID`;</li><li>Displays `To infinity and beyond` indefinitely;</li><li>Displays `I hate the kill command` when receiving a `SIGTERM` signal;</li><li>Displays `Y U no love me?!` when receiving a `SIGINT` signal</li><li>Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal.</li></ul>|
| 12. | [manage_my_process](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/manage_my_process) | A Bash script that:<ul><li>indefinitely writes `I am alive!` to the file `/tmp/my_process`; and</li><li>in between every `I am alive!` message, it pauses for `2 seconds`.</li></ul>|
| 13. | [101-manage_my_process](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/101-manage_my_process) | A Bash script that manages [manage_my_process](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/manage_my_process) above.</br></br>Requirements<ul><li>When passing the argument `start`:<ul><li>starts `manage_my_process`;</li><li>creates the file `/var/run/my_process.pid` containing its PID; and</li><li>displays `manage_my_process started`.</li></ul></li><li>When passing the argument `stop`:<ul><li>stops `manage_my_process`;</li><li>deletes the file `/var/run/my_process.pid` containing; and</li><li>displays `manage_my_process stopped`.</li></ul></li><li>When passing the argument `restart`:<ul><li>stops `manage_my_process`;</li><li>deletes the file `/var/run/my_process.pid` containing its PID;</li><li>starts `manage_my_process`;</li><li>creates the file `/var/run/my_process.pid` containing its PID; and</li><li>Displays `manage_my_process restarted`.</li></ul></li><li>displays `Usage: manage_my_process {start\|stop\|restart}`if any other argument or no argument is passed.</li></ul></br>*Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running. When doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started/running.*|
| 14. | [102-zombie.c](https://github.com/thecypherzen/alx-system_engineering-devops/tree/main/0x05-processes_and_signals/102-zombie.c) | A C program that creates 5 zombie processes.</br></br>Requirements<ul><li>For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`;</li><li>code must use the **Betty style**. It will be checked using `betty-style.pl` and `betty-doc.pl`; and</li><li>When it is done creating the parent process and the zombies, call the function bellow:
```
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
</li></ul>|
