+++
kind = "proof"
of = "sk-lem-sp-tower"
uses = ["sk-prop-sp-integral-towers", "sk-prop-pe-replete", "sk-prop-integral-criterion"]
+++
The adjunction is $Lh^*p^{-1}\dashv Rp_*h_*$, for the change of rings $h$ from towers to
constant inverse systems of $\mathcal O_{E,T}$-modules and the morphism $p$ to $T_{\mathrm{pro}\acute{e}t}$
with $p_*=\varprojlim$ [Stacks, Tag 06YV](https://stacks.math.columbia.edu/tag/06YV), [Stacks, Tag 07A6](https://stacks.math.columbia.edu/tag/07A6). By
Proposition [sk-prop-sp-integral-towers](1), $\operatorname{red}_T$ maps
$\Dbc(T,\mathcal O_E)$ into normalized constructible towers, and on $\Dbc$ the unit is an
isomorphism since objects of $\Dbc$ are derived complete. Conversely, if $C_\bullet$ is
normalized and
$C=R\varprojlim C_n$, then $C/\ell^m$ differs from $C_m$ by the derived limit of the tower
$(C_m[1])_n$ with transition maps multiplication by $\ell$. This limit vanishes because
$\ell^m$ kills $C_m$, so $C/\ell^m\simeq C_m$. Hence $C$ is derived complete with $C/\ell$
constructible, and it is bounded because $T_{\mathrm{pro}\acute{e}t}$ is replete [Stacks, Tag 0940](https://stacks.math.columbia.edu/tag/0940); therefore
$C\in\Dbc(T,\mathcal O_E)$ by Proposition [sk-prop-sp-integral-towers](2). The counit
$\operatorname{red}_TC\to C_\bullet$ is at level $m$ the reduction map $C/\ell^m\to C_m$,
an isomorphism by what we just showed, and since evaluations detect isomorphisms the
counit is an isomorphism.
