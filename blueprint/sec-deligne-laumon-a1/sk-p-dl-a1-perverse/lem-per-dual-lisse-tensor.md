+++
id = "lem-per-dual-lisse-tensor"
kind = "lemma"
title = "Dual of a lisse tensor"
lean = ["AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_verdierDual_tensor"]
order = 3084
uses = ["def-trf-dualizing-complex", "sk-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "def-weil-pbc-scheme-conventions", "def-wf-tate-twist", "fix-lem-tensor-adjunction"]
+++
Let $X$ be
smooth of pure dimension
$d$, let $K\in D^b_c(X,\overline{\mathbf Q}_\ell)$
([sk-def-sfb-bounded-constructible]) and let $\mathcal L$ be a lisse
$\overline{\mathbf Q}_{\ell,X}$-module ([sk-lem-coefficient-heart]), that is, locally free of
finite rank for the pro-étale topology. Then the Verdier dual satisfies

$$
D_X\bigl(K\otimes^L\mathcal L\bigr)\;\cong\;
D_XK\otimes^L\mathcal L^\vee,
$$

the linear dual $\mathcal L^\vee$ of $\mathcal L$.
