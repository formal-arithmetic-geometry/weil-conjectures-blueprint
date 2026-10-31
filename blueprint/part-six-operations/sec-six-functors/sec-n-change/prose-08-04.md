+++
id = "prose-08-04"
kind = "hidden"
title = "Change of coefficients"
order = 380
+++
Later proofs often establish a statement for finite or integral
coefficients and then extend scalars to $E$ or $\overline{\mathbf Q}_\ell$. For instance, smooth
base change for $E$ and $\overline{\mathbf Q}_\ell$ is deduced in this way from the integral
case in Section [sec-smooth-base-change]. For this the six operations
must commute with extension of scalars.

For pullback, extension by zero and tensor product this is formal, since
extension of scalars is itself a tensor product. For the right adjoints
it is not. For a map $A\to B$ of finite rings, the statement
$R\Gamma(X,K)\otimes^{\mathbf L}_A B\simeq R\Gamma(X,K\otimes^{\mathbf L}_A B)$
is a projection formula that needs finite cohomological dimension, and for
$\mathcal O_E\to E$ or $E\to \overline{\mathbf Q}_\ell$ the comparison for $Rf_*$ says that
$Rf_*$ commutes with a colimit, which holds because the terms are uniformly
bounded below. For $f^!$ the comparison map is defined by adjunction, and
it is shown to be an isomorphism by computing $f^!$ once more, for a
closed immersion and for $\mathbf P^1$.
The main result is Proposition [sk-prop-scalar-six], and its main use is the
reduction principle of Proposition [sk-prop-reduction-to-finite].

A change of coefficients is derived extension of scalars along a map
of condensed rings, pulled back to $X$. For a map $\Lambda\to\Lambda'$ write

$$
K_{\Lambda'}=\Lambda'_X\otimes^{\mathbf L}_{\Lambda_X}K.
$$

This functor $D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda')$ is left
adjoint to the exact restriction of scalars
$D(X_{\mathrm{pro}\acute{e}t},\Lambda')\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
We consider the following maps of coefficient rings:

1. any homomorphism $A\to B$ of finite admissible rings;
2. the maps $\mathcal O_E\to\mathcal O_F$ and $E\to F$ for a
   finite extension $F/E$ inside $\overline{\mathbf Q}_\ell$;
3. localization $\mathcal O_E\to E$, inclusions $E\to \overline{\mathbf Q}_\ell$,
   and continuous maps $\mathcal O_E\to A$ to finite admissible rings,
   such as the reductions $\mathcal O_E\to\mathcal O_E/\pi_E^n$ (continuity
   is needed for the map to define a map of condensed rings);
4. composites of these maps.

For $E=\Ql$, the list contains $\Zl\to\mathcal O_F$, $\Ql\to F$, $\Zl\to\Ql$,
$\Zl\to A$ and $\Ql\to \overline{\mathbf Q}_\ell$, so these maps connect all the admissible
coefficient rings. Since the map
$A\to B$ in (1) need not be flat, extension of scalars is derived.
