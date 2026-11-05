+++
kind = "proof"
of = "lemma-lattices-after-finite-stratification--1"
order = 289002
uses = ["lemma-lattices-lisse-e-sheaves", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "corollary-continuity-cohomology", "lemma-comparison-completed-coefficients"]
+++
Use the usual inverse images on integral and rational modules. They
preserve local finite freeness, commute with scalar extension, and are
compatible with composition, by [proposition-topos-functoriality] and
[lemma-inverse-image-coefficient-sheaves].

By [lemma-lattices-lisse-e-sheaves], integral lattices exist étale locally.
Refine these neighborhoods by affine opens. Their images form an open
cover of $X$, so topological Noetherianity gives a finite subcover. Its
disjoint union gives a surjective étale map $p:U\to X$, with $U$
quasi-compact and quasi-separated, and a locally free integral module
$M_0$ with $M_0[1/\ell]\simeq p^*L$.

Stratify $X$ into finitely many locally closed subschemes $S_s$ so that
$q_s:U\times_X S_s\to S_s$ is finite étale. It remains surjective by
base change. Pull back $M_0$ to $M_s$ on $U\times_X S_s$. Compatibility of
inverse image with scalar extension gives
$M_s[1/\ell]\simeq q_s^*j_s^*L$. Each $S_s$ is topologically Noetherian,
since its immersion identifies it with a subspace of $X$.

On one stratum write $q=q_s$ and $P=j_s^*L$. Form the inverse image

$$
L_{0,s}=\eta^{-1}\!\left(\operatorname{im}
  (q_*M_s\longrightarrow q_*q^*P)\right),
\qquad \eta:P\longrightarrow q_*q^*P,
$$

where all modules in this formula are viewed as integral modules. This
is the pullback of the image along the adjunction unit. When the finite
étale cover is split into sheets, it is the intersection of the
lattices on those sheets.

Pro-étale locally, this intersection is the kernel of a finite integral
matrix which becomes surjective after inverting $\ell$. One obtains the
matrix by clearing denominators in the local rational model. Successive
matrix pivots reduce the kernel to a finite free module; hence $L_{0,s}$
is locally free of finite rank.

Finally, scalar extension is localization at $\ell$
([lemma-comparison-completed-coefficients]), so it is exact. It commutes
with $q_*$ because the latter preserves the filtered colimit of
multiplication by $\ell$, by the degree-zero case of
[corollary-continuity-cohomology]. Thus the pushed lattice map becomes an
isomorphism after scalar extension, and the image and pullback
construction gives $L_{0,s}[1/\ell]\simeq P$. Doing this on every stratum
gives the asserted models, including on empty strata and in rank zero.
