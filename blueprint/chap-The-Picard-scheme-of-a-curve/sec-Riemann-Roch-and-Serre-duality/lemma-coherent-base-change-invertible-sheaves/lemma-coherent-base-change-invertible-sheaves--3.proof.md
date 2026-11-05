+++
kind = "proof"
of = "lemma-coherent-base-change-invertible-sheaves--3"
order = 1530006
uses = ["lemma-coherent-base-change-invertible-sheaves--1", "lemma-coherent-base-change-invertible-sheaves--2"]
+++
The complexes of [lemma-coherent-base-change-invertible-sheaves--1]
give a local bound on the nonzero fibre cohomology groups and upper
semicontinuity of their dimensions. Thus the locus $U_i$ where all
degrees other than $i$ vanish is open. The fibre Euler characteristic
is locally constant, since it is the alternating sum of the ranks of
the terms of a finite free complex. On $U_i$ it is $(-1)^i$ times the
dimension in degree $i$. Its rank-$r$ locus $U_{i,r}$ is therefore open;
this is `AlgebraicGeometry.Scheme.Modules.isOpen_perfectLocusOfRank`.

Locally choose a finite free complex $P^\bullet$. The matrix criterion
`AlgebraicGeometry.Scheme.Modules.IsFiniteFreeComplex.exists_opens_range_subset_iff`
characterizes the open set on which pullbacks of $P^\bullet$ have
cohomology finite locally free of rank $r$ in degree $i$ and zero
elsewhere. Identify its residue-field condition with membership in
$U_{i,r}$, and use
[lemma-coherent-base-change-invertible-sheaves--2] to transfer the
criterion to the higher direct images on opens of $T'$. Vanishing and
finite local freeness then hold on $T'$ if $a(T')\subseteq U_{i,r}$.
Conversely, if the higher direct images on $T'$ have this form, restrict
to the inverse images of the opens on which $P^\bullet$ is defined and
apply the reverse implication of the same matrix criterion. It forces
every $a(t')$ to lie in $U_{i,r}$. This gives
`AlgebraicGeometry.Scheme.Modules.range_subset_perfectLocusOfRank_iff`.
Finally, a finite locally free module of rank one is invertible, giving
the stated specialization.
