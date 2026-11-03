+++
id = "prose-05-07"
kind = "hidden"
title = "Continuity of cohomology and of Ext"
order = 244
+++
Cohomology, and Hom out of a constructible complex, commute with
filtered colimits of complexes that have a common lower bound. Here a filtered
colimit of complexes means the
termwise colimit of a filtered diagram of complexes of sheaves. This is the
pro-étale analogue of the classical fact that cohomology of a
quasi-compact quasi-separated scheme commutes with filtered colimits. We use it
in the descent to a finite coefficient field below, in the uniform
bound for Ext groups, and in the compactness argument for $E$ and $\overline{\mathbf Q}_\ell$
(Section [sec-compactness]). Since the uniform bound for Ext groups is proved
first for integral lattices and then transported to $E$ by inverting $\pi_E$,
we need it for $\mathcal O_E$ as well as for $E$ and $\overline{\mathbf Q}_\ell$.

The common lower bound is what makes the argument work. We compute Hom out
of $a_!L$ as cohomology on the stratum $S$ of a complex built from the
target by $Rj_*$ and restrictions, and we compare the two sides by a
hypercohomology spectral sequence. For complexes bounded below uniformly,
only finitely many terms of this spectral sequence contribute to a given
degree, and each term commutes with the colimit.

For cohomology and higher direct images the statement is
Corollary [sk-cor-pe-bounded-continuity], which holds for every sheaf of
rings. We apply it both to $R\Gamma$ on a stratum and to $Rj_*$ for an
open immersion $j$.

By Lemma [sk-lem-coefficient-heart](3), a constructible sheaf with
coefficients $E$ or $\overline{\mathbf Q}_\ell$ has a finite filtration whose subquotients
are of the form $a_!L$, with $a:S\hookrightarrow X$ locally closed and
$L$ lisse on $S$. To reduce statements about $R\!\operatorname{Hom}(a_!L,-)$ to
cohomology on $S$, we use sections with support in a closed subscheme.
