+++
kind = "proof"
of = "sk-lem-pd-preservation"
uses = ["sk-lem-sf-flat-model", "sk-thm-sf-ctf-stability", "sk-thm-purity-transport"]
+++
By Proposition [sk-thm-sf-ctf-stability], $a_X^!$ and internal Hom preserve
$D^b_{\mathrm{ctf}}$. Since $\Lambda_s$ lies in $D^b_{\mathrm{ctf}}(s,\Lambda)$, it follows that
$\omega_X=a_X^!\Lambda_s$ and $\mathbb D_XK$ lie in
$D^b_{\mathrm{ctf}}(X,\Lambda)$ for $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$.

With finite coefficients there is also a
direct argument using smooth strata, and its dévissage to generators
$t_!P$ is used again in the proof of
Lemma [sk-lem-pd-generic-restriction]. Choose a finite stratification by
smooth strata, disregarding nilpotents, on which the restrictions
$P$ of $K$ are locally constant perfect complexes. Using the
localization triangles, we build $K$ by finitely many cones from
complexes $t_!P$, for locally closed $t:T\hookrightarrow X$. To make
this precise we use the bounded flat models of
Lemma [sk-lem-sf-flat-model] and their stupid filtrations. By internal
adjunction we have

$$
\mathbb D_X(t_!P)\simeq Rt_*\mathbb D_TP.
$$

On a smooth stratum of dimension $r$, Theorem [sk-thm-purity-transport] identifies the dual
$\mathbb D_TP$ with $P^\vee(r)[2r]$, which is locally a perfect complex. Its
ordinary direct image lies in $D^b_{\mathrm{ctf}}(X,\Lambda)$ by
Proposition [sk-thm-sf-ctf-stability]. Since $\mathbb D_X$ is exact and
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is closed under cones, and $K$ is built by
finitely many cones, the lemma follows.
