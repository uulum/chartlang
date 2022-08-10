from .chartlang import chartlang
import datetime


def main():
    code = 1
    while code != "x":
        try:
            prompt = datetime.datetime.utcnow().isoformat()
            code = input(f"CHARTLANG {prompt} >> ")
            code = code.strip()
            if code != "" and code != "x":
                chartlang(code)
        except EOFError as eof:
            print("Exiting...", eof)
            break
        except Exception as err:
            print(err)

if __name__ == "__main__":
    main()
