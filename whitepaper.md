# Table of Contents

1. Introduction
2. The problem
3. Overview
4. Protocol
5. What is an Action?
6. What is Data?
7. What is an Account?
8. Example
9. Security
10. Further information

## Introduction
As the world becomes increasingly more technology-driven, many businesses are seeking
secure solutions to maintain digital transparency with their customers.
Blockchain technologies like Ethereum, which allow decentralized, trustless systems for
applications to be built off of, have exploded in recent years.
Bullet Train is a simple but comprehensive framework that allows transparent, linked, and verifiable systems
to be built off of it.

The code contained in this repository contains code for the official Bullet Train node, and
also a simple command line application for testing.

## The problem

Digital transparency is harder than it should be. Ethereum is a way to make data 
shared and decentralized, but it is expensive, takes a significant amount of time to be processed,
and isn't ideal for businesses that want both security and transparency.

True digital transparency would allow both a corporation and an individual to easily access data that
verified the authenticity of a digital action taken. That's where Bullet Train comes in.

## Overview

Bullet Train is a network of linked computers. These computers are called nodes. Other computers that communicate
with nodes are called clients. All communication is done using TCP.

Nodes update information between each other, updating their local copy of the network graph. Updates to the
network graph don't conflict with other updates, meaning updates can happen out of order, which eliminates
the need for blocks and mining.
## Protocol

Messages sent between nodes are in JSON format. These include update-related messages and also discovery requests.

Messages sent between nodes and a client are also in JSON format.

A node stores data in a structure called the network state.
The network state is represented by a linked graph of Data, Accounts, and Actions.
Accounts are linked to one or more Action and/or Data objects.

A node also stores a list of nodes it knows about (via IP addresses). A node can request that it be added to that list,
and it can also request the list to locate other nodes.

## What is an Action?

An action is a signed piece of data that is stored digitally on a node. It is linked
It has several parts: the signed portion, the action hash, the ID, and the public key set.

The signed portion contains the signatures of the action, which
are signed by anyone that verifies it.
The action hash is a SHA256 hash of the original action.
The public key set is a list of public keys used in signing the transaction.
The ID is a SHA256 hash of the action hash + combined digital signatures.
It is used when looking up an action on a Nodes's action set.

An Action can also be located by filtering by an Account's public key.

After 3 days, the Action 'decays'. To reduce storage for the Node, the node takes the SHA256 of the action
and replaces the original action with this hash. Anyone with the original action can still verify that 
this action exists.

## What is Data?
Data is information about an Account. It is usually used as a way of linking the Account to an
external digital service or classifying it in a certain way.

Data is added by clients, which push a Data update to a node. That data update contains just three parts:
The data to be attached, it's corresponding digital signature (which must be signed by the private
key that relates to the Account), and the Account public key to attach the data to. 
This information is then communicated by the Node to other Nodes on the network.

Data is immutable and cannot be deleted. Usually, Data is encrypted by an external party before handing
it to the user that pushes it, so that only that entity can identify the relationship.

## What is an Account?

An account, in it's most simple form, is a public key of a private/public key pair. The private key
is unknown to the network, and is used for signing Data or Actions associated with an Account.

A node stores a list of Accounts that have Data or Actions attached to them. An Action is associated with
an Account via the public key set.
Data is associated with an Account via the public key component of it as well.

## Example
Client A is a digital payment handler, and Client B is a app on a phone that is sending a payment.
Nodes A and B are Bullet Train nodes run independently.

Here is an example scenario of the Bullet Train protocol in action:
1. Client A communicates with Client B and Client B signs a payment action requested
by Client A.
3. Client A signs this signed data with it's own private key, combines the signatures into a complete action, and then sends a push
request to Node A.
4. Node A validates the integrity of the action.
5. Then, Node A appends the action to it's action set, linking the Action to the Accounts associated with Client
A and B.
6. Node A pushes this Action to Node B. Node B verifies it and sends an update request to the Nodes
it knows.
7. Meanwhile, a bank's computer sends a request to Node B, to get a updated list of Actions from each of it's
users (it store public keys linked to accounts in it's server). Client B (who has an account with the bank)
has a new Action attached to it, so the bank analyzes it.
8. The original request to be signed has been separately sent from the digital payment handler to the
bank's computer, so the bank compares the hash of this against the Action, and also verifies the signatures
match. Seeing that Client B has agreed to this payment action, the bank performs a transfer of funds from
Client B's account.
9. Each client can also verify this action, as they can query a Node's action set, filtering by
their Account.

## Security

As part of Bullet Train's transparency, anyone can run a Bullet Train node.

Action objects are never stored in their original state, only as a hash, to prevent a malicious client
from receiving the original data, as some objects may contain sensitive information.

Though it isn't enforced, Data should also be encrypted/hashed to prevent other users from linking certain
information with an account.

Nodes also have settings that allow them to either blacklist or whitelist certain nodes if they detect
suspicious behavior such as invalid actions being send, or invalid network states.

## Further information

This project is currently under heavy development. Feel free to contribute!

Team:
    Jackson Lewis (Lead Developer/Engineer) : st.japa6@gmail.com