from threading import Timer


# 可重复执行的timer，原timer只会执行一次
class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
