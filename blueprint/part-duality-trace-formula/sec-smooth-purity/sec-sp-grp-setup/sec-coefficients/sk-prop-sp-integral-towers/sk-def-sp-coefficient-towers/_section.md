+++
id = "sk-def-sp-coefficient-towers"
kind = "definition"
title = "Coefficient towers"
lean = ["AlgebraicGeometry.ProEtale.spCoefficientTowers"]
order = 2944
uses = ["sk-prop-sfb-qlbar-colimit-x"]
+++
Fix a finite extension $E/\Ql$ and a scheme $T$. The ideals $(\ell^n)$ and
$(\pi_E^n)$ of $\mathcal O_E$ are cofinal, so we use powers of $\ell$; by
[sk-prop-sfb-qlbar-colimit-x], $\mathcal O_{E,T}=\varprojlim_n(\mathcal O_E/\ell^n)_T$,
and we write $\mathcal O_{E,T}/\ell^n$ for $(\mathcal O_E/\ell^n)_T$.

The category $\operatorname{Tow}(T,\mathcal O_E)$ has as objects the systems
$C_\bullet=(C_n,t_n)_{n\geq1}$, where $C_n$ is a sheaf of
$\mathcal O_{E,T}/\ell^n$-modules on $T_{\mathrm{proét}}$ and
$t_n:C_{n+1}\to C_n$ is linear over
$\mathcal O_{E,T}/\ell^{n+1}\to\mathcal O_{E,T}/\ell^n$. Morphisms are families
of module maps commuting with the $t_n$. We write
$\mathcal O_{E,T}/\ell^\bullet=(\mathcal O_{E,T}/\ell^n)_n$ for the tower of
coefficient rings.
