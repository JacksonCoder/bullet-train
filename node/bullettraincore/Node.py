# from nodestate import NodeState
# from dbconnection import DBConn
# from utils import check_state, abort, DB_STATUS_FAILURE, NET_STATE_FAILURE, exit
# from network import NetworkState
def _main(args,path):
    #
    #
    # Step 1: Connect to db instance
    #
    #localDBInstance = DBConn.connect(path)
    #
    # Step 2: Check state of db
    #
    #ch = check_state(localDBInstance)
    #if not ch.stable():
    #   abort(ch.msg(),code=DB_STATUS_FAILURE)
    #
    # Step 3: Load network state into memory
    #
    # globalNetwork = NetworkState()
    # globalNetwork.load(localDBInstance.getNetwork())
    #
    # Step 4: Perform checks on network state
    #
    #if not globalNetwork.stable():
    #   abort(globalNetwork.error().msg(),code=NET_STATE_FAILURE)
    #
    #  Step 5: Establish connection with external Nodes
    #
    #conn = Communicator(583) # Connects on port 583
    #IPList = localDBInstance.getIPList()
    #conn.setup(IPList)
    #conn.verify()
    #
    # Step 6: Initialize NodeState
    #
    #ns = NodeState(localDBInstance,globalNetwork,conn)
    #
    # Step 7: Initialize NodeState thread dispatching
    #
    #ns.dispatch()
    #
    # Step 8: Connect NodeState to logger
    #
    #ns.connect_log(path)
    #
    # Step 9: Wait for exit
    #
    #ns.standby()
    #
    #
    # Step 10: Exit
    #
    #ns.close()
    #
    #exit()







    pass

class Node:
    def __init__(self,argstate):
        self.version = argstate.version
        self.dbpath = argstate.dbpath
    def Run(self):
        print("Starting up Bullet Train")
        #_main({"version":self.version},self.dbpath)

    def Exit(self):
        print("Exiting")