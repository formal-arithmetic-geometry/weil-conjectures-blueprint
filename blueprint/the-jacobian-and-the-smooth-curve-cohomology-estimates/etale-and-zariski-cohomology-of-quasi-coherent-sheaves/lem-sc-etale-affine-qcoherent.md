+++
id = "lem-sc-etale-affine-qcoherent"
kind = "lemma"
title = "Étale acyclicity of a quasi-coherent module on an affine"
order = 4516
lean = ["AlgebraicGeometry.Etale.cohomology_eq_zero_of_isAffine_qcoherent"]
uses = ["def-sc-etale-qcoherent-module"]
+++
Let $X$ be an affine scheme and $\mathcal F$ a quasi-coherent module. Then
$H^q(X_{\mathrm{et}},\mathcal F_{\mathrm{et}})=0$ for $q>0$, with the
associated sheaf of [def-sc-etale-qcoherent-module].

## Proof

We induct on $q$, simultaneously for all affine schemes and all
quasi-coherent modules.

A class in positive sheaf cohomology vanishes on some covering: using an
injective resolution, represent it by a cocycle; exactness of that
resolution as a complex of sheaves means this cocycle is locally a boundary.
Refine the resulting étale covering by affine opens. Since étale maps are
open and $X$ is quasi-compact, finitely many such affine opens cover $X$.
Their disjoint union $V=\operatorname{Spec}(B)$ gives a faithfully flat
étale map to $X=\operatorname{Spec}(A)$.

All iterated fibre products $V\times_X\cdots\times_XV$ are affine. Their
sections of the sheaf of [def-sc-etale-qcoherent-module] are
$M\otimes_AB^{\otimes_A(p+1)}$, where $\mathcal F=\widetilde M$. The
associated Čech complex is exact in positive degrees.

For $q=1$, the Čech-to-cohomology spectral sequence identifies the kernel of
restriction to $V$ with a quotient of this zero Čech cohomology group. Hence
the class is zero. For $q>1$, the induction hypothesis kills every row of
that spectral sequence with cohomology degree strictly between $0$ and $q$.
Our class restricts to zero on $V$, so its only possible filtration piece
comes from the degree-$q$ Čech cohomology in row zero. That group is again
zero. This proves the induction.

Unresolved dependencies: lem:pc-cech-exact, lem:sc-cech-spectral
