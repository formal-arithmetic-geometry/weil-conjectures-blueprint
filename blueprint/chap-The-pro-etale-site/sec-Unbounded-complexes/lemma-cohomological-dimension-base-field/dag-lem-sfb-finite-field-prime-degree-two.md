+++
id = "dag-lem-sfb-finite-field-prime-degree-two"
kind = "dag-lemma"
title = "Finite-field degree-two vanishing with constant prime coefficients"
name_showing = false
order = 159502
tags = ["sheaf-dag"]
split_from = "lemma-cohomological-dimension-base-field--1"
dag_id = "lem-sfb-finite-field-prime-degree-two"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["DiscreteModule.subsingleton_H_two_trivialZMod_of_finiteField"]
+++
Let K be a finite field, Ks a separable closure of K `def-pd-separable-closure`, and ell a prime nonzero in K. Put G = Gal(Ks/K) with its Krull topology. The degree-two continuous cohomology H²(G, Z/ell), for the trivial discrete action and with cohomology as in `def-exc-continuous-cohomology`, vanishes. In the Lean presentation this is Ext² from the trivial integer module in the category of discrete abelian G-modules; the coefficient group is ULift of ZMod ell in universe u+1.

(SHEAF DAG node `lem-sfb-finite-field-prime-degree-two`; machine-alignment layer.) Split from [lemma-cohomological-dimension-base-field--1]. DAG kind: statement. Placed through `sk-lem-base-field-cd` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-field-extension`.
