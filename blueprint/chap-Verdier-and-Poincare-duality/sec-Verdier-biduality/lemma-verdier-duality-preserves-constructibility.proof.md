+++
kind = "proof"
of = "lemma-verdier-duality-preserves-constructibility"
order = 837
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "lemma-flat-models-generators", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "corollary-open-direct-image-over-field", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "proposition-sp-unique-adjoint", "lemma-internal-adjunction-two-exchange-formulas", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The lemma follows from the stability of $D^b_{\mathrm{ctf}}$ under the six operations.
Proposition [proposition-six-operations-dctf] shows that $a_X^!$ and
internal Hom preserve $D^b_{\mathrm{ctf}}$. As $\Lambda_s$ lies in $D^b_{\mathrm{ctf}}(s,\Lambda)$,
both $\omega_X=a_X^!\Lambda_s$ and $\mathbb D_XK$ lie in
$D^b_{\mathrm{ctf}}(X,\Lambda)$ for $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$. We also give a direct
argument with finite coefficients and smooth strata, because the proof of
Lemma [lemma-restriction-geometric-generic-fibre] uses its
dévissage to generators $t_!P$ again.

*Dévissage.* The complex $K$ is built by finitely many cones from
complexes $t_!P$, for locally closed $t:T\hookrightarrow X$ with $T$
smooth and $P$ a locally constant perfect complex. To see this, choose a
finite stratification by smooth strata, disregarding nilpotents, on which
the restrictions $P$ of $K$ are locally constant perfect complexes, and
use the localization triangles. The bounded flat models of
Lemma [lemma-flat-models-generators] and their stupid filtrations make
this precise. Since $\mathbb D_X$ is exact and $D^b_{\mathrm{ctf}}(X,\Lambda)$ is closed
under cones, it suffices to show that $\mathbb D_X(t_!P)$ lies in
$D^b_{\mathrm{ctf}}(X,\Lambda)$.

*The generators.* Internal adjunction (10.3)
for $t$ gives

$$
\mathbb D_X(t_!P)\simeq Rt_*\mathbb D_TP.
$$

On a smooth stratum of dimension $r$,
Theorem [theorem-smooth-purity-all-admissible-coefficients] identifies
the dual $\mathbb D_TP$ with $P^\vee(r)[2r]$, which is locally a perfect
complex. By Proposition [proposition-six-operations-dctf]
its ordinary direct image lies in $D^b_{\mathrm{ctf}}(X,\Lambda)$.
