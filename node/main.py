# This is the code run on the node startup

from bullettraincore import Node
import arghandler
def _main(nodestate):
    # Code that handles nodestate info goes here



    node = Node.Node(nodestate)
    # Main process
    node.Run()

    # Cleanup stage
    node.Exit()

    exit(0)
if __name__ == "__main__":
    _main(arghandler.handleNodeArgs())