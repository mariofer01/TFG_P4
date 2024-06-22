from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

net.setLogLevel('info')
net.setCompiler(p4rt=True) #en caso de ejecutar 'net.setP4SourceAll' se compilaría el programa P4 directamente
#net.execScript('python3 controlador.py', reboot=True)

net.addP4RuntimeSwitch('s1')
net.addP4RuntimeSwitch('s2')
net.addP4RuntimeSwitch('s3')
net.addP4RuntimeSwitch('s4')
net.addP4RuntimeSwitch('s5')
net.addP4RuntimeSwitch('s6')
net.addP4RuntimeSwitch('s7')
net.addP4RuntimeSwitch('s8')
net.addP4RuntimeSwitch('s9')
net.addP4RuntimeSwitch('s10')


net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')

net.addLink("h1", "s1", port2=1)
net.addLink("s1", "s2", port1=2, port2=1)
net.addLink("s1", "s3", port1=3, port2=1)
net.addLink("s1", "s4", port1=4, port2=1)
net.addLink("s2", "s5", port1=2, port2=2)
net.addLink("s3", "s5", port1=2, port2=3)
net.addLink("s3", "s6", port1=3, port2=3)
net.addLink("s4", "s6", port1=2, port2=2)
net.addLink("s5", "h2", port1=1)
net.addLink("s5", "s7", port1=5, port2=2)
net.addLink("s5", "s8", port1=4, port2=2)
net.addLink("s6", "h3", port1=1)
net.addLink("s6", "s8", port1=4, port2=3)
net.addLink("s6", "s9", port1=5, port2=2)
net.addLink("s7", "s10", port1=1, port2=2)
net.addLink("s8", "s10", port1=1, port2=3)
net.addLink("s9", "s10", port1=1, port2=4)
net.addLink("s10", "h4", port1=1)

net.l3()

net.enablePcapDumpAll()
net.enableLogAll()
net.enableCli()
net.startNetwork()
