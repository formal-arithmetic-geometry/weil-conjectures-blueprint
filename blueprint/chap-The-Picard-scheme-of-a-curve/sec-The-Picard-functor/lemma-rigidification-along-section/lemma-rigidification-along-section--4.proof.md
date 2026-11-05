+++
kind = "proof"
of = "lemma-rigidification-along-section--4"
order = 1520008
uses = []
+++
Pullback commutes with tensor products and
$\sigma_T^*f_T^*\mathcal N\simeq\mathcal N$. Thus the pullback of the
normalization is

$$
\sigma_T^*\mathcal L\otimes(\sigma_T^*\mathcal L)^{-1}
\simeq\mathcal O_T.
$$

Lean makes this construction with the dual of $\sigma_T^*\mathcal L$
inside `AlgebraicGeometry.isSheaf_fpqc_picardFunctorNormalized`.

For uniqueness, pull the two given isomorphisms back along $\sigma_T$.
Writing $\mathcal A=\sigma_T^*\mathcal P$, this gives

$$
\mathcal O_T\simeq\mathcal A\otimes\mathcal N,
\qquad
\mathcal O_T\simeq\mathcal A\otimes\mathcal N'.
$$

Associativity and symmetry of tensor products identify $\mathcal N$
with $\mathcal N'$: both are tensor inverses of $\mathcal A$.
Pull this isomorphism back along $f_T$ and tensor with $\mathcal P$.
The original isomorphisms then identify $\mathcal L$ with
$\mathcal L'$, so their Picard classes are equal.
