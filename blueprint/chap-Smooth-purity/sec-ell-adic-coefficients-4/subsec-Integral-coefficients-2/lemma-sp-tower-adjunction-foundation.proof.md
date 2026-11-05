+++
kind = "proof"
of = "lemma-sp-tower-adjunction-foundation"
order = 777
+++
The adjunction is a composite of two standard adjunctions of ringed topoi.
For the equivalence we check that the unit is an isomorphism on $\Dbc$ and
that the counit is an isomorphism on normalized constructible towers. The
second is the substantial point, since there we must show that the limit of such
a tower is again constructible.

The adjunction is $Lh^*p^{-1}\dashv Rp_*h_*$, for the change of rings $h$ from towers to
constant inverse systems of $\mathcal O_{E,T}$-modules and the morphism $p$ to $T_{\mathrm{pro}\acute{e}t}$
with $p_*=\varprojlim$ [Stacks, [06YV](https://stacks.math.columbia.edu/tag/06YV), [07A6](https://stacks.math.columbia.edu/tag/07A6)]. By
Proposition [proposition-sp-integral-towers](1), $\operatorname{red}_T$ maps
$\Dbc(T,\mathcal O_E)$ into normalized constructible towers. On $\Dbc$ the
unit is an isomorphism, since objects of $\Dbc$ are derived complete.

Conversely, let $C_\bullet$ be normalized and put $C=R\varprojlim C_n$. The
key point is that $C/\ell^m\simeq C_m$. Indeed, the complex $C/\ell^m$ differs from
$C_m$ by the derived limit of the tower $(C_m[1])_n$ with transition maps
multiplication by $\ell$, and this limit vanishes, because $\ell^m$ kills $C_m$
and so any $m$ consecutive transition maps compose to zero. Consequently
$C$ is derived complete and $C/\ell\simeq C_1$ is constructible. Moreover
$C$ is bounded, because the $C_n$ have cohomology in a fixed interval, and
on the replete topos $T_{\mathrm{pro}\acute{e}t}$ derived limits of such towers increase the
range by at most one [Stacks, [0940](https://stacks.math.columbia.edu/tag/0940)]. Therefore
$C\in\Dbc(T,\mathcal O_E)$ by Proposition [proposition-sp-integral-towers](2). Finally, the counit
$\operatorname{red}_TC\to C_\bullet$ is at level $m$ the reduction map
$C/\ell^m\to C_m$, which is an isomorphism by what we just showed. Since
evaluations detect isomorphisms, the counit is an isomorphism.
