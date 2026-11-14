+++
kind = "proof"
of = "lemma-sp-tower-adjunction-foundation--2"
order = 777004
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--8", "definition-w-local-w-strictly-local--4", "theorem-existence-contractible-covers--1", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-exact-products--1"]
+++
By Proposition [proposition-sp-integral-towers], reduction of a bounded constructible integral complex is a normalized constructible tower. Its unit is the completion isomorphism. It remains to verify the counit on an arbitrary normalized tower, as follows.

Conversely, let $C_\bullet$ be normalized and put $C=R\varprojlim C_n$. The
key point is that $C/\ell^m\simeq C_m$. The complex $C/\ell^m$ differs from
$C_m$ by the derived limit of the tower $(C_m[1])_n$ with transition maps
multiplication by $\ell$. This limit vanishes, because $\ell^m$ kills $C_m$
and so any $m$ consecutive transition maps compose to zero. Consequently
$C$ is derived complete and $C/\ell\simeq C_1$ is constructible. Moreover
$C$ is bounded. Indeed, the $C_n$ have cohomology in a fixed interval, and
on the replete topos $T_{\mathrm{pro}\acute{e}t}$ derived limits of such towers increase the
range by at most one [Stacks, [0940](https://stacks.math.columbia.edu/tag/0940)]. Therefore
$C\in\Dbc(T,\mathcal O_E)$ by Proposition [proposition-sp-integral-towers](2). The counit
$\operatorname{red}_TC\to C_\bullet$ is at level $m$ the reduction map
$C/\ell^m\to C_m$, which is an isomorphism by what we just showed. Since
evaluations detect isomorphisms, the counit is an isomorphism.

*Source:* the proof of Lemma [lemma-sp-tower-adjunction-foundation].
