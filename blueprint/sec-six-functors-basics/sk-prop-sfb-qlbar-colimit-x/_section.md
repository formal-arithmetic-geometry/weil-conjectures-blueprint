+++
id = "sk-prop-sfb-qlbar-colimit-x"
kind = "lemma"
title = "Comparison with completed coefficients"
order = 1547
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pullback-from-point"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObj", "AlgebraicGeometry.ProEtale.padicAlgClRingObj", "AlgebraicGeometry.ProEtale.padicAlgClRingObjCocone", "AlgebraicGeometry.ProEtale.isColimitPadicAlgClRingObjCocone"]
tags = ["sketch"]
+++
Let $\ell$ be a prime, let $X$ be a scheme, and let $E\subseteq\Qlb$ be a finite extension
of $\mathbf Q_\ell$ with ring of integers $\cO_E$ and uniformizer $\pi_E$. For a condensed
ring $\Lambda$ write $\Lambda_X=p_X^*\Lambda$ for its pullback to $X_{\mathrm{proét}}$
along $p_X\colon\Sh(X_{\mathrm{proét}})\to\Sh(*_{\mathrm{proét}})$
([sk-def-sfb-pullback-from-point], [sk-def-sfb-pulled-back-coefficients]). Write
$\cO_{E,X}$, $E_X$ and $\QbarX$ for the pullbacks to $X_{\mathrm{proét}}$ of the condensed
rings $\underline{\cO_E}$, $\underline E$ ([sk-def-sfb-condensed-ring]) and
$\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed]). There are canonical isomorphisms of
sheaves of rings

$$
\cO_{E,X}\cong\varprojlim_n(\cO_E/\pi_E^n)_X,
\qquad E_X\cong\cO_{E,X}[1/\ell],
\qquad \QbarX\cong\varinjlim_E E_X,
$$

where $(\cO_E/\pi_E^n)_X$ is the constant sheaf, $\cO_{E,X}[1/\ell]$ is the colimit of
$\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\xrightarrow{\ell}\cdots$, and the last colimit runs
over the filtered poset of finite subextensions $\mathbf Q_\ell\subseteq E\subseteq\Qlb$,
with transition maps induced by the inclusions $\underline E\to\underline F\to\underline{\Qlb}$.
They are compatible with inverse image along every morphism of schemes.

For $E=\mathbf Q_\ell$ this gives
$\mathbf Z_{\ell,X}\simeq\varprojlim_n(\mathbf Z/\ell^n)_X$ and
$\mathbf Q_{\ell,X}\simeq\mathbf Z_{\ell,X}[1/\ell]$.
