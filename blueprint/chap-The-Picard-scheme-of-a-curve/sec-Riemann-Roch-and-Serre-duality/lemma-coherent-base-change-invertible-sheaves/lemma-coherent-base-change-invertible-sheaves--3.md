+++
id = "lemma-coherent-base-change-invertible-sheaves--3"
kind = "lemma"
title = "The open locus of a finite locally free module in one degree"
name_showing = false
order = 1530003
aliases = ["bp-r477-3"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree"]
+++
Let $f:X\to T$ be proper and of finite presentation, and let $\mathcal F$
be an $\mathcal O_X$-module of finite presentation, flat over $T$.
For $i,r\geq0$, the locus
$$
U_{i,r}=\{t\in T:\ H^q(X_t,\mathcal F_t)=0\text{ for }q\ne i,
\quad \dim_{\kappa(t)}H^i(X_t,\mathcal F_t)=r\}
$$
is open. For every $a:T'\to T$, with cartesian base change
$f':X'\to T'$ and $b:X'\to X$, the morphism $a$ factors through
$U_{i,r}$ if and only if $R^qf'_*b^*\mathcal F=0$ for all $q\ne i$
and $R^if'_*b^*\mathcal F$ is finite locally free of rank $r$.

For $f_T:C_T\to T$, $\mathcal F=\mathcal L$, $i=0$ and $r=1$, this
gives the open locus on which the direct image is invertible and all
positive higher direct images vanish. The same condition holds after
every base change into this open locus.
