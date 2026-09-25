+++
id = "thm-exc-curve-closed-preservation-general"
kind = "theorem"
title = "Closed exceptional images on arbitrary curves"
order = 1975
uses = ["def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-scheme-conventions", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "prop-exc-closed-tor", "thm-exc-curve-open-constructible-general", "thm-exc-curve-open-dimension-general"]
+++
Let $T$ be of finite type of dimension at most one over
a finite field or its algebraic closure. Let
$i:Z\hookrightarrow T$ be any closed immersion, and let
$A=A_{E,n}$, with $\ell$ invertible on $T$.
On the ordinary etale
derived categories,
the ambient right adjoint $Ri^!$ takes a bounded
constructible
object of Tor
amplitude $[a,b]$ to a bounded constructible object
of Tor amplitude $[a,b+2]$.

## Proof

Let $j$ be the complementary open immersion. The
geometric conditions needed for the support calculation
are now established: [thm-exc-curve-open-dimension-general]
gives $R^qj_*M=0$ for all module sheaves when $q>1$,
and [thm-exc-curve-open-constructible-general] gives
constructibility for all constructible inputs.
Use the actual ambient right adjoint of
[lem-exc-closed-ambient].
Tor amplitude $[a,b]$ implies the same cohomological
bound, by testing with $A$ in
[def-weil-finite-tor-amplitude].
The support triangle estimate in
[lem-exc-closed-amplitude], with $c=1$, gives
bounded constructible cohomology in $[a,b+2]$.
The constant coefficient and residue-field argument in
[prop-exc-closed-tor], with the same proved geometric
conditions and $c=1$, gives Tor amplitude $[a,b+2]$.
No smoothness, reducedness, or finiteness of the set
underlying $Z$ is required.
