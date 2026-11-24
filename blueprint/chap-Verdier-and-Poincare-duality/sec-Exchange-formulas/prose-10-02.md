+++
id = "prose-10-02"
kind = "hidden"
title = "Exchange formulas (1)"
order = 824
+++
After defining the dualizing complex $\omega_X$,
the Verdier dual $\mathbb D_X$ and the double-dual map
$\delta_K:K\to\mathbb D_X\mathbb D_XK$, we prove the two exchange
formulas that need only adjunctions
(Lemma [lemma-internal-adjunction-two-exchange-formulas]). They say
that $\mathbb D$ turns [$Rf_!$](@proposition-construction-independence-rf-shriek) into $Rf_*$
and $f^*$ into [$f^!$](@theorem-existence-exceptional-inverse-image). For example, for $f=a_X$ and $K=\Lambda_X$ the first says that
$R\Gamma(X,\omega_X)$ is the dual of $R\Gamma_c(X,\Lambda)$, as for the
homology of a manifold. The other half, with the roles of $!$ and $*$
reversed, needs [biduality](@theorem-verdier-biduality).

The induction in the proof of Theorem [theorem-verdier-biduality]
ends on the geometric point, the case $\dim X=0$. There we want duality to be
the duality of finite projective modules, and for this [constructible
complexes](@definition-constructible-sheaves) must be perfect. Over $\mathbf Z/\ell^n$ this is a real
condition; for instance, the module $\mathbf Z/\ell$ has infinite projective
dimension over $\mathbf Z/\ell^2$. This is why we require the coefficients to
have finite Tor dimension. With this requirement,
Lemma [lemma-perfect-complexes-geometric-point] shows that [$D^b_{\mathrm{ctf}}$](@definition-constructible-sheaves) of the
point is exactly the category of perfect complexes.
