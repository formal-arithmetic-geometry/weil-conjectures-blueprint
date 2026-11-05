+++
kind = "proof"
of = "proposition-fourier-inversion--1"
order = 1231003
uses = ["proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients", "lemma-artin-schreier-character-sheaf", "lemma-integral-linear-character", "proposition-extension-zero-restriction-closed-subscheme", "definition-tate-twists"]
+++
Write $(x,y,z)$ for the coordinates on $\mathbf A^3_{k_0}$, let
$r_{13}$ be the projection onto $(x,z)$, and let $p_1,p_2$ be the
projections from this plane. Put $r_1=p_1r_{13}$ and $r_3=p_2r_{13}$.
Base change and composition for $Rf_!$
([proposition-composition-base-change-rf-shriek]), together with the
projection formula and the tensor identity for the Artin–Schreier
sheaf ([lemma-artin-schreier-character-sheaf]), give

$$
\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)
\simeq Rr_{3!}\bigl(\mathcal L_{\psi((x-z)y)}\otimes r_1^*K\bigr)[1][1].
$$

This is `AlgebraicGeometry.nonempty_iso_fourierTransform_comp_fourierTransform_inv`.
It keeps the pulled-back complex inside the integral on the triple
product.

Let $\Delta:V\hookrightarrow\mathbf A^2_{k_0}$ be the diagonal.
The relative delta-kernel computation
`AlgebraicGeometry.WeilComplex.nonempty_iso_derivedLowerShriek_tensorLisse_artinSchreierOf_mul`,
applied to $h(x,z)=x-z$ and $P=p_1^*K$, gives

$$
Rr_{13!}\bigl(\mathcal L_{\psi((x-z)y)}\otimes r_{13}^*P\bigr)
\simeq R\Delta_!\bigl((\Delta^*P)(-1)[-2]\bigr).
$$

Indeed, over $x\ne z$ the integral vanishes by the relative form of
[lemma-integral-linear-character]. On the diagonal the character
sheaf is trivial, and the trace isomorphism for the trivial line
bundle gives $(\Delta^*P)(-1)[-2]$. The open–closed localization
isomorphism, underlying
[proposition-extension-zero-restriction-closed-subscheme], identifies
the integral with the direct image of this restriction.

Since $p_1\Delta=p_2\Delta=\mathrm{id}_V$, composition of pullbacks
and direct images now gives
$K(-1)[-2][1][1]$; this is the form recorded in
`AlgebraicGeometry.nonempty_iso_fourierTransform_comp_inv`. Cancelling
the shifts gives the displayed inversion formula. All these
isomorphisms are formed in the categories of Weil complexes.

Finally apply inversion to both $\psi$ and $\psi^{-1}$. The two
composites are isomorphic to the Tate twist $(-1)$, an equivalence
with inverse the twist $(1)$. The categorical criterion
`CategoryTheory.Functor.isEquivalence_of_comp_iso` therefore makes
$\operatorname{FT}_\psi$ an equivalence.
