+++
kind = "proof"
of = "lemma-verdier-duality-preserves-constructibility"
order = 837
uses = ["definition-small-pro-etale-site", "lemma-flat-models-generators", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "lemma-internal-adjunction-two-exchange-formulas", "definition-categorical-trace", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
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
