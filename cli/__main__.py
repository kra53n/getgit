from sys import platform


if platform == "win32":
    from windows import main
if platform == "linux":
    from unix import main
main()
