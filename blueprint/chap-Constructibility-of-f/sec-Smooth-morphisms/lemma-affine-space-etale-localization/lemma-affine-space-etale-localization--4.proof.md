+++
kind = "proof"
of = "lemma-affine-space-etale-localization--4"
order = 558009
uses = ["definition-derived-base-change-map", "definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-composition-base-change-rf-shriek--1", "proposition-forgetting-supports-composition--1", "proposition-sp-unique-adjoint--1", "lemma-schematic-closure-uniqueness--1", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
(2) For an étale $u$, the functor $Ru_!$ is extension by zero. By its
elementary construction [Stacks, [03S2](https://stacks.math.columbia.edu/tag/03S2)], it is an exact functor
$u_!:\operatorname{Mod}(U_{\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\acute{e}t},\Lambda)$ left adjoint to $u^*$.
As both functors are exact, they need not be derived, and the adjunction
extends to derived categories. For every $M\in D(U_{\acute{e}t},\Lambda)$,

$$
\Hom(M,u^*f^!N)
=\Hom(u_!M,f^!N)
=\Hom(Rf_!u_!M,N)
=\Hom(R(fu)_!M,N),
$$

where the last step is the composition isomorphism of [Stacks, [0F7J](https://stacks.math.columbia.edu/tag/0F7J)]. The
Yoneda lemma gives (6.12). Taking $M=u^*f^!N$ and the
identity on the left, we see that the counit of $R(fu)_!\dashv(fu)^!$ is
the composite of the counits as stated. The isomorphism for $uu'$ and the
composite of those for $u$ and $u'$ both correspond under the Yoneda lemma
to bijections obtained from the composition isomorphism for
$f\circ u\circ u'$. These bijections agree by associativity of the
composition isomorphisms [Stacks, [0F7K](https://stacks.math.columbia.edu/tag/0F7K)].

*Source:* the proof of Lemma [lemma-affine-space-etale-localization].
