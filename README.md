# eBPF filter to audit sensitive file access on head node

This repository contains eBPF filter to alert access to sensitive files and execute actions accordingly, e.g., drop network connections accordingly.

* Validating eBPF support (requires kernel >= 4.16)

Run printk.py to get a `kprobe` message from eBPF

* Sensitive file filter

Implementation in C and bpftrace (for testing). See `ssh_key_monitor.bpftrace` and `ssh_key_monitor.c`


An incomplete list of files tobe monitored are listed below: 

    /home/$USER/.ssh/authorized_keys
    /home/$USER/.ssh/id_rsa
    /home/$USER/.ssh/id_ed25519
    /home/$USER/.gnupg
    /etc/gshadow
    /etc/passwd
    /etc/shadow
    /etc/ssh/id_dsa
    /etc/ssh/id_ecdsa
    /etc/ssh/id_ed25519
    /etc/ssh/id_rsa
    /etc/ssh/known_hosts
    /etc/ssh/ssh_config
    /etc/ssh/sshd_config
    /root/.bash_history
    /var/log/auth.log

* Actions to be taken will be called separatedly on the host.

Currently, one action is listed

    drop_packets.bpftrace
