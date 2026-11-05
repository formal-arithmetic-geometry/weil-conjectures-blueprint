+++
id = "lemma-integral-models--6"
kind = "lemma"
title = "Integral models over a finite coefficient field"
order = 294007
aliases = ["bp-r087-6"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.continuousConstructible_integral_model"]
uses = ["lemma-integral-models--3", "definition-constructible-sheaves"]
+++
Lean bypasses the description by generators in this clause by constructing
an integral model of the whole complex.

Let $E/\mathbf Q_\ell$ be a finite normed extension and let $X$ have
Noetherian underlying space. With the module-object constructibility
notation of [lemma-integral-models--3], every
$K\in D^b_{\mathrm{fp}}(X,E)$ admits
$K_0\in D^b_{\mathrm{fp}}(X,\mathcal O_E)$ and an isomorphism
$$
E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}K_0\simeq K.
$$
In the Noetherian setting of the lemma these are the corresponding
$\Dbc$ categories. No global lisse or locally free condition is imposed
on $K_0$.
