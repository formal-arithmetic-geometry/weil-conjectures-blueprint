+++
kind  = "proof"
of    = "lem-weil-pbc-etale-restriction-injectives"
+++
A morphism from the presheaf in [def-weil-pbc-etale-sum-extension] to a sheaf
$N$ is a compatible family of maps $M(V,s)\to N(V)$. Such a family is exactly
a morphism $M\to v^*N$: on the slice etale site, the inverse image of
[def-weil-pbc-inverse-image] is restriction. Sheafification has the same maps
to $N$, so this proves adjunction.

At a geometric point $\bar x$, the defining direct sums give

$$
 (v_!M)_{\bar x}=\bigoplus_{\bar w\in W_{\bar x}} M_{\bar w}.
$$

Indeed, a point of the etale fibre is a lift on an etale neighbourhood of
$\bar x$. Finitely many lifts and germs can be represented on a common
neighbourhood by taking fibre products. Equality of finitely many germs holds
on a further neighbourhood. Thus taking the colimit over neighbourhoods gives
exactly the displayed direct sum, whose elements have finite support.
Geometric stalks are exact by
[prop-weil-pbc-geometric-stalks-exact]; direct sums of modules are exact.
Conservativity in [lemma-weil-pbc-geometric-stalk-conservative] proves
exactness of $v_!$. Finally
$\operatorname{Hom}(-,v^*I)=\operatorname{Hom}(v_!(-),I)$ is exact when $I$
is injective, proving the last assertion.
