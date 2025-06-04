from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, Lambda, Data, Classification    

tm = TM("Student Voter System")
tm.description = "Activity 1 CSSECDV Group 5 - Cajumban, Larraquel, Pe, Santos, Singson"


#Boundaries
dependcies = Boundary("dependencies")


#Blocks
election_administrator = Actor("Election Administrator")

voter = Actor("Voter")

client_web_browser = Actor("Client Web Browser")
client_web_browser.inBoundary = dependcies

server = Server("Server")

student_voter_information = Datastore("Student Voter Information")

etherium = Server("Etherium")

#Election administrator dataflows
reg_candidates = Dataflow(election_administrator, client_web_browser, "Register candidates")

reg_voters = Dataflow(election_administrator, client_web_browser, "Register voters")

logs_in = Dataflow(election_administrator, client_web_browser, "Logs_in")

#Client browser dataflows
display_log_in_voter = Dataflow(client_web_browser, voter, "Displays log in status")

enable_export_perms = Dataflow(client_web_browser, election_administrator, "Enables exporting permissions")

generates_new_pass = Dataflow(client_web_browser, election_administrator, "Generates new password")

display_log_in_admin = Dataflow(client_web_browser, voter, "Displays log in status")

send_credentials = Dataflow(client_web_browser, server, "Sends Credentials")

submit_candidate_info = Dataflow(client_web_browser, server, "Submits candidate information")

submit_voter_info = Dataflow(client_web_browser, server, "Submits new voter information")

send_filter_ballot = Dataflow(client_web_browser, voter, "Sends filtered ballot")

req_auth_client = Dataflow(client_web_browser, voter, "Requests authentication")

send_filter_ballot_client = Dataflow(client_web_browser, server, "Sends filtered ballot")

#Voter dataflows
answered_Ballot = Dataflow(voter, client_web_browser, "Answers Ballot")

log_in_voter = Dataflow(voter, client_web_browser, "Logs in")

send_auth_voter = Dataflow(voter, client_web_browser, "Sends authentication")

#Server dataflows

returns_auth_server = Dataflow(server, client_web_browser, "Returns authentication")

req_auth = Dataflow(server, etherium, "Requests authentication")

store_candidate_info = Dataflow(server, student_voter_information, "Stores Candidates information")

gen_keys = Dataflow(server, student_voter_information, "Generate public & private keys for each voter")

store_voter_cred = Dataflow(server, student_voter_information, "Stores voter credentials")

send_filter_ballot_server = Dataflow(server, client_web_browser, "Sends filtered ballot")

record_transaction = Dataflow(server, etherium, "Records transactions")

create_signed_ballot = Dataflow(server, server, "Creates sigened ballot")

req_keys = Dataflow(server, student_voter_information, "Requests public and private keys")


#Etherium Dataflow
returns_auth_eth = Dataflow(etherium, server, "Stores Candidate Info")

#Student Voter Info

send_keys = Dataflow(student_voter_information, server, "Sends public and private keys")

send_ballot_info = Dataflow(student_voter_information, server, "Sends ballot info")