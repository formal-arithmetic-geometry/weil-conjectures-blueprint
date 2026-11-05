+++
id = "lemma-integral-models--7"
kind = "lemma"
title = "Integral models over the algebraic closure"
order = 294008
aliases = ["bp-r087-7"]
lean = ["AlgebraicGeometry.ProEtale.exists_padicAlgCl_iso_integralModel"]
uses = ["lemma-integral-models--3", "definition-constructible-sheaves"]
+++
Lean bypasses the description by generators in this clause by descending
the whole complex to a finite coefficient field and choosing an integral
model there.

Let $X$ have Noetherian underlying space. Every
$K\in D^b_{\mathrm{fp}}(X,\overline{\mathbf Q}_\ell)$ admits a finite
subextension $E\subset\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$,
an object $K_0\in D^b_{\mathrm{fp}}(X,\mathcal O_E)$, and an isomorphism
$$
\QbarX\otimes^{\mathbf L}_{E_X}
\bigl(E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}K_0\bigr)\simeq K.
$$
Here $D^b_{\mathrm{fp}}$ is as in [lemma-integral-models--3]; for Noetherian
$X$ these are the corresponding $\Dbc$ categories.
