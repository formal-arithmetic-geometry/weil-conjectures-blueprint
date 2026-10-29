+++
id = "sk-prop-scalar-six"
kind = "proposition"
title = "The six operations and change of coefficients"
order = 2815
uses = ["sk-def-sfb-constructible", "sk-thm-sf-ctf-stability"]
tags = ["sketch"]
+++
A change of coefficients is derived extension of scalars along a map of condensed rings, pulled back to
$X$. For a map $\Lambda\to\Lambda'$ write

$$
K_{\Lambda'}=\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K.
$$

This functor $D(X_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda')$ is left adjoint to the exact restriction of
scalars $D(X_{\mathrm{proét}},\Lambda')\to D(X_{\mathrm{proét}},\Lambda)$. We consider the following maps of coefficient rings:

1. any homomorphism $A\to B$ of finite admissible rings;
2. the maps $\mathcal O_E\to\mathcal O_F$ and $E\to F$ for a finite extension $F/E$ inside $\Qlb$;
3. localization $\mathcal O_E\to E$, inclusions $E\to\Qlb$, and continuous maps $\mathcal O_E\to A$ to finite
   admissible rings, such as the reductions $\mathcal O_E\to\mathcal O_E/\pi_E^n$ (continuity is needed for the map
   to define a map of condensed rings);
4. composites of these maps.

For $E=\Ql$, the list contains $\Zl\to\mathcal O_F$, $\Ql\to F$, $\Zl\to\Ql$, $\Zl\to A$ and $\Ql\to\Qlb$, so
these maps connect all the admissible coefficient rings. Since the map $A\to B$ in (1) need not be flat,
extension of scalars is derived.

**Proposition.** For the maps of coefficient rings listed above, extension of scalars sends
$\Dctf(X,\Lambda)$ ([sk-def-sfb-constructible]) into $\Dctf(X,\Lambda')$. For $f\colon X\to Y$, the canonical
change-of-coefficients maps for $f^*$, $Rf_*$, $Rf_!$, $f^!$, tensor product and internal Hom
([sk-thm-sf-ctf-stability]), such as $(Rf_*K)_{\Lambda'}\to Rf_*(K_{\Lambda'})$ for $K\in\Dctf(X,\Lambda)$, are
isomorphisms. They respect composition and the units, counits and evaluation maps defining the comparisons.

Without finite Tor amplitude, the categories would not be preserved under change of coefficients. For
instance, if $X$ is a geometric point, the sheaf $\mathbf F_\ell$ belongs to $\Dbc(X,\mathbf Z/\ell^2)$ but not to
$\Dctf(X,\mathbf Z/\ell^2)$, and its extension of scalars $\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ is
unbounded. Thus $\Dbc$ is not preserved by arbitrary changes of finite coefficient rings.
