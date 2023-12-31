import threading
t=threading.current_thread()
print('current thread :',t)
print('current thread name :',t.name)
print('current thread identifier :',t.ident)
print('current thread akive or not :',t.is_alive())
t.name='vishnu'
print('current thread name after change :',t.name)
