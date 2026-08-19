% Backward Chaining

fact(fly).
fact(cough).

rule(furry, [fly, cough]).
rule(rest, [fly]).
rule(doctor_visit, [furry, rest]).

backward_chaining(Goal) :-
    fact(Goal).

backward_chaining(Goal) :-
    rule(Goal, Conditions),
    prove_all(Conditions).

prove_all([]).

prove_all([Condition | Rest]) :-
    backward_chaining(Condition),
    prove_all(Rest).

start :-
    write('BACKWARD CHAINING'),
    nl,
    write('Enter goal: '),
    read(Goal),
    (
        backward_chaining(Goal)
        ->
        write('Goal can be proved from facts.')
        ;
        write('Goal cannot be proved from given facts.')
    ),
    nl.