+++
kind = "proof"
of = "lemma-smooth-morphisms-locally-constant-sheaves"
order = 566
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We write $Rf_*L$ as the dual of $Rf_!N$ for a suitable constructible
$N$. The point is that constructibility and base change are known for $Rf_!N$, and over a dense open of $S$ the cohomology sheaves of $Rf_!N$ are locally
constant, and there dualizing preserves both properties.

By Proposition [proposition-locally-constant-sheaves-finite-presentation], the locally
constant sheaf $L$ comes from a locally constant sheaf on the étale
site, and we work with the latter.

Since $X$ is the disjoint union of finitely many open pieces of pure
relative dimension, we may assume that $f$ has pure relative dimension
$d$. Let $\omega_f=f^!\mathbf F_{\ell,S}$ as in
Proposition [proposition-exceptional-inverse-image-smooth-morphism], and let

$$
N=\cHom_X(L,\mathbf F_{\ell,X})\otimes^{\mathbf L}\omega_f .
$$

By Proposition [proposition-exceptional-inverse-image-smooth-morphism], $\omega_f$ is locally
$\mathbf F_{\ell,X}(d)[2d]$. Hence $N$ is bounded constructible and
$\cHom_X(N,\omega_f)=L$.

*Duality.* Consider the pairing

$$
Rf_!N\otimes^{\mathbf L}Rf_*L
\longrightarrow Rf_!(N\otimes^{\mathbf L}L)
\longrightarrow Rf_!\omega_f
\xrightarrow{\varepsilon_{\mathbf F_{\ell,S}}}\mathbf F_{\ell,S},
\tag{6.15}
$$

where the first arrow is the projection formula followed by the counit
$f^*Rf_*L\to L$, and the second is evaluation. Its adjoint is a map

$$
\delta_L:Rf_*L
\longrightarrow \cHom_S(Rf_!N,\mathbf F_{\ell,S}),
\tag{6.16}
$$

and we claim that it is an isomorphism.
Since the map is an adjoint transpose, we test it on Hom groups out of a
family of generators, where adjunctions turn one side into the other.
To this end we write $L=\cHom_X(N,f^!\mathbf F_{\ell,S})$, and test
$\delta_L$ on the objects $P[n]$, where $P=u_!\Fell$
and $u:V\to S$ is quasi-compact, separated and étale. The objects $u_!\Fell$ are constructible of finite Tor amplitude, and their shifts detect
isomorphisms in $D(S_{\acute{e}t},\Fell)$. Since
$f^*P\otimes^{\mathbf L}N$ lies in $D^b_{\mathrm{ctf}}(X,\Fell)$, we may use tensor-Hom
adjunction, the adjunction $Rf_!\dashv f^!$ of
Theorem [theorem-existence-exceptional-inverse-image] between
$\Loc(D^b_{\mathrm{ctf}}(X,\Fell))$ and $\Loc(D^b_{\mathrm{ctf}}(S,\Fell))$, and the projection
formula. With Hom groups in $D(S_{\acute{e}t},\Fell)$, we then obtain

$$
\Hom(P,Rf_*\cHom(N,f^!\mathbf F_{\ell,S}))
=\Hom(Rf_!(f^*P\otimes^{\mathbf L}N),\mathbf F_{\ell,S})
=\Hom(P\otimes^{\mathbf L}Rf_!N,\mathbf F_{\ell,S}).
$$

By tensor-Hom adjunction, the last group is
$\Hom(P,\cHom_S(Rf_!N,\mathbf F_{\ell,S}))$. Unwinding the
adjunctions, one sees that the composite bijection is the map induced by
$\delta_L$, for every shift of $P$. Hence $\delta_L$
is an isomorphism.

*Shrinking the base.* Since $\delta_L$ is an isomorphism, it now suffices to
understand the dual of $Rf_!N$. By the finiteness theorem for $Rf_!$
[Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0), [0G2A](https://stacks.math.columbia.edu/tag/0G2A)], the complex $Rf_!N$ is bounded constructible. A
constructible sheaf on the integral scheme $S$ is locally constant on a
nonempty open subset. Thus each of the finitely many nonzero cohomology
sheaves of $Rf_!N$ is locally constant on a nonempty open of $S$. Let $S_0$
be the intersection of these opens; it is nonempty because $S$ is
irreducible.

Over the field $\Fell$, a finite locally constant sheaf is locally free of
finite rank. Its dual is exact, and evaluation identifies it with its
double dual. We now argue by induction on the number of nonzero cohomology
sheaves, using that the relevant canonical maps form morphisms of the
truncation triangles. In this way we see that a bounded complex with finite
locally constant cohomology is dualizable, that its dual is again of this
kind, and that forming the dual commutes with every pullback. Through
$\delta_L$, this proves the first assertion over $S_0$.

*Base change.* The duality $\delta_L$ exchanges $Rf_*L$ with
the dual of $Rf_!N$, and $Rf_!N$ satisfies base change. We show that the
duality is compatible with base change; then $Rf_*L$ satisfies base change
too. Let $v:T\to S_0$ be a
$k$-scheme of finite type over $S_0$, and let $f_T:X_T\to T$ and
$v_X:X_T\to X$ be the base changes. First, base change for $Rf_!$ and (6.1) identify $v_X^*N$, $v^*Rf_!N$ and $v_X^*\omega_f$ with the
corresponding objects for $f_T$. Next, the base change map $v^*Rf_*L\to Rf_{T,*}v_X^*L$ is characterized by the fact that it
carries the pullback of the counit $f^*Rf_*L\to L$ to the counit for
$f_T$. Hence the pullback of (6.15) is the pairing for
$f_T$, composed with this base change map. Finally, the complex $v^*Rf_!N$ is dualizable with dual $v^*\cHom(Rf_!N,\mathbf F_{\ell,S})$. Therefore the
base change map for $Rf_*L$ is identified with the dual of the base change
isomorphism for $Rf_!N$, and it is an isomorphism.
