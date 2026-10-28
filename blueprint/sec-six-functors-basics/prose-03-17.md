+++
id = "prose-03-17"
kind = "hidden"
title = "Plan of the proof"
order = 2801
+++
Compactness of a constructible complex $C$ means that $\Hom(C,-)$ commutes
with direct sums. The difficulty is that the summands may have cohomology
in unboundedly many degrees. Since, on the strata of a finite
stratification, $C$ is locally of the form $\Lambda_S\otimes P$ with $P$
perfect, and by continuity of cohomology, the groups
$\operatorname{Ext}^q(C,-)$ commute with filtered colimits and vanish above a degree
that depends only on $C$. Lemma [sk-lem-brown-hypotheses] collects the
three cases (finite rings, fields and $\mathcal O_E$).

To define $Rf_!$ we choose, by Nagata's theorem
(Theorem [sk-thm-nagata-compactification]), a compactification $f=pj$ and put
$Rf_!=Rp_*j_!$. This functor preserves direct sums because $p$ has finite
cohomological dimension, and proper base change shows that it does not
depend on the compactification. By Brown representability we then
obtain $f^!$ for every admissible coefficient ring, including finite rings
(Theorem [sk-prop-sf-existence]).

For (4), since every morphism factors locally as a closed immersion
followed by the projection of an affine space, it suffices to treat these
two cases. For the projection, the trace on $\mathbf P^1$ makes the
adjunction explicit, and $f^!$ is locally $f^*(d)[2d]$. For a closed
immersion, $f^!$ is local cohomology, which is constructible because
$Rj_*$ preserves constructibility for open immersions $j$; this last fact
is in turn deduced from the case of the projection. With finite
coefficients one also checks finite Tor amplitude, by the projection
formula. For finite rings and for the $\ell$-adic rings $\mathcal O_E$, $E$
and $\overline{\mathbf Q}_\ell$ this is carried out in Theorems [sk-prop-sf-rf-shriek-preservation]
and [sk-thm-restriction], respectively. The global isomorphism
$f^!\simeq f^*(d)[2d]$ for smooth $f$, compatible with trace and
composition, is smooth purity (Section “Smooth purity”); its
compatibility with Frobenius is in Section “Frobenius and Weil complexes”.
