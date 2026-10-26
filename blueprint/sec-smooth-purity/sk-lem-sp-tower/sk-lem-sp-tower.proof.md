+++
kind = "proof"
of = "sk-lem-sp-tower"
uses = ["sk-prop-sp-integral-towers", "sk-prop-pe-replete", "sk-prop-integral-criterion"]
+++
The adjunction is $Lh^*p^{-1}\dashv Rp_*h_*$, for the change of rings $h$ from
towers to constant inverse systems of $\mathcal O_{E,T}$-modules and the morphism
$p$ of topoi to $T_{\mathrm{proét}}$ with $p_*=\varprojlim$ (Stacks, Tags 06YV and
07A6). By [sk-prop-sp-integral-towers] (1), $\operatorname{red}_T$ maps
$\Dbc(T,\mathcal O_E)$ into normalized constructible towers, and on
$\Dbc(T,\mathcal O_E)$ the unit is an isomorphism, since objects of
$\Dbc(T,\mathcal O_E)$ are derived complete ([sk-prop-integral-criterion]).

Conversely, let $C_\bullet$ be a normalized constructible tower and
$C=R\varprojlim_nC_n$. Then $C/\ell^m$ differs from $C_m$ by the derived limit of
the tower $(C_m[1])_n$ with transition maps multiplication by $\ell$. This limit
vanishes because $\ell^m$ kills $C_m$, so $C/\ell^m\simeq C_m$. Hence $C$ is
derived complete with $C/\ell\simeq C_1$ constructible, and it is bounded because
$T_{\mathrm{proét}}$ is replete ([sk-prop-pe-replete]; Stacks, Tag 0940); therefore
$C\in\Dbc(T,\mathcal O_E)$ by [sk-prop-sp-integral-towers] (2). The counit
$\operatorname{red}_TC\to C_\bullet$ is at level $m$ the reduction map
$C/\ell^m\to C_m$, an isomorphism by what we just showed, and since evaluations
detect isomorphisms the counit is an isomorphism.
