class Program:
    language = "Python"

    def say_hello():
        print(f"Hello from {Program.language}!")

mapping_proxy = Program.__dict__

print(f"\n {mapping_proxy =}\n")

for k, v in mapping_proxy.items():
    print({f"{k} = {v}"})
print("")

Program.say_hello()
print("")
print(getattr(Program, "say_hello"))