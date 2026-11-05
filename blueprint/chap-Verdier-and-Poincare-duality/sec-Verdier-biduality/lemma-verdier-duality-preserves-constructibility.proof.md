+++
kind = "proof"
of = "lemma-verdier-duality-preserves-constructibility"
order = 837
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "lemma-flat-models-generators", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "proposition-six-operations-change-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
