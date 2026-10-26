+++
id = "sk-prop-scalar-six"
kind = "proposition"
title = "The six operations and coefficient comparison"
order = 2469
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-derived-lower-shriek", "sk-prop-ctf-finite-comparison", "sk-cor-pe-bounded-continuity", "sk-thm-existence"]
tags = ["sketch"]
+++
A change of coefficients is derived extension of scalars along a map of condensed rings, pulled back to
$X$. For a map $\Lambda\to\Lambda'$ write

$$
K_{\Lambda'}=\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K.
$$

This functor $\D(X_{\mathrm{proét}},\Lambda)\to\D(X_{\mathrm{proét}},\Lambda')$ is left adjoint to the exact restriction of
scalars $\D(X_{\mathrm{proét}},\Lambda')\to\D(X_{\mathrm{proét}},\Lambda)$. The coefficient maps used are:

1. any homomorphism $A\to B$ of finite admissible rings;
2. the maps $\mathcal O_E\to\mathcal O_F$ and $E\to F$ for a finite extension $F/E$ inside $\Qlb$;
3. localization $\mathcal O_E\to E$, inclusions $E\to\Qlb$, and maps $\mathcal O_E\to A$ to finite admissible rings;
4. composites of these maps.

Taking $E=\mathbf Q_\ell$ gives $\mathbf Z_\ell\to\mathcal O_F$, $\mathbf Q_\ell\to F$, $\mathbf Z_\ell\to\mathbf Q_\ell$, $\mathbf Z_\ell\to A$ and
$\mathbf Q_\ell\to\Qlb$, so these maps connect all the admissible coefficient rings. A map from $\mathcal O_E$ to a
finite ring is continuous, and its target is killed by a power of $\pi_E$. The map $A\to B$ in (1) need not
be flat.

**Proposition.** For the listed coefficient maps, extension of scalars sends $\Dctf(X,\Lambda)$ into
$\Dctf(X,\Lambda')$. For $f\colon X\to Y$, the canonical coefficient comparison maps for $f^*$, $Rf_*$, $Rf_!$,
$f^!$, tensor product and internal Hom, such as $(Rf_*K)_{\Lambda'}\to Rf_*(K_{\Lambda'})$ in
$\Dctf(Y,\Lambda')$ for $K\in\Dctf(X,\Lambda)$, are isomorphisms of functors from $\Dctf(-,\Lambda)$ to
$\Dctf(-,\Lambda')$. They respect composition and the units, counits and evaluation maps defining the
comparisons.

Finite Tor amplitude is what makes the statement uniform in the coefficients: on a geometric point $X$, the
sheaf $\mathbf F_\ell$ belongs to $\Dbc(X,\mathbf Z/\ell^2)$ but not to $\Dctf(X,\mathbf Z/\ell^2)$, and its extension of scalars
$\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ is unbounded.
