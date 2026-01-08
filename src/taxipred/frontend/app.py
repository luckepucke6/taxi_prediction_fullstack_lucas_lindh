from taxipred.backend.api import predict

def main() -> None:
    print(predict("  Hello Taxi  "))

if __name__ == "__main__":
    main()