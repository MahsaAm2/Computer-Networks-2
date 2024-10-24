from mininet.topo import Topo

class Project( Topo ):
    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        # Add links
        self.addLink(h1,s1)
        self.addLink(s1,s2)
        self.addLink(s2,h2)
        self.addLink(s2,h3)
        self.addLink(s2,s3)
        self.addLink(s3,h4)
        self.addLink(s3,s4)
        self.addLink(s4,h5)
        self.addLink(s4,h6)
        self.addLink(s4,h7)
        self.addLink(s4,s5)
        self.addLink(s5,h8)
        self.addLink(s6,h10)
        self.addLink(s7,h11)
        self.addLink(s7,h9)
        self.addLink(s4,s7)
        self.addLink(s6,s7)
        self.addLink(s8,h12)
        self.addLink(s7,s8)

      

topos = { 'project': ( lambda: Project() )} 