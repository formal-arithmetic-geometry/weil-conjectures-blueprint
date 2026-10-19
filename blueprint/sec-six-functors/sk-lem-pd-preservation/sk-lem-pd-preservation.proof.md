+++
kind = "proof"
of = "sk-lem-pd-preservation"
uses = ["sk-lem-sf-flat-model", "sk-thm-sf-ctf-stability"]
+++
Composition of the exceptional functors puts
$\omega_X=a_X^!\Lambda_s$ in $\Dctf(X,\Lambda)$.
Internal-Hom preservation in Proposition [sk-thm-sf-ctf-stability] therefore
already proves the assertion. With finite coefficients there is also a
direct argument from smooth strata; its dévissage to generators
$t_!P$ is used again in the proof of
Lemma [sk-lem-pd-generic-restriction]. Choose a finite smooth
stratification, disregarding nilpotents, on which the restrictions
$P$ of $K$ are locally constant perfect complexes. The
localization triangles build $K$ by finitely many cones from
$t_!P$, for locally closed $t:T\hookrightarrow X$. For finite
coefficients one uses the bounded flat models of
Lemma [sk-lem-sf-flat-model] and their stupid filtrations. Internal
adjunction gives

$$
 \mathbb D_X(t_!P)\simeq Rt_*\mathbb D_TP.
$$

On a smooth stratum of dimension $r$, purity identifies the latter
dual with $P^\vee(r)[2r]$, a locally perfect complex. Its
ordinary direct image lies in $\Dctf(X,\Lambda)$ by
Proposition [sk-thm-sf-ctf-stability], and finite cones prove preservation.
