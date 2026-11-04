+++
id = "prose-03-24"
kind = "hidden"
title = "Continuity of Ext (1)"
order = 276
+++
A morphism of $\overline{\mathbf Q}_\ell$-complexes should be defined over some finite
extension $E$ of $\mathbf Q_\ell$. Since $\QbarX=\varinjlim_EE_X$, this asks Hom out
of a constructible complex to commute with a filtered colimit. Here a
filtered colimit of complexes means the termwise colimit of a filtered
diagram of complexes of sheaves. We prove this continuity for complexes with
a common lower bound. It is the pro-étale analogue of the classical fact that
cohomology of a quasi-compact quasi-separated scheme commutes with filtered
colimits. Besides the descent to a finite coefficient field below, continuity
is used in two places. The first is the uniform bound for Ext groups. That bound
is proved first for integral lattices, so we need continuity for $\mathcal O_E$
as well. The second is the compactness argument for $E$ and $\overline{\mathbf Q}_\ell$
(Section [sec-Compactness-of-constructible-complexes]).

For cohomology and higher direct images the statement is
Corollary [corollary-continuity-cohomology], which holds for every sheaf of
rings. A constructible sheaf has a finite filtration by sheaves $a_!L$ with
$L$ lisse on a stratum $S$ (Lemma [lemma-constructible-sheaves](3)). Using
sections with support in a closed subscheme, we turn Hom out of $a_!L$ into
cohomology on $S$ of a complex built from the target by $Rj_*$ and
restrictions. The comparison then goes through a hypercohomology spectral
sequence. Because of the common lower bound, only finitely many of its
terms contribute to a given degree, and each of these terms commutes with
the colimit.
