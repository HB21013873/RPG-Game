from Text_Writing_Style import TypeWriter as TW
import sys
tw = TW(delay=0.02, jitter=True)
class Print_Type_Animation:
    def Print(*args, sep=" ", end="\n"):
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
