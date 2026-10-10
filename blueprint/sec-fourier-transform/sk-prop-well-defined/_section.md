+++
id = "sk-prop-well-defined"
kind = "section"
title = "P2: the transform is an exact triangulated functor"
order = 2696
lean = ["AlgebraicGeometry.Etale.boundedConstructible_fourierTransform_obj_of_boundedConstructible", "AlgebraicGeometry.Etale.fourierTransformBoundedConstructible"]
uses = ["sk-def-ft", "sk-prop-kernel-lisse"]
+++
*Proposition (sketch).*

Let $\Lambda$ be a finite commutative ring in which $p$ is invertible and
whose exponent is invertible on $S$, let $p_2$ be of finite type and
admit a compactification, and let $V'$ be locally of finite type over a
field. For every $K\in\Dbc(V,\Lambda)$ one has
$\FT_\psi(K)\in\Dbc(V',\Lambda)$, so $\FT_\psi$ restricts to a functor
$\Dbc(V,\Lambda)\to\Dbc(V',\Lambda)$.

## Proof

By P1 the kernel is lisse of rank one, hence of finite Tor amplitude, so
$p_1^*K\otimes^L\mathcal K_\psi\in\Dbc(V\times_SV^\vee,E)$. By the
six-operations package prop:functor-package the derived pullback, the
derived tensor product and the compact-support direct image along the
separated finite-type $p_2$ are exact triangulated functors on their
constructible and finite-Tor domains, and they preserve bounded
constructible objects; the shift $[r]$ does too.
