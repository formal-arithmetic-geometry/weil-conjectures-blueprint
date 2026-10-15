+++
id = "det-curve-invariance-inseparable-closure"
kind = "lemma"
title = "Passage to the algebraic closure of a separably closed field"
uses = ["thm-weil-pbc-universal-homeomorphism-invariance", "lem-weil-pbc-universal-homeomorphism-base-change", "def-weil-pbc-curve-setting"]
+++
Let $k$ be a separably closed field with algebraic closure $\bar k$, let $C$
be a $k$-scheme, $u:C_{\bar k}\to C$ the projection, and $F$ an abelian sheaf
on $C_{\mathrm{ét}}$. Then $u$ is a universal homeomorphism and the pullback
maps

$$
H^q(C_{\mathrm{ét}},F)\longrightarrow H^q((C_{\bar k})_{\mathrm{ét}},u^{-1}F)
$$

are isomorphisms for all $q$. If $k\subseteq k'$ is a further separably
closed field and $\bar k\subseteq\bar k'$ are compatible algebraic closures,
then the square of pullback maps formed by $C_{\bar k'}\to C_{\bar k}\to C$
and $C_{\bar k'}\to C_{k'}\to C$ commutes.
