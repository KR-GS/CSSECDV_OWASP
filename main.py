from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, Lambda, Data, Classification

tm = TM("Student Voter System")
tm.description = "Activity 1 CSSECDV Group 5 - Cajumban, Larraquel, Pe, Santos, Singson"

election_administrator = Actor("Election Administrator")

voter = Actor("Voter")

client_web_browser = Actor("Client Web Browser")

server = Server("Server")

student_voter_information = Datastore("Student Voter Information")

etherium = Server("Etherium")