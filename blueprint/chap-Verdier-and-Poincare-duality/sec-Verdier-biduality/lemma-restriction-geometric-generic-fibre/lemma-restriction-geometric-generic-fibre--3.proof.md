+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--3"
order = 839006
+++
The direct-image and closed-support comparisons needed in this argument are clauses [lemma-restriction-geometric-generic-fibre--1] and [lemma-restriction-geometric-generic-fibre--2].

*Internal Hom.* The complexes $K$ for which the comparison is an
isomorphism are closed under cones and shifts, because both sides are exact
functors of $K$. The dévissage of
Lemma [lemma-verdier-duality-preserves-constructibility] therefore
reduces us to $K=t_!P$,
where $t$ is the inclusion of a stratum and $P$ is locally perfect
on it. For these generators, internal adjunction and the
dualizability of the locally perfect complex $P$ express internal Hom
through operations we have already compared:

$$
\cHom_X(t_!P,M)
\simeq Rt_*(P^\vee\otimes^{\mathbf L}t^!M).
$$

We check that $g^*$ commutes with each operation on the right. Factor $t$
as a closed immersion followed by an open immersion. For the open immersion
$t^!$ is restriction, which commutes with $g^*$, and for the closed immersion
we use the second comparison. Pullback commutes with $Rt_*$ by the first
comparison, and it commutes with tensor products and with $P^\vee$. The
first two comparisons apply here, because by
Lemma [lemma-verdier-duality-preserves-constructibility]
all complexes used remain bounded constructible. Hence the comparison holds
for $K=t_!P$.

*Source:* the proof of Lemma [lemma-restriction-geometric-generic-fibre].
