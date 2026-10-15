+++
kind = "proof"
of = "det-pbc-torsion-stalk-proetale-point"
+++
*(1)* A weakly étale $\Omega$-algebra is ind-étale, hence a filtered colimit
of finite products of copies of $\Omega$; so every affine object of
$P_{\mathrm{proét}}$ is $\operatorname{Spec}C(S,\Omega)$ for a profinite set
$S$ ($C(S,\Omega)$ the locally constant functions). Since $P$ is
quasi-compact, every pro-étale covering of $P$ is refined by a covering with a
single affine member $\operatorname{Spec}C(S,\Omega)\to P$ (a finite disjoint
union of affine members), with $S\neq\emptyset$, and such a map has a
section (choose a point of $S$). Hence an epimorphism of sheaves
$M\to N$ is surjective on sections over $P$: a section of $N$ over $P$ lifts
after such a covering, and pulling back along the section gives a lift over
$P$. So $\Gamma(P,-)$ is exact, and $R\Gamma(P,-)$ is computed termwise on
bounded below complexes.

*(2)* Every étale $\Omega$-scheme is a disjoint union of copies of $P$, so
$\Gamma(P_{\Et},-)$ is an equivalence from sheaves on $P_{\Et}$ to sets (and
to $\Lambda$-modules for module sheaves), with exact inverse
$N\mapsto\underline N$. The pullback $\nu_P^*\underline N$ is the
pro-étale sheaf associated with the presheaf
$\operatorname{Spec}C(S,\Omega)\mapsto\varinjlim N$ over étale maps, that is
$S\mapsto C(S,N)$ (locally constant functions), whose value on $P$ is $N$. As
$\nu_P^*$ and $\Gamma(P_{\mathrm{proét}},-)$ are both exact, the
identification extends termwise to complexes.

*(3)* The geometric stalk $(Rf_*K_{\mathrm{ét}})_{\bar y}$ is by definition
$\Gamma(P_{\Et},\bar y^{-1}Rf_*K_{\mathrm{ét}})$. By the comparison
isomorphisms $\bar y^*\nu_Y^*\simeq\nu_P^*\bar y^{-1}$ and
$\nu_Y^*Rf_*K_{\mathrm{ét}}\simeq Rf_*\nu_X^*K_{\mathrm{ét}}=Rf_*K$
([prop-weil-pbc-comparison-direct-image], $f$ being qcqs), and by (2), it is
$\Gamma(P_{\mathrm{proét}},\bar y^*Rf_*K)$. By proper base change for the
square with $g=\bar y$, transported to the pro-étale site as in
[lem-weil-pbc-transport-identifies-exchange], $\bar y^*Rf_*K\simeq
Ra_*i^*K$. Applying the exact functor $\Gamma(P_{\mathrm{proét}},-)$ of (1)
and composing derived global sections,
$\Gamma(P_{\mathrm{proét}},Ra_*i^*K)=R\Gamma(P_{\mathrm{proét}},Ra_*i^*K)
=R\Gamma(X_{\bar y,\mathrm{proét}},i^*K)$. The agreement with the étale
fibre isomorphism (for finite $\Lambda$ this is
[cor-weil-pbc-geometric-fiber-finite]) holds because every identification
used is induced by the comparison morphisms $\nu$, which are compatible with
units and counits.
