+++
kind  = "proof"
of    = "prop-sf-open-closed-triangle-all-stages"
uses = ["lem-fin-extension-by-zero"]
+++
*The triangle.* The argument is the same for every $\Lambda$. Apply
[sk-prop-sf-open-closed-triangle] with $B=\Lambda_X=p_X^*\Lambda$. Its inverse
images are $i^*\Lambda_X=\Lambda_Z$ and $j^*\Lambda_X=\Lambda_U$, since
pullback of the condensed ring commutes with inverse image along $i$ and $j$
([det-def-sfb-pulled-back-coefficients]). The functors $i^*$, $i_*$, $j^*$,
$j_!$ on $\Lambda$-module sheaves are exact, so they act on complexes and pass
to derived categories without deriving. For a complex $M$ of
$\Lambda_X$-modules representing $K$, the termwise exact sequence

$$
0\longrightarrow j_!j^*M\longrightarrow M\longrightarrow i_*i^*M\longrightarrow0
$$

of [sk-prop-sf-open-closed-triangle] is a short exact sequence of complexes,
natural in $M$. It gives a distinguished triangle in
$D(X_{\mathrm{proét}},\Lambda)$, whose first two arrows are the counit of
$j_!\dashv j^*$ and the unit of $i^*\dashv i_*$
([prop-weil-open-closed-recollement-adjunctions]).

*Hom vanishing.* Since $j_!\dashv j^*$ is an adjunction of exact functors, it
persists on derived categories. Moreover $j^*i_*=0$: for $V\to U$ weakly étale,
$(i_*N)(V)=N(V\times_XZ)=N(\varnothing)=0$. Hence
$\operatorname{Hom}(j_!N[m],i_*M)=\operatorname{Hom}(N[m],j^*i_*M)=0$. Two
completions of the first two arrows differ by an automorphism $h$ of the third
vertex with $h-\operatorname{id}$ factoring through $i_*i^*K\to
j_!j^*K[1]$, hence through a zero map; so $h=\operatorname{id}$. The same
vanishing gives functoriality.

*Constructibility.* The pullback $j^*$ is exact and preserves constructible
sheaves, so $j^*K\in D^b_c(U,\Lambda)$. Since $D^b_c(X,\Lambda)$ is a
triangulated subcategory ([det-def-sfb-bounded-constructible]), containing $K$,
it suffices to show $j_!j^*K\in D^b_c(X,\Lambda)$; then $i_*i^*K$ is in it
as well. For $\Lambda=\mathcal O_E$ this is [sk-lem-integral-models], (3). For
$\Lambda=E,\Qlb$ one has $D^b_c=D^b_{ctf}$, and $j_!=Rj_!$ preserves
$D^b_{ctf}$ ([sk-thm-existence], (2)). For $\Lambda=A=A_{E,n}$ use the
étale comparison of [def-sf-setting]. Write $K\cong\nu_X^*G$ with $G$ a
bounded constructible complex on the étale site
([lem-sf-proetale-constructible-origin]); then $j_!j^{-1}G$ is bounded
constructible, since $j_!$ is exact and carries the constructible
cohomology sheaves of $j^{-1}G$ to constructible sheaves
([lem-fin-extension-by-zero];
[Tag 095X](https://stacks.math.columbia.edu/tag/095X)). The comparisons of
[lem-cbc-proetale-extension-zero-comparison] (for $j_!$),
[lem-weil-pbc-comparison-pullback] (for $j^*,i^*$) and
[prop-weil-pbc-comparison-direct-image] (for the finite, hence
quasi-compact, $i$), together with the exactness of $\nu_X^*$
([prop-weil-pbc-site-comparison-finite-level]), identify the triangle with
$\nu_X^*$ of the étale triangle $j_!j^{-1}G\to G\to i_*i^{-1}G\to$ of
[lem-cbc-open-closed-recollement].

*Weil structures.* The geometric Frobenius $g_X$ of
[def-weil-frobenius-detailed] restricts to $g_U$ and $g_Z$, and the squares
formed by $j$, $i$ and these automorphisms are cartesian. The exchange maps
of [fix-lem-exchanges] for these automorphism squares are isomorphisms
(their inverses come from the inverse squares), and they give the Weil
structures on $j_!$ and $i_*$; the pullbacks use $g_U^*j^*=j^*g_X^*$ and
$g_Z^*i^*=i^*g_X^*$. The counit and unit are equivariant, since the exchange
maps are built from, and paste with, the same units and counits
([fix-lem-exchanges]). Transporting the triangle along $g_X^*$ and the Weil
isomorphisms gives a distinguished triangle with the same first two arrows;
by the uniqueness above it has the same third arrow, which is therefore
equivariant.
