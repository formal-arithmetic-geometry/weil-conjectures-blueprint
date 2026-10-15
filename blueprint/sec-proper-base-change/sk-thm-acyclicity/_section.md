+++
id = "sk-thm-acyclicity"
kind = "lemma"
title = "Acyclic resolutions"
order = 1050
lean = ["CategoryTheory.Functor.nonempty_rightDerivedObjIso_homology_of_acyclic"]
tags = ["sketch"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor between
abelian categories with enough injectives. If $F\to A^\bullet$ is a resolution
and each $A^m$ is $v$-acyclic, then

$$
\mathcal H^q(vA^\bullet)\simeq R^qvF.
$$

More generally, for a bounded below complex $A^\bullet$ of $v$-acyclic
objects, the canonical comparison $vA^\bullet\to Rv(A^\bullet)$ is an
isomorphism in $D^+(\mathcal B)$.
