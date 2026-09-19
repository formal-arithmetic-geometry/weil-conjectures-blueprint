+++
id = "lemma-weil-pbc-spectral-restriction"
kind = "lemma"
title = "Zariski restriction on a spectral space"
order = 692
+++
If $T$ is spectral, $T_0\subseteq T$ is closed, and every irreducible closed
subset $C\subseteq T$ has $C\cap T_0$ connected and nonempty, then for every
abelian sheaf $F$ on $T$ the restriction $\Gamma(T,F)\to\Gamma(T_0,F|)$ is a
bijective map.

## Proof

Injectivity is pointwise. If $s\in\Gamma(T,F)$ restricts to zero, its germ
vanishes at every point of $T_0$. The zero-germ locus is open and stable under
generization. If its complement contained $x$, then the irreducible closed
$C=\overline{\{x\}}$ would meet $T_0$; the specialization map from the germ
at the generic point of $C$ to the germ at $x$ would force the latter to be
zero, a contradiction.

For surjectivity, write $F$ as the filtered colimit of subsheaves generated
by finitely many sections on quasi-compact opens. Restriction to $T_0$ and
both section functors commute with this filtered colimit, so it is enough to
handle one finitely generated subsheaf. Such a subsheaf embeds into a finite
product

$$
F\hookrightarrow\prod_{b=1}^r(i_b)_*\underline{M_b},
$$

with $i_b:C_b\hookrightarrow T$ closed and $M_b$ finite: the finite germs of
the chosen generators determine finitely many closed equalizer loci, and the
corresponding finite value sets give the displayed embedding. If $F\subseteq G$, the injectivity already proved gives

$$
\Gamma(T,F)=\Gamma(T_0,F|_{T_0})\cap\Gamma(T,G)
\subseteq\Gamma(T_0,G|_{T_0}).
$$

Thus it suffices to extend sections of one finite constant pushforward.

For $i:C\hookrightarrow T$ closed, the condition on irreducible closures is
inherited by $C$. A section of $\underline M$ on $C\cap T_0$ is constant on
each connected component. Every component of $C$ meets its closed subset,
and that intersection is connected by hypothesis, so the same constant gives
a unique section on the component. These componentwise sections agree on
quasi-compact overlaps and glue by the sheaf equalizer; pushing forward gives
the extension on $T$. Finite products, subobjects, and the filtered colimit
then give an extension for $F$. The stalkwise injectivity proves uniqueness,
so restriction is bijective. This is the expanded spectral argument at Tag
`09ZG`; no etale lifting is used.
