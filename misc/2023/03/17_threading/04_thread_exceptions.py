import threading

def buggy_task():
    raise Exception('Something bad happened')


print("\nHow it works by default:\n")

thread = threading.Thread(target=buggy_task)
thread.start()
thread.join()

print("---")

print("\nHow you can castomize it:\n")
threading.excepthook = (
    lambda args: print(f'Thread failed: {args.exc_value}')
)

thread = threading.Thread(target=buggy_task)
thread.start()
thread.join()
print("---")