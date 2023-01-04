import mumbler

def main():
    Mmb = mumbler.MumblerOptimized  # + 0 Mb
	# mumbler.MumblerUnoptimized # + 50 Mb
    mumblers = []
    while True:
        print("")
        inp = input(">> ")
        print("")
        if inp == "exit":
            break
        mumblers.append(Mmb(inp))
        for m in mumblers:
            m.mumble()

if __name__ == "__main__":
    main()
	
# >> A
# [Mumbler A]: (mumbles) Медленно и время обратной дороге я полагаю...

# >> B
# [Mumbler A]: (mumbles) Это меня больше чем она не могут 
#  «предупредить» о том что ваш номер на то ни нисходящие 
#  ни счастья той степени аналогична передачи информации и 
#  моралью .
# [Mumbler B]: (mumbles) По сравнению с чаем поскольку ни 
#  бога весны и время – его он представил ему и у аистов 
#  зябликов цихлид мы никогда не миротворцем
