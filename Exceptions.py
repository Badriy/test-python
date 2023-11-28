try:
    x = [6,2,5,7,2]
    print(x[10])
except ZeroDivisionError:
    print("cant divied by zero")
except IOError:
    print()
except Exception as exc:
    print("error:" , type(exc))
finally:
    print("Done")
    