import magma as m
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('S1').input().on()
icestick.J1[1].rename('S2').input().on()
icestick.J1[2].rename('S3').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()

def fulladder(a,b,c):
    S = a ^ b ^ c
    C = (a&b) | (b&c) | (c&a)
    return S, C

S, C = fulladder(main.S1,main.S2,main.S3)

m.wire( S, main.D1 )
m.wire( C, main.D2 )

