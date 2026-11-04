+++
id = "theorem-smooth-purity-all-admissible-coefficients"
kind = "theorem"
title = "Smooth purity for all admissible coefficients"
order = 724
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothOrientation"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For every
admissible coefficient ring $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$,
with $A$ finite, there are isomorphisms, natural in $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$,

$$
\gamma_f(K):
f^{*}K(d)[2d]\xrightarrow{\sim}f^{!}K,
\tag{9.2}
$$

with the following properties.

1. If $f$ is the projection $p:\mathbf A^1_Y\to Y$, then
   $\varepsilon_p(\Lambda_Y)\circ Rp_!\bigl(\gamma_p(\Lambda_Y)\bigr)$ is the
   trace map (9.1).
2. For $g:Y'\to Y$ as in
   Definition [definition-exceptional-base-change-map], with exceptional
   base change map $\beta:g'^*f^!K\to f'^!g^*K$, we have
   $\beta\circ g'^*\gamma_f(K)=\gamma_{f'}(g^*K)$, the sources being
   identified by $g'^*f^*\simeq f'^*g^*$.
3. For a smooth morphism $h:Y\to Z$ of pure relative dimension $e$ and
   $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$, the map $\gamma_{h\circ f}(K)$ is the composite of
   $f^*(\gamma_h(K))(d)[2d]$ and $\gamma_f(h^!K)$, the sources being identified
   by $(h\circ f)^*\simeq f^*h^*$ and the targets by the composition
   isomorphism $f^!h^!\simeq(h\circ f)^!$ of
   Proposition [proposition-composition-open-restriction-compactifications-f](1).
4. For a coefficient map $\Lambda\to\Lambda'$ of
   Proposition [proposition-six-operations-change-coefficients], the
   change-of-coefficients isomorphism $(f^!K)_{\Lambda'}\to f^!(K_{\Lambda'})$
   of that proposition carries $(\gamma_{f,\Lambda}(K))_{\Lambda'}$ to
   $\gamma_{f,\Lambda'}(K_{\Lambda'})$, the sources being identified by the
   change-of-coefficients isomorphism for $f^*$.
