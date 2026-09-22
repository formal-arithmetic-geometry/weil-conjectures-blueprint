+++
id = "fin4-prop-curve-family-betti"
kind = "theorem"
title = "Fibrewise cohomology of a smooth projective curve family"
order = 5220
tags = ["latex:proposition"]
lean = ["AlgebraicGeometry.Etale.fiberCohomology_card_of_smoothProper_curveFamily"]
uses = ["sbc-def-coefficient-conventions", "def-sbc-smooth-morphisms", "fin4-lem-stalk-constructibility-criterion", "def-weil-pbc-eight-curve-assertions"]
+++
Let $f:X\to S$ be a smooth proper [def-sbc-smooth-morphisms] morphism with
$S$ of finite type over $k$, whose geometric fibres are smooth separated
curves of genus $g_s$ per connected component, with $ncc_s$ connected
components; let $l$ be a prime and let $\underline{\mathbf Z/l}$ be the
constant sheaf on $X_{\Et}$. Then for every geometric point $\bar s$ of $S$,
$$
\bigl|H^q\bigl(X_{\bar s},\underline{\mathbf Z/l}\bigr)\bigr|=
\begin{cases}
l^{ncc_s},&q=0,\\
l^{2g_sncc_s},&q=1\ \text{and}\ l\neq\operatorname{char}\kappa(\bar s),\\
l^{\operatorname{p-rank}_s\,ncc_s},&q=1\ \text{and}\ l=\operatorname{char}\kappa(\bar s),\\
l^{ncc_s},&q=2\ \text{and}\ l\neq\operatorname{char}\kappa(\bar s),\\
1,&q=2\ \text{and}\ l=\operatorname{char}\kappa(\bar s),\\
1,&q>2,
\end{cases}
$$
where $\operatorname{p-rank}_s\leq g_s$ is the $p$-rank of the fibre
($l=p=\operatorname{char}\kappa(\bar s)$); in particular all these values
are finite. Moreover the functions
$s\mapsto|H^q(X_{\bar s},\underline{\mathbf Z/l})|$ are constructible on $S$
for every $q$.

## Proof

The fibre $C=X_{\bar s}$ is a smooth proper curve over the algebraically
closed field $\kappa(\bar s)$: the disjoint union of $ncc_s$ connected
components of genus $g_s$, identified with the stalk of
$R^qf_*\underline{\mathbf Z/l}$ by proper base change. The constant sheaf is
the direct sum of its restrictions to the components, so
$H^q(C_{\Et},\underline{\mathbf Z/l})$ is the direct sum over the components
and the computation is that of one connected component $C_0$.

*Good primes* ($l\neq\operatorname{char}\kappa(\bar s)$). Via the
trivialization by a primitive root of unity, the Kummer/Pic computation on a
proper curve gives $H^0=\mathbf Z/l$, $H^1=(\mathbf Z/l)^{2g_{C_0}}$,
$H^2=\mathbf Z/l$, and the vanishing above degree two (and the assertions $\mathcal C_1$, $\mathcal C_5$ of
[def-weil-pbc-eight-curve-assertions]); summing over the components
gives the first, third and fourth column values.

*Bad primes* ($l=p=\operatorname{char}\kappa(\bar s)>0$). The
Artin–Schreier exact sequence
$0\to\underline{\mathbf Z/p}\to\underline{\mathbf G_a}\to\underline{\mathbf G_a}\to0$
gives $H^0=\mathbf Z/p$,
$H^1(C_0,\mathbf Z/p)=\ker\bigl(\wp:H^1(C_0,\mathcal O)\to H^1(C_0,\mathcal O)\bigr)$
and $H^2=\operatorname{coker}(\wp)$, the cokernel being trivial by the
Lang–Steinberg surjectivity of $\wp$, with the vanishing above degree two
(the Artin–Schreier dimension bound and the assertion $\mathcal C_3$).

The kernel is finite: an $\mathbf F_p$-space of dimension the $p$-rank of
$C_0$, at most $g_{C_0}$ by the assertion $\mathcal C_5$; the same finiteness is visible
through the $p$-torsion group scheme of the Jacobian (finite flat of order
$p^{2g_{C_0}}$) and through the Artin–Schreier transfer: the covering
$\operatorname{Spec}\mathcal O[T]/(T^p-T-\cdot)$ of the Fourier–Deligne
chapter is finite étale of degree $p$ for the curve, and the finite transfer
together with the genus recursion $g(C'_0)=p(g_{C_0}-1)+1$ bounds the kernel
dimension. The values of the fibre are therefore finite: the second and
fifth column values.

*Constructibility of the values.* The genus $g_s$ is locally constant in the
smooth proper family (the cohomology comparison of the curve chapters: the
pullback maps are isomorphisms over algebraically closed field extensions;
equivalently the coherent Euler characteristic is locally constant), the
number of connected components $ncc_s$ is constructible (EGA IV, 9.7.9), and
in the bad-prime case the $p$-rank is constructible: the kernel dimensions
of the fibrewise $\wp$-operators of the smooth proper family are upper
semi-continuous, so the $p$-rank is constant on the open ordinary locus of
the smooth family and drops on the closed complement, giving a finite
constructible stratification.

Hence all displayed functions are constructible, the stalks of the sheaves
$R^qf_*\underline{\mathbf Z/l}$ are finite, and
[fin4-lem-stalk-constructibility-criterion] makes each
$R^qf_*\underline{\mathbf Z/l}$ constructible: $P$ holds for the smooth
proper curve families with constant $\underline{\mathbf Z/l}$-coefficients,
with the vanishing bound $R^qf_*=0$ for $q>2$ — the displayed value $1$ at
$q>2$ is the vanishing $H^q(C,\underline{\mathbf Z/l})=0$ of the
cohomological-dimension bound over the algebraically closed
$\kappa(\bar s)$, read through the base-change identification.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, def:weil-pbc-geometric-stalks, def:sc-genus, def:sc-curves, cor:weil-pbc-geometric-fiber-finite, thm:sc-proper-cohomology, thm:sc-affine-cohomology, lem:sc-cohomological-dimension, def:sc-mu-trivialization, lem:sc-as-sequence, lem:sc-lang-steinberg, lem:sc-isogeny-facts, lem:sc-mult-n-finite-flat, lem:fd-as-cover, thm:sc-constant-invariance, lem:sc-C1, lem:sc-C3, lem:sc-C5, lem:sc-artin-schreier-dimension
