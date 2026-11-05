+++
id = "proposition-fourier-transform-perverse-heart--2"
kind = "proposition"
title = "Preservation and reflection of curve perversity"
name_showing = false
order = 1260002
aliases = ["bp-r390-2"]
lean = ["AlgebraicGeometry.isCurvePerverse_fourierTransform_obj_iff"]
uses = ["lemma-artin-schreier-character-sheaf", "definition-weil-structure", "definition-perverse-sheaves-curve"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}k_0$ be prime, and let
$\psi:k_0\to\overline{\mathbf Q}_\ell^\times$ be a nontrivial additive
character. For a bounded constructible Weil complex $K$ on
$\mathbf A^1_{k_0}$,

$$
\operatorname{FT}_\psi K\text{ is curve perverse}
\quad\Longleftrightarrow\quad
K\text{ is curve perverse}.
$$

Curve perversity means that both cohomological conditions in
Definition [definition-perverse-sheaves-curve] hold: $K$ belongs to
${}^pD^{\le0}\cap{}^pD^{\ge0}$.
