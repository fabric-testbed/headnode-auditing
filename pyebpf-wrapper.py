from socket import socket
import time
from pyebpf.ebpf_wrapper import EBPFWrapper


b = EBPFWrapper()

def hello(data, **kwargs):
    print('{pid} Hello, World!'.format(pid=data.process_id))

b.attach_kprobe(event=b.get_syscall_fnname('clone'), fn=hello)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
