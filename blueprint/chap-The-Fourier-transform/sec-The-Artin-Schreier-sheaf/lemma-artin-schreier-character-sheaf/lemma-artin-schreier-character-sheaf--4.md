+++
id = "lemma-artin-schreier-character-sheaf--4"
kind = "lemma"
title = "Normalization of multiplication"
order = 1217005
aliases = ["bp-r375-4"]
lean = []
uses = ["lemma-artin-schreier-character-sheaf--1", "lemma-artin-schreier-character-sheaf--2"]
+++
Lean bypasses this normalization clause: the multiplication theorem
asserts the existence of an isomorphism and does not assert its
compatibility with a chosen trivialization at zero.

The additional clause in the human statement is that the multiplication
isomorphism respects the specified trivializations at zero. The
isomorphism of [lemma-artin-schreier-character-sheaf--2] is used in the
Lean proof of Fourier inversion without this additional condition.
