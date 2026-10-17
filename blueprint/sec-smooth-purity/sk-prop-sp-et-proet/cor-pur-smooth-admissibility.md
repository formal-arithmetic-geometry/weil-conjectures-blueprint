+++
id = "cor-pur-smooth-admissibility"
kind = "theorem"
title = "Smooth morphisms satisfy the preservation clauses"
order = 2421
tags = ["latex:corollary"]
uses = ["cor-pur-dualizing-object-purity", "cor-sf-ambient-adjoint-discharge", "def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-ambient-exceptional-adjoint", "def-weil-constructible-intervals", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "lem-exc-residue-tor-test", "lem-weil-field-tor-amplitude", "prop-weil-pbc-inverse-image-exact", "prop-weil-twist-preserves", "thm-asd-smooth-tensor", "thm-cbc-finite-level-proetale", "thm-pur-diagonal-dualizing-object", "thm-sf-ambient-adjoint-class"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $f:X\to Y$ be smooth separated of pure relative dimension $d$.
Then $f$ satisfies the
two preservation clauses of
[def-weil-exceptional-adjoint-admissibility], with
$c_f^-=c_f^+=-2d$ in the signed convention of that definition:

1. *constructibility.* For all integers $a\leq b$,
$$
L\in D_c^{[a,b]}(Y,A)\quad\Longrightarrow\quad
Rf^!L\in D_c^{[a-2d,b-2d]}(X,A).
$$
1. *finite Tor amplitude.* If $K\in D^b_{ctf}(Y,A)$ has
finite Tor amplitude in
$[a,b]$, then $Rf^!K$ has finite Tor amplitude in
$[a-2d,b-2d]$; in particular $Rf^!$ carries $D^b_{ctf}(Y,A)$
into $D^b_{ctf}(X,A)$.

Thus every smooth morphism is
exceptional-adjoint admissible at $A=A_{E,n}$ in the constructible sense:
the preservation clauses of [def-weil-exceptional-adjoint-admissibility]
hold on the complexes of the blueprint's coefficient class. The ambient
exceptional right adjoint datum of [def-weil-ambient-exceptional-adjoint] is
not assumed: on the bounded constructible and finite-Tor coefficients that
the two clauses quantify over it is the theorem
[cor-sf-ambient-adjoint-discharge]. The unrestricted clause (1) of
[def-weil-exceptional-adjoint-admissibility], on all pro-étale sheaves, is
false in general and is not asserted. Admissibility at
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$ demands in addition the uniformity of the
two clauses over the finite stages and the finite-reduction and
scalar-extension compatibilities of the right adjoints. For smooth morphisms
these are [sk-thm-purity-transport] and [det-sp-purity-coefficient-change];
they are not asserted here.
