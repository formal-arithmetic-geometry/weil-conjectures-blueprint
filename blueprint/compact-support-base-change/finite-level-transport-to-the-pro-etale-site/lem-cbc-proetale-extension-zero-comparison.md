+++
id = "lem-cbc-proetale-extension-zero-comparison"
kind = "lemma"
title = "Comparison of extension by zero with the site morphism"
order = 6618
lean = ["AlgebraicGeometry.Proetale.comparison_extensionByZero"]
uses = ["lem-cbc-proetale-extension-zero", "lem-cbc-extension-zero-composition"]
+++
Let $\nu_X:X_{\Proet}\to X_{\Et}$ be the comparison morphism. For an open
immersion $j:U\hookrightarrow X$ and a finite commutative ring $\Lambda$ the
canonical comparison
$$
 \nu_X^*j^{\mathrm{et}}_!F\xrightarrow{\ \sim\ }j^{\mathrm{proet}}_!\nu_U^*F
$$
is an isomorphism for every sheaf $F$ of $\Lambda$-modules on $U_{\Et}$,
naturally in $F$ and compatible with composition of open immersions; here the
two $j_!$ are the etale and the pro-etale extension by zero.

## Proof

Both sides are left adjoints of functors to the sheaves on $U_{\Proet}$,
and we identify their right adjoints. The inverse image $\nu_X^*$ is left
adjoint to $\nu_{X*}$, and it is computed on the objects common to the two
sites; the functors $j^{\mathrm{et}}_!$ and $j^{\mathrm{proet}}_!$ are left
adjoint to the corresponding restriction along $j$. For a sheaf $M$ on
$X_{\Proet}$ the two Hom-functors in $F$ are therefore
$$
 \operatorname{Hom}\bigl(\nu_X^*j^{\mathrm{et}}_!F,M\bigr)
 \cong\operatorname{Hom}\bigl(j^{\mathrm{et}}_!F,\nu_{X*}M\bigr)
 \cong\operatorname{Hom}\bigl(F,j^{\mathrm{et},-1}\nu_{X*}M\bigr),
$$
$$
 \operatorname{Hom}\bigl(j^{\mathrm{proet}}_!\nu_U^*F,M\bigr)
 \cong\operatorname{Hom}\bigl(\nu_U^*F,j^{-1}M\bigr)
 \cong\operatorname{Hom}\bigl(F,\nu_{U*}j^{-1}M\bigr).
$$
The two right adjoints agree as functors to sheaves on $U_{\Et}$. Indeed, for
an etale $W\to U$ the under-category of etale $X$-schemes under $W$ has $W$
itself as initial object, because $W$ is etale over $X$ as a composite of
etale morphisms; hence both $j^{\mathrm{et},-1}\nu_{X*}M$ and
$\nu_{U*}j^{-1}M$ evaluate at $W$ to $M(W)$, the identification being the
restriction of sections along the open immersion $U\hookrightarrow X$. The two
Hom-functors in $F$ are therefore isomorphic, and by Yoneda the two left
adjoints are canonically isomorphic: this is the displayed comparison.
Naturality in $F$ and compatibility with a composite of open immersions follow
from the same identification of right adjoints, which is the restriction of
sections along an open immersion and is natural and transitive, as in
[lem-cbc-extension-zero-composition].

Unresolved dependencies: def:weil-pbc-site-comparison-morphism, def:weil-pbc-extension-by-zero, def:weil-extension-by-zero, def:weil-pbc-proetale-site
