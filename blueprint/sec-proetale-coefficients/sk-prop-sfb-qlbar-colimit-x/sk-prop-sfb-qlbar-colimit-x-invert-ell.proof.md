+++
kind  = "proof"
of    = "det-prop-sfb-qlbar-colimit-x-invert-ell"
+++
*On the point.* Let $S$ be a profinite set and $h\in C(S,E)$. Since $S$ is compact, $h(S)$ is
compact, hence bounded in $E$, so $h(S)\subseteq\ell^{-m}\cO_E$ for some $m$, and then
$\ell^mh\in C(S,\cO_E)$. Thus
$$
C(S,E)=\bigcup_m\ell^{-m}C(S,\cO_E)=\varinjlim\bigl(C(S,\cO_E)\xrightarrow{\ell}C(S,\cO_E)\xrightarrow{\ell}\cdots\bigr),
$$
the colimit of abelian groups being injective since $C(S,\cO_E)$ is $\ell$-torsion free.
These identifications are compatible with restriction along maps of profinite sets.

*The colimit is a sheaf.* Profinite sets are quasi-compact in $*_{\mathrm{proét}}$, so the
sheaf condition for a covering involves only a finite covering family, i.e. it is a
finite limit; filtered colimits of abelian groups commute with finite limits. Hence the
sectionwise colimit of the sheaves $\underline{\cO_E}$ is already a sheaf, and the previous
paragraph shows that $\underline E=\varinjlim(\underline{\cO_E}\xrightarrow{\ell}\underline{\cO_E}\to\cdots)$
in $\Sh(*_{\mathrm{proét}},\Ab)$, the structure maps being $\ell^{-m}$ times the inclusion
[def-sfb-integers-to-subfield-point].

*Pullback.* The functor $p_X^*$ is a left adjoint ([sk-def-sfb-pullback-from-point]),
so it preserves colimits, and it is additive, so it sends multiplication by $\ell$ to
multiplication by $\ell$. Applying it gives
$E_X=\varinjlim(\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\to\cdots)=\cO_{E,X}[1/\ell]$, the
structure map from the first term being $p_X^*$ of the inclusion, i.e. $\varphi$.

*Ring structure.* $\varphi$ is a map of ring objects [def-sfb-integers-to-subfield], and
$\ell$ is invertible in $E_X$ because it is invertible in $\underline E$. By the universal
property of the localization, $\varphi$ extends uniquely to a ring map
$\cO_{E,X}[1/\ell]\to E_X$; on the $m$-th term of the colimit it is $\ell^{-m}\varphi$, so it
is the isomorphism just obtained.

*Flatness.* $E_X$ is a filtered colimit of free $\cO_{E,X}$-modules of rank one; tensor
products commute with colimits and filtered colimits of modules are exact, so
$E_X\otimes_{\cO_{E,X}}-$ is exact.
