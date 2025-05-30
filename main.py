from pytm.pytm import TM, Datastore, Dataflow, Boundary, Actor, Lambda, Data, Classification

tm = TM("Student Voter System")
tm.description = "Activity 1 CSSECDV Group 5 - Cajumban, Larraquel, Pe, Santos, Singson"
tm.isOrdered = True

election_administrator = Actor("Election Administrator")
voter = Actor("Voter")
client_web_browser = Actor("Client Web Browser")