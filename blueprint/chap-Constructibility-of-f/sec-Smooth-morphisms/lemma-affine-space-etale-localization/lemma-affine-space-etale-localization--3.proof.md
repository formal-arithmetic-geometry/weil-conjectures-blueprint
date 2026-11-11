+++
kind = "proof"
of = "lemma-affine-space-etale-localization--3"
order = 558007
uses = ["definition-derived-base-change-map", "proposition-forgetting-supports-composition", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1", "definition-constructible-sheaves--5", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--1", "lemma-identity-pasting--2", "theorem-comparison-over-henselian-pair-degree--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--4", "proposition-adjunction-projective-line--3", "lemma-affine-space-etale-localization--1", "theorem-smooth-base-change-classical-torsion--1", "lemma-kunneth-one-identity-factor--1", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Both parts follow formally from uniqueness of right adjoints. Part (1)
comes from (6.9) and $j_!\dashv j^*$ for $\mathbf A^1\subset\mathbf P^1$, and
part (2) from $u_!\dashv u^*$ for étale $u$.

(1) Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the open
immersion, so that $Rp_{1!}=Rp_*j_!$ for $d=1$.
Since $j_!\dashv j^*$ and $Rp_*\dashv p^*(1)[2]$ by (6.9),
composing right adjoints gives $p_1^!=j^*p^*(1)[2]$. This equals
$p_1^*(1)[2]$ because $p\circ j=p_1$. For general $d$, write $p_d$ as a
composite of $d$ projections $r_1,\dots,r_d$ of affine lines. By
[Stacks, [0F7J](https://stacks.math.columbia.edu/tag/0F7J)] we have $Rp_{d!}\simeq Rr_{1!}\circ\dots\circ Rr_{d!}$.
Hence $p_d^!$ is the composite of the right adjoints of the $Rr_{i!}$,
which is $p_d^*(d)[2d]$ by the case $d=1$. Under this isomorphism, the
counit of $Rp_{d!}\dashv p_d^*(d)[2d]$ is the composite of the $d$ counits
for the affine lines. Each of these is a trace (6.5)
composed with the counit of $j_!\dashv j^*$. By associativity
[Stacks, [0F7K](https://stacks.math.columbia.edu/tag/0F7K)], the composite does not depend on how the $d$ factors are
grouped. Each factor and the composition isomorphism [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)] commute
with base change, and therefore so does the counit. The unit is determined
by the counit through the triangle identities, and it commutes with base
change as well.

*Source:* the proof of Lemma [lemma-affine-space-etale-localization].
