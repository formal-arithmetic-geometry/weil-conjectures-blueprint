+++
kind = "proof"
of = "theorem-cohomology-curves--1"
order = 360010
uses = ["lemma-sheaves-finite-support-finite-morphisms", "lemma-finite-morphisms-cohomology"]
+++
Give the finitely many irreducible components of $C$ their reduced
structures, with inclusions $c_i:C_i\to C$. Away from finitely many
closed points, the unit map
$$
F\longrightarrow\bigoplus_i c_{i,*}c_i^*F
$$
is an isomorphism, by invariance under universal homeomorphisms.
The finite-support calculation
[lemma-sheaves-finite-support-finite-morphisms] therefore makes it an
isomorphism on cohomology in degrees at least two. Finite direct image
[lemma-finite-morphisms-cohomology] reduces the assertion to integral
curves.

On an integral curve, replace $F$ in these degrees by
$\eta_*\eta^*F$, where $\eta:\Spec k(C)\to C$ is the generic point.
For a sheaf killed by an integer, the cohomological dimension bound for
$k(C)$ and dimension shifting with acyclic envelopes give vanishing
in degrees at least three. Finally, write a torsion sheaf as the
filtered union of its subsheaves killed by positive integers and use
commutation of cohomology with filtered colimits on the qcqs curve.
