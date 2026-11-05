+++
id = "prose-09-21"
kind = "hidden"
title = "Integral coefficients (1)"
order = 772
+++
Fix a finite extension $E/\mathbf Q_\ell$. An object $M$ of $\Dbc(T,\mathcal O_E)$ is derived
complete, $M\simeq R\varprojlim_nM/\ell^n$, and the finite theory applies to each
$M/\ell^n$. The units, counits and transition maps at the finite levels, however, live in
the different categories $D(T_{\mathrm{pro}\acute{e}t},\mathcal O_E/\ell^n)$, and a family of them that
commutes with the transition maps only up to unspecified isomorphisms
does not define a morphism between the derived limits. We therefore work in the derived category $D(\operatorname{Tow}(T))$ of towers
$(C_n)_n$, where $C_n$ is a sheaf of $\mathcal O_{E,T}/\ell^n$-modules on $T_{\mathrm{pro}\acute{e}t}$ and
the transition maps are linear over $\mathcal O_{E,T}/\ell^{n+1}\to\mathcal O_{E,T}/\ell^n$.
These are the modules over $(\mathcal O_{E,T}/\ell^n)_n$ in the topos of inverse systems
[Stacks, [0940](https://stacks.math.columbia.edu/tag/0940)]. In this category a compatible family of maps is one morphism. Evaluation
$C_\bullet\mapsto C_n$ is exact, and the evaluations jointly detect isomorphisms, but they do
not detect equality of morphisms. This is why the maps below are always compared in
$D(\operatorname{Tow}(T))$. A tower is *constructible* if each $C_n$ lies in
$D^b_{\mathrm{ctf}}(T_{\mathrm{pro}\acute{e}t},\mathcal O_E/\ell^n)$ with bounds independent of $n$, and
*normalized* if its reduction maps $C_n\otimes^{\mathbf L}\mathcal O_{E,T}/\ell^m\to C_m$
are isomorphisms for all $m\le n$.

We need two facts about integral complexes. Part (1) of the next
proposition gives the uniform bounds in the definition of a constructible
tower, and part (2) shows that the derived limit of such a tower is again
an object of $\Dbc$.
