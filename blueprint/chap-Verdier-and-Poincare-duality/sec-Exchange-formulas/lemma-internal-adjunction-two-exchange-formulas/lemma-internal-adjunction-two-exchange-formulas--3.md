+++
id = "lemma-internal-adjunction-two-exchange-formulas--3"
kind = "lemma"
title = "Exchange with inverse image along the Lean route"
name_showing = false
order = 829003
aliases = ["bp-r248-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.verdierDualUpperStarIso", "AlgebraicGeometry.WeilComplex.nonempty_upperShriek_verdierDual_iso"]
uses = ["definition-constructible-sheaves", "definition-verdier-dual-evaluation", "definition-weil-structure", "theorem-exceptional-inverse-image"]
+++
The general adjunction-only form of (10.4) is bypassed by the Lean route;
the following two forms occur in the proof.

Let $k$ have positive characteristic $p\ne\ell$, with $p$ and $\ell$
prime, and let $j:U\hookrightarrow Y$ be an open immersion of separated
schemes of finite type over $k$. For
$L\in\Dbc(Y,\overline{\mathbf Q}_\ell)$ on the pro-étale site there is
an isomorphism

$$
j^*\mathbb D_YL\simeq\mathbb D_Uj^*L.
$$

Using $j^!\simeq j^*$, this is the open-immersion case of (10.4).

For the other form, let $k_0$ be a finite field, let $\ell$ be a prime
different from its characteristic, and let $f:X\to Y$ be a separated
morphism of finite type between separated schemes of finite type over
$k_0$. Suppose $Rf_!$, $Ra_{X!}$ and $Ra_{Y!}$ have right adjoints on
Weil complexes. For every Weil complex $L$ on $Y$ with coefficients in
$\overline{\mathbf Q}_\ell$ there is an isomorphism

$$
f^!\mathbb D_YL\simeq\mathbb D_Xf^*L.
$$

The Weil-complex version uses biduality and is therefore a later
consequence, rather than an input to the proof of biduality.
