+++
kind = "proof"
of = "lemma-simple-objects--1"
order = 1255001
uses = ["lemma-perverse-sheaves-curve", "lemma-largest-punctual-subsheaf", "lemma-simple-objects--2", "definition-constructible-sheaves"]
+++
For a simple $P$, the ordinary truncation triangle gives a
monomorphism $(\mathcal H^{-1}P)[1]\to P$ in the perverse full
subcategory. It is zero or an isomorphism, so either
$\mathcal H^{-1}P=0$ or $\mathcal H^0P=0$
(`AlgebraicGeometry.WeilComplex.isZero_homologySheaf_neg_one_or_zero_of_simple`).
In the first case $P\simeq(\mathcal H^0P)[0]$ is punctual.
The long exact cohomology sequence of a subobject of a punctual object
shows that its subobjects are precisely the ordinary subsheaves in
degree zero. Thus $G[0]$ is simple in the perverse full subcategory
exactly when $G$ is a simple Weil sheaf
(`AlgebraicGeometry.WeilComplex.simple_punctualObj_iff`).

In the second case $P\simeq F[1]$, where $F=\mathcal H^{-1}P$
has no nonzero punctual subsheaf. Choose a dense open on which $F$
is lisse. The unit $F\to j_*j^*F$ is injective and has punctual
cokernel $B$
(`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_mono_directImage`).
The rotated triangle gives a monomorphism $B[0]\to F[1]$ in the
perverse full subcategory. Simplicity and the nonvanishing of $F$
force $B=0$, so $P\simeq(j_*M)[1]$ with $M=j^*F$.
For a lisse subsheaf $M_1\subset M$, left exactness of $j_*$ embeds
$\operatorname{coker}(j_*M_1\to j_*M)$ into $j_*(M/M_1)$.
It therefore has no nonzero punctual subsheaf, by
[lemma-largest-punctual-subsheaf]. The resulting triangle makes
$(j_*M_1)[1]\to P$ a monomorphism in the perverse full subcategory.
Simplicity and $j^*j_*\simeq\id$ give $M_1=0$ or $M_1=M$
(`AlgebraicGeometry.WeilComplex.exists_middleExtension_of_simple`).

Conversely, let $P=(j_*M)[1]$ with $M$ irreducible lisse, and let
$Q\to P$ be a monomorphism in the perverse full subcategory. Its
cone $R$ is perverse by [lemma-perverse-sheaves-curve], and the long
exact cohomology sequence gives $\mathcal H^0R=0$ and

$$
0\longrightarrow\mathcal H^{-1}Q\longrightarrow j_*M
\longrightarrow\mathcal H^{-1}R\longrightarrow\mathcal H^0Q
\longrightarrow0.
$$

Apply [lemma-simple-objects--2]. Either
$\mathcal H^{-1}Q=\mathcal H^0Q=0$, so $Q=0$, or
$\mathcal H^{-1}R=0$, so $R=0$ and $Q\to P$ is an isomorphism
(`AlgebraicGeometry.WeilComplex.eq_zero_or_isIso_of_mono_middleExtension`).
Since $j^*j_*M\simeq M\ne0$, the object $P$ is nonzero and hence simple.
