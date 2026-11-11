+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--3"
order = 839006
uses = ["definition-derived-base-change-map", "lemma-finite-cover-projective-space", "proposition-composition-open-restriction-compactifications-f", "theorem-picard-scheme-jacobian-over-separably", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--6", "definition-small-pro-etale-site--1", "definition-constructible-sheaves--5", "lemma-flat-models-generators--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "corollary-cohomology-geometric-fibres--2", "proposition-forgetting-supports-composition--3", "corollary-open-direct-image-over-field--1", "proposition-sp-unique-adjoint--1", "lemma-restriction-geometric-generic-fibre--1", "definition-categorical-trace--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-uniqueness-maps-dense-open--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--3", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
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
