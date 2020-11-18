from flask import Flask, jsonify, request, render_template

import block
import node
import wallet
import transaction

import json
import requests

app = Flask(__name__)

# This node private IP Address
MY_ADDRESS = '192.168.0.3' # TODO: This changes dynamically

# Bootstrap node address (we suppose it is known to everyone)
SERVER_ADDRESS = '127.0.0.1'

def setup_regular_node():
    # Create node and associate with VM via address
    myNode = node.Node(0, MY_ADDRESS)
    print(myNode)

    # Our node sends it's publik key (= wallet address = MY_ADDRESS ? )
    # and receives a unique id (0..NETWORK_SIZE) 
    print('http://' + SERVER_ADDRESS + ':5000/add_to_ring')
    r = requests.post('http://' + SERVER_ADDRESS + ':5000/add_to_ring', data = {'public_key':MY_ADDRESS})
    print(r)
    print(r.text)

setup_regular_node()