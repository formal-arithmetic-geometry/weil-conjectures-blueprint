+++
id = "proposition-base-change-fourier-inversion--3"
kind = "proposition"
title = "The fibre and stalk at a rational point"
name_showing = false
order = 1229004
aliases = ["bp-r379-3"]
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_comp_upperStar_rationalPointHom", "AlgebraicGeometry.nonempty_equiv_stalk_homologySheaf_fourierTransform_rationalPoint"]
uses = ["definition-weil-structure", "lemma-artin-schreier-character-sheaf", "definition-frobenius-operator"]
+++
Let $k_0$ be a finite field, let $\ell\ne\operatorname{char}(k_0)$ be prime,
and let $\psi:k_0\to\Qbarl^\times$ be an additive character. Write
$A=\mathbf A^1_{k_0}$ and $p:A\to\operatorname{Spec}k_0$.
For $a\in k_0$, let $i_a:\operatorname{Spec}k_0\to A^\vee$ be the
corresponding rational point. There is an isomorphism of functors on
bounded constructible Weil complexes on $A$,
$$
i_a^*\operatorname{FT}_\psi(-)
\simeq Rp_!\bigl(-\otimes\mathcal L_{\psi(ax)}\bigr)[1].
$$
Consequently, for every such complex $K$ and every $n\in\mathbf Z$,
there is a Frobenius-equivariant $\Qbarl$-linear isomorphism

$$
\bigl(\mathcal H^n(\operatorname{FT}_\psi K)\bigr)_{\bar a}
\simeq
H_c^{n+1}\bigl(\mathbf A^1_{\overline{k_0}},
K\otimes\mathcal L_{\psi(ax)}\bigr).
$$

Here $\bar a$ is a geometric point above $a$, with the local Frobenius
at $a$, and the right side carries the geometric Frobenius of $k_0$.
No nontriviality assumption on $\psi$ is needed. This is the rational-point
case on the line of the geometric stalk formula (16.2).
