+++
kind = "proof"
of = "proposition-multiplication-n--2"
order = 1503004
uses = ["lemma-abelian-variety-commutative", "proposition-multiplication-n--1"]
+++
By [proposition-multiplication-n--1], $A[n]$ is finite of rank
$n^{2g}$, where $g=\dim A$. It is a group scheme because $A$ is
commutative ([lemma-abelian-variety-commutative]) and $[n]$ is a
homomorphism.

A finite group scheme over a field of characteristic $p$ is étale
if $p$ does not divide its rank
(`AlgebraicGeometry.etale_of_not_dvd_finrankΓ`). This criterion is
proved by presenting the group scheme as the spectrum of a
finite-dimensional commutative Hopf algebra and applying
`HopfAlgebra.etale_of_not_dvd_finrank`.
If $p>0$, it is prime, and $p\nmid n$ implies $p\nmid n^{2g}$.
If $p=0$, the required condition says that $n^{2g}\ne0$, which
follows from $n>0$. Applying the criterion to $A[n]$ proves étaleness.
