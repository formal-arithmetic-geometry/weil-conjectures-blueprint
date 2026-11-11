+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--8"
order = 866017
uses = ["lemma-cohomology-modules-underlying-abelian", "proposition-pro-etale-coverings--1", "theorem-trace-isomorphism-top-degree--4"]
+++
Let $E\subset\overline{\mathbf Q}_\ell$ be finite over $\mathbf Q_\ell$. By clause [lemma-comparison-completed-coefficients--2],
$E_S=\mathcal O_{E,S}[1/\ell]$ is the colimit of
$\mathcal O_{E,S}\xrightarrow{\ell}\mathcal O_{E,S}\xrightarrow{\ell}\cdots$, and
by clause [lemma-comparison-completed-coefficients--3], $\overline{\mathbf Q}_{\ell,S}=\varinjlim_EE_S$ over
the finite subextensions $E$. Both are filtered colimits of sheaves in degree
zero, and $S$, being of finite type over a field, is quasi-compact and
quasi-separated. So Corollary [corollary-continuity-cohomology], in the
form of clause [corollary-continuity-cohomology--1], gives

$$
H^i(S,E_S)=\varinjlim H^i(S,\mathcal O_{E,S}),\qquad
H^i(S,\overline{\mathbf Q}_{\ell,S})=\varinjlim_EH^i(S,E_S).
$$

By clause [theorem-trace-isomorphism-top-degree--4], applied to $A=\mathcal O_E$ and
$U_n=\pi_E^n\mathcal O_E$, whose quotients have $\ell$-power order invertible
in $k'$, we have $H^i(S,\mathcal O_{E,S})=0$ for $i\notin[0,2d]$. Hence the
same holds for $E_S$ and for $\overline{\mathbf Q}_{\ell,S}$. The last assertion
is the case $S=X$, $k'=k$.

*Source:* the proof of Theorem [theorem-trace-isomorphism-top-degree].
