+++
kind  = "proof"
of    = "lem-sc-genus-invariant"
+++
By [def-sc-genus] and Serre duality (applied on each of the finitely many
connected components), $g(C)=\dim_kH^0(C,\Omega^1_{C/k})=\dim_kH^1(C,\mathcal O_C)$,
and likewise over $k'$, since $C_{k'}$ is again proper and smooth of relative
dimension one. By
[lem-pc-flat-base-change-cohom] applied to
$\mathcal F=\mathcal O_C$ and the flat extension $k\to k'$,

$$
\dim_{k'}H^1(C_{k'},\mathcal O_{C_{k'}})=\dim_kH^1(C,\mathcal O_C),
$$

i.e. $g(C_{k'})=g(C)$.
