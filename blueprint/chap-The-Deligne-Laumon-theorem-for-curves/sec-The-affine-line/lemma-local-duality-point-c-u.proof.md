+++
kind = "proof"
of = "lemma-local-duality-point-c-u"
order = 1292
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The two stalks are cohomology sheaves of the complexes $i^*Rj_*F^\vee$
(in degree zero) and $i^*Rj_*F$ (in degree one) on the boundary. We
compute the Verdier dual of the second complex by duality on the curve,
and we find the first one, shifted and twisted.

Let $i:Z\hookrightarrow C$ be the inclusion of the whole finite
complement, and put $K_F=i^*Rj_*F$. For a lisse sheaf $G$ on $U$, the
adjunction $j^*\dashv Rj_*$ shows that $i^!Rj_*G=0$, and applying
$i^!$ to the localization triangle for $Rj_*G$ we obtain
$i^!j_!G\simeq i^*Rj_*G[-1]$. Since duality
exchanges $Rj_*$ with $j_!$ and $i^*$ with $i^!$, this formula lets us
write the result again in the form $i^*Rj_*$. Indeed, by Verdier duality on
the smooth curve, $\mathbb D_UF=F^\vee(1)[2]$ for the lisse sheaf $F$,
and we find

$$
\begin{split}
\mathbb D_Z K_F
&\simeq i^!\mathbb D_C Rj_*F
\simeq i^!j_!\mathbb D_UF\\
&\simeq i^*Rj_*(F^\vee(1)[2])[-1]
=K_{F^\vee}(1)[1].
\end{split}
$$

On the finite geometric scheme $Z$, Verdier duality is the exact
duality of coefficient vector spaces, so taking degree $-1$ at $\bar s$
we get $(R^1j_*F)_{\bar s}^\vee=(j_*F^\vee)_{\bar s}(1)$, which
is the pairing. It is Frobenius-equivariant because the adjunction,
localization and duality maps are natural in $F$ and respect its Weil
structure.
