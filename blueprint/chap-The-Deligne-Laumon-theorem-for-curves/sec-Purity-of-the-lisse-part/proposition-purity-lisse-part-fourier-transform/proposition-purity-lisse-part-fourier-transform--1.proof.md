+++
kind = "proof"
of = "proposition-purity-lisse-part-fourier-transform--1"
order = 1280002
uses = ["proposition-fourier-transform-middle-extension", "lemma-artin-schreier-character-sheaf", "lemma-fourier-transform-boundary-sequence", "lemma-twisted-envelope", "theorem-grothendieck-lefschetz-trace-formula", "proposition-composition-base-change-rf-shriek", "theorem-purity-real-sheaves-curves", "corollary-unramified-boundary-point"]
+++
Choose a Fourier partner $M''$ which is nonzero irreducible and lisse,
as in Proposition [proposition-fourier-transform-middle-extension].
The dual $M^\vee$ is again irreducible and has no geometric constituent
of the excluded form for $\psi^{-1}$: duality carries
$\mathcal L_{\psi(ax)}$ to $\mathcal L_{\psi^{-1}(ax)}$.
Choose a Fourier partner of $M^\vee$ for $\psi^{-1}$ as well.
Lemma [lemma-fourier-transform-boundary-sequence] supplies correction
sequences for both partners.

On the product of the two lines put

$$
F=(p_1^*j_!M\otimes\mathcal K_\psi)
\oplus(p_1^*j_!M^\vee\otimes\mathcal K_{\psi^{-1}}).
$$

Since $M$ has weight zero, the local eigenvalues of its dual are the
complex conjugates of those of $M$. The character eigenvalues have
finite order, and the zero extensions have zero stalks at the boundary.
Thus $F$ is real, by the argument of Lemma [lemma-twisted-envelope].
This is `AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isReal_realifiedKernel`
with weight zero and twisting unit $1$.

The two correction sequences show that $R^\nu p_{2!}F=0$ for
$\nu\ne1$. Set $H=R^1p_{2!}F$. Compact-support base change
(Proposition [proposition-composition-base-change-rf-shriek]) identifies
its stalks with the degree-one compactly supported cohomology of the
fibres. The trace formula
(Theorem [theorem-grothendieck-lefschetz-trace-formula]) makes the traces
of all powers of Frobenius on this cohomology real; Newton identities
then make its local characteristic polynomials real. Consequently $H$
is real. This is
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isReal_higherLowerShriek_realifiedKernel`.

The direct-sum decomposition of $H$ and the first correction sequence
give an epimorphism $H\to j''_*M''$. Restrict to $U''_0$ using
$j''{}^*j''_*M''\simeq M''$, and then to a dense open $W\subseteq U''_0$
on which $H$ is lisse. The restriction $M''|_W$ remains irreducible,
and the kernel of this epimorphism is lisse. Hence
Theorem [theorem-purity-real-sheaves-curves], applied to this irreducible
quotient of a real lisse sheaf, makes $M''|_W$ pure of some real weight
$v$. Corollary [corollary-unramified-boundary-point] extends the purity
to $U''_0$. These are the steps of
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_isPunctuallyPureOfWeight_of_correction`.

Finally, both $(j'_*M')[1]$ and $(j''_*M'')[1]$ are the Fourier
transform of $(j_*M)[1]$, so taking cohomology in degree $-1$ gives
$j'_*M'\simeq j''_*M''$. Their stalks agree on the common dense open,
where $M'$ is therefore pure of weight $v$. Apply
Corollary [corollary-unramified-boundary-point] once more to extend
purity to all of $U'_0$. This transfer to the given Fourier partner is
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.IsFourierPartner.isPunctuallyPureOfWeight`.
