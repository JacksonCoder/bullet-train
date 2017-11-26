# Table of Contents

1. Introduction
2. Protocol
3. What is an Action?
4. What is an Account?
5. How does account registry work?
6. Example
7. Security
8. Further information

## Introduction
As the world becomes increasingly more technology-driven, many businesses are seeking
secure solutions to maintain digital transparency with their customers.
Blockchain technologies like Ethereum, which allow decentralized, trustless systems for
applications to be built off of, have exploded in recent years.
Bullet Train is a simple but comprehensive framework that allows transparent, linked systems
to be built off of it.

The code contained in this repository contains code for the official Bullet Train node, and
also a simple command line application for testing.


## Protocol

Bullet Train networks are localized, with clients that can relay signed data to the central node
and receive information about an account or action.

Messages sent between nodes are in JSON format. The only messages that can be sent are messages to update the 
Account registry.

Messages sent between nodes and a client are also in JSON format.

## What is an Action?

An action is a signed piece of data that is stored digitally on a node. 
It has several parts: the signed portion, the original action, the ID, and the key pair.

The signed portion contains the level I and II signatures of the action, which
are signed by the receiver and the requester, respectively.
The original action is a JSON object that contains data describing an action.
The ID is a SHA256 hash of the level II signature.
It is used when looking up an action on a database's action set.

An action can also be located by filtering by it's key pair, or the pair of public keys that identify the action's
requester and receiver, or just by one public key.

## What is an Account?

An Account is the identity of a client, or user of the Bullet Train system. Unlike Actions,
Accounts are not localized, and in fact shared with other nodes as part of a decentralized 
user registry. Accounts are linked to profiles on 3rd party sources, which can be verified only
by that designated 3rd party.

## How does account registry work?

If a client wishes to attach metadata (for example, a username for a external service or maybe a phone number) to their account, they send a request (as well as a signature
verifying that it is them). This metadata is added to the node's database and then broadcasted
to other nodes that it knows about.

## Example
Client A is a digital payment handler, and Client B is a app on a phone that is sending a payment.
Node A is a Bullet Train node run by the digital payment handler's company.

Here is an example scenario of the Bullet Train protocol in action:
1. Client A communicates with Client B and Client B signs a payment action requested
2. by Client A with a local private key which is linked to an account on Node A.
3. Client A signs this signed data, combines it into a complete action, and then sends a push
request to Node A.
4. Node A validates the integrity of the action.
5. Then, Node A appends the action to it's action set.
6. Meanwhile, a bank's computer sends a request to Node A to get an updated list of Actions taken
by a user with an account that is registered under Client B's Account (Client B has an account with that bank). It receives the new action
sees the new action as part of that list, and can independently verify this action.
7. Each client can also verify this action, as they can query Node A's action set, filtering by
their public key.

## Security
How can actions be tied to a 3rd party account without malicious users being able to verify it?
Simple: metadata pushed to an account is actually encrypted with the 3rd parties private key, meaning only 
they can decipher data about their users.

## Further information

This project is currently under heavy development. Feel free to contribute!

Team:
    Jackson Lewis (Lead Developer/Engineer) : st.japa6@gmail.com