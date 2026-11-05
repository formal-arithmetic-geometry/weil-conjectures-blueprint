+++
kind = "proof"
of = "theorem-verdier-biduality--4"
order = 844009
uses = ["theorem-verdier-biduality--2", "lemma-integral-models", "proposition-dctf-x-qbar-2-colimit", "proposition-six-operations-change-coefficients"]
+++
Choose a finite subextension $E\subset\overline{\mathbf Q}_\ell$ and an integral model $K_0$ with

$$
K\simeq T_XK_0,\qquad
T_X=(-)\otimes^{\mathbf L}_{\mathcal O_E}E
       \otimes^{\mathbf L}_E\overline{\mathbf Q}_\ell.
$$

This is `AlgebraicGeometry.ProEtale.exists_padicAlgCl_iso_integralModel`, combining descent to a finite coefficient field with the existence of an integral model; see [proposition-dctf-x-qbar-2-colimit] and [lemma-integral-models].

The comparisons for exceptional inverse image identify $T_X\omega_{X,\mathcal O_E}$ with $\omega_{X,\overline{\mathbf Q}_\ell}$. The comparisons for internal Hom, applied twice, and compatibility with the symmetry and evaluation identify invertibility of $T_X\delta_{K_0}$ with that of $\delta_{T_XK_0}$; see [proposition-six-operations-change-coefficients]. This is `AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierBiduality_integersToPadicAlgCl_obj`. Now apply [theorem-verdier-biduality--2] and transport along $T_XK_0\simeq K$. Lean packages this step as `AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierBiduality_of_integral`.
