+++
id = "sbc-lem-bc-failure-field"
kind = "lemma"
title = "A failure is detected on the generic fibre"
order = 5132
lean = ["AlgebraicGeometry.exists_field_counterexample_baseChange"]
uses = ["sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-bc-injectivity", "sbc-lem-bc-minimal-counterexample", "sbc-lem-thickening-etale-site", "sbc-lem-higher-direct-image-limit"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] assume for some
$q\geq1$ that $\mathrm{BC}(f,n,q-1)$ is true, but $\mathrm{BC}(f,n,q)$ is
not. Then there exist a commutative diagram
$$
\begin{array}{ccccc}
X & \longleftarrow & X' & \longleftarrow & Y\\
f\big\downarrow & & \big\downarrow f' & & \big\downarrow e\\
S & \longleftarrow & S' & \longleftarrow & \operatorname{Spec}K
\end{array}
$$
where $X'=X\times_SS'$, $Y=X'\times_{S'}\operatorname{Spec}K$, $K$ is a
field, and an abelian sheaf $\mathcal F$ on $\operatorname{Spec}K$
annihilated by $n$ such that
$$
f'^{-1}R^qg_*\mathcal F\longrightarrow R^qh_*e^{-1}\mathcal F
$$
is not an isomorphism.

(*Stacks Project, Lemma 59.88.6, [Tag
0F07](https://stacks.math.columbia.edu/tag/0F07).*)

## Proof

Choose a counterexample, i.e. a diagram with $T$ quasi-compact
quasi-separated and $\mathcal F$ annihilated by $n$ with the map of
[sbc-def-base-change-map] not an isomorphism; replace $S'$ by an affine
open, so $T$ is quasi-compact and quasi-separated. By
[sbc-lem-bc-injectivity] the map is injective, so there is a geometric point
$\bar x$ of $X'$ and an element $\xi$ of
$(R^qh_*e^{-1}\mathcal F)_{\bar x}$ not in the image of
$(f'^{-1}R^qg_*\mathcal F)_{\bar x}$.

For a morphism $\pi:T'\to T$ let $\mathcal F'=\pi^{-1}\mathcal F$ and define
$P(T')$ to be the property: the image $\xi'$ of $\xi$ in
$(R^qh'_*(e')^{-1}\mathcal F')_{\bar x}$ is not in the image of
$(f'^{-1}R^qg'_*\mathcal F')_{\bar x}$. We apply
[sbc-lem-bc-minimal-counterexample] to $P$.

*(1) Thickenings.* By [sbc-lem-thickening-etale-site] the étale site of a
scheme and of a thickening of it are the same, so the cohomology sheaves
involved are unchanged and $P(T'')$ iff $P(T')$.

*(2) Limits.* For $T'=\varprojlim T_i$ with affine transitions,
$\mathcal F'$ is the colimit of the pullbacks of $\mathcal F_i$, and
[sbc-lem-higher-direct-image-limit] gives
$\varinjlim R^qh'_{i,*}e_i^{-1}\mathcal F_i=R^qh'_*e'^{-1}\mathcal F'$ and
the analogue on the $g'$-side; hence $P(T_i)$ for all $i$ implies $P(T')$.

*(3) Closed–open split.* Let $T'$ satisfy $P(T')$ and let $Z\subset T'$ be
closed with quasi-compact complement $V$. Choose an injection
$j^{-1}\mathcal F'\to\mathcal J$ with $\mathcal J$ an injective sheaf of
$\mathbf Z/n\mathbf Z$-modules on $V$, where $j:V\hookrightarrow T'$; then
$\mathcal F'\to j_*\mathcal J\oplus i_*i^{-1}\mathcal F'$ is injective
(with $i:Z\hookrightarrow T'$ the closed immersion), so by
[sbc-lem-bc-injectivity] the image of $\xi'$ is nonzero in the direct-sum
cokernel for $\mathcal G=j_*\mathcal J\oplus i_*i^{-1}\mathcal F'$.

If it is nonzero in the second summand, then, since $i_*$ (also $i'_*$) is
exact for closed immersions,
$R^qg'_*i_*i^{-1}\mathcal F'=R^q(g'\circ i)_*i^{-1}\mathcal F'$ and
$R^qh'_*e'^{-1}i_*i^{-1}\mathcal F'=R^qh''_*e_Z^{-1}i^{-1}\mathcal F'$ by
the Grothendieck spectral sequence, so $P(Z)$ holds.

If it is nonzero in the first summand, then
$e'^{-1}j_*\mathcal J=j'_*e_V^{-1}\mathcal J$, and by $\mathrm{BC}(f,n,q-1)$
applied to the square over $V$ together with the injectivity of
$\mathcal J$, the higher direct images $R^aj'_*e_V^{-1}\mathcal J$ vanish
for $a=1,\dots,q-1$; the relative Leray spectral sequence for
$h'\circ j'$ shows
$$
R^qh'_*e'^{-1}j_*\mathcal J\longrightarrow R^q(h'\circ j')_*e_V^{-1}\mathcal J
$$
is injective, and applying [sbc-lem-bc-injectivity](3) to
$j^{-1}\mathcal F'\subset\mathcal J$ gives $P(V)$.

By [sbc-lem-bc-minimal-counterexample], $P(\operatorname{Spec}K)$ holds for
some field $K$, which is the assertion.
