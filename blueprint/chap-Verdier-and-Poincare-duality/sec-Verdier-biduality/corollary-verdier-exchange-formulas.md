+++
id = "corollary-verdier-exchange-formulas"
kind = "corollary"
title = "Verdier exchange formulas"
order = 841
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_dualizingComplex", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_verdierDual", "AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_verdierDual"]
uses = ["lemma-internal-adjunction-two-exchange-formulas"]
+++
For a morphism $f:X\to Y$ there are natural isomorphisms of functors on
$D^b_{\mathrm{ctf}}(X,\Lambda)$, respectively $D^b_{\mathrm{ctf}}(Y,\Lambda)$,

$$
\begin{aligned}
\mathbb D_YRf_!&\simeq Rf_*\mathbb D_X,&
\mathbb D_YRf_*&\simeq Rf_!\mathbb D_X,\\
\mathbb D_Xf^*&\simeq f^!\mathbb D_Y,&
\mathbb D_Xf^!&\simeq f^*\mathbb D_Y.
\end{aligned}
$$

In particular, for an open $j:U\hookrightarrow X$ and a closed
$i:Z\hookrightarrow X$,

$$
\mathbb D_Xj_!\simeq Rj_*\mathbb D_U,\qquad
\mathbb D_XRj_*\simeq j_!\mathbb D_U,\qquad
i^*\mathbb D_X\simeq\mathbb D_Zi^!.
$$

The isomorphisms in the left column are (10.3)
and (10.4); those in the right column are
obtained from them by biduality, as displayed in the proof.
