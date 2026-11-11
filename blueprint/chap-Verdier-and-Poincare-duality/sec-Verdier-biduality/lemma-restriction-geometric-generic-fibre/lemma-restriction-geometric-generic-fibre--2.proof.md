+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--2"
order = 839004
uses = ["definition-derived-base-change-map", "definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "proposition-construction-independence-rf-shriek--7", "proposition-composition-base-change-rf-shriek--4", "proposition-forgetting-supports-composition--3", "lemma-restriction-geometric-generic-fibre--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Use the direct-image comparison of clause [lemma-restriction-geometric-generic-fibre--1].

*Exceptional inverse image.* Let $j$ be the open complement of
$i$ and pull back

$$
i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M
\longrightarrow.
$$

We compare the pulled-back triangle with the triangle with closed support
on the generic fibre, whose first term is $i_{\bar\eta,*}i_{\bar\eta}^!g_X^*M$.
The second terms agree. The third terms agree too, because the first
comparison identifies the pullback of $Rj_*j^*M$ with
$Rj_{\bar\eta,*}j_{\bar\eta}^*g_X^*M$, and the map between them is the same.
The first terms are then determined functorially. Indeed, there are no nonzero
maps, in any degree, from a complex supported on $Z_{\bar\eta}$ to one of the form
$Rj_{\bar\eta,*}N$, so the first term of each triangle is the fibre of the
second map. Pullback commutes with direct image along a closed immersion, so
the first term of the pulled-back triangle is $i_{\bar\eta,*}g_Z^*i^!M$. The
induced map $i_{\bar\eta,*}g_Z^*i^!M\to i_{\bar\eta,*}i_{\bar\eta}^!g_X^*M$
is adjoint to the pulled-back counit, that is, it is $i_{\bar\eta,*}$ of our
comparison map, and it is an isomorphism. Since $i_{\bar\eta,*}$ is fully
faithful, the comparison map itself is an isomorphism.

*Source:* the proof of Lemma [lemma-restriction-geometric-generic-fibre].
