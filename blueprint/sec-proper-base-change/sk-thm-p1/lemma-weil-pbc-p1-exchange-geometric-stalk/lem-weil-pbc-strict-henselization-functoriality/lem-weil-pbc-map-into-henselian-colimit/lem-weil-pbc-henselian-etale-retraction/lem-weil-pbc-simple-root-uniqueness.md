+++
id = "lem-weil-pbc-simple-root-uniqueness"
kind = "lemma"
title = "A simple root in a local ring is unique in its residue class (Stacks 06RR)"
refines = "proof/lem-weil-pbc-henselian-etale-retraction"
lean = ["IsLocalRing.eq_of_eval_eq_zero_of_not_isUnit_sub"]
tags = ["sheaf-dag", "mathlib", "stacks-06RR"]
+++
Let $(R,\mathfrak m)$ be a local ring, $f\in R[T ]$ with derivative $f'$, and $a,b\in R$ with $f(a)=f(b)=0$, $a-b\in\mathfrak m$ and $f'(a)\notin\mathfrak m$. Then $a=b$.
