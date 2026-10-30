+++
id = "prose-10-18"
kind = "hidden"
title = "Smooth purity with $\\ell$-adic coefficients"
order = 459
+++
We now deduce Theorem [sk-thm-purity-transport] for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ from
Proposition [sk-thm-smooth-purity], following the plan of Section [sec-sp-grp-finite]. The derived limit over $n$
first requires the finite constructions to be compatible with change of coefficients.
Throughout, $f:X\to Y$ is smooth of pure relative dimension $d$.

The reader who knows $\ell$-adic cohomology as $\varprojlim_nH^i(X,\mathbf Z/\ell^n)$
may expect this step to be a formality, and on cohomology groups it nearly is. The
difficulty is that we want an isomorphism of functors $f^*(-)(d)[2d]\simeq f^!$ on
$\Dbc(-,\mathcal O_E)$, and $f^!_{\mathcal O_E}$ is defined by Brown representability,
not as a limit of the finite $f^!$. So we proceed in three stages. First we check that
the finite isomorphisms $\gamma_{f,A}$ commute with the reduction maps
$\mathcal O_E/\ell^{n+1}\to\mathcal O_E/\ell^n$, which is
(10.16). Then we redo the construction in the category of towers,
where these compatibilities become single morphisms, and take $R\varprojlim$ to obtain
an explicit right adjoint of $Rf_{!,\mathcal O_E}$
(Proposition [sk-prop-sp-integral-adjunction]). Finally, for fields we show that
$f^*(-)(d)[2d]$ is a right adjoint of $Rf_!$ by inverting $\ell$ in Hom groups
(Proposition [sk-prop-sp-rational] and Theorem [sk-thm-sp-qbar]). In every case the
comparison with $f^!$ is the uniqueness of adjoints
(Proposition [sk-prop-sp-unique-adjoint]).
