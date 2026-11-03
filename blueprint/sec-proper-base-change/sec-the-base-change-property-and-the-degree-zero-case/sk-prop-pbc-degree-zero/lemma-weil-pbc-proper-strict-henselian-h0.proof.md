+++
kind  = "proof"
of    = "lemma-weil-pbc-proper-strict-henselian-h0"
+++
Put $S_0=\Spec k$, $Z_0=Z\times_SS_0$ with closed immersion $i_0:Z_0\to Z$, and
let $v:Z_s\to Z_0$ be the base change of $\Spec k^{\mathrm{alg}}\to\Spec k$, so
that $a=i_0\circ v$.

*Step 1: the closed fibre.* By [def-weil-pbc-henselian-terminology] a strictly
henselian local ring is henselian local, so $(A,\mathfrak m)$ is a henselian pair.
Since $p$ is proper, [lemma-weil-pbc-etale-degree-zero] shows that
$i_0^\sharp:\Gamma(Z,F)\to\Gamma(Z_0,i_0^{-1}F)$ is an isomorphism.

*Step 2: the geometric fibre.* The residue field $k$ is separably closed, so
every element of $k^{\mathrm{alg}}$ is purely inseparable over $k$ and
$\Spec k^{\mathrm{alg}}\to\Spec k$ is a universal homeomorphism (surjective,
integral and radicial). Its base change $v$ is again a universal homeomorphism
[lem-weil-pbc-universal-homeomorphism-base-change], so inverse image along $v$ is
an equivalence of categories of etale sheaves
[thm-weil-pbc-universal-homeomorphism-invariance]; hence the unit of
$v^{-1}\dashv v_*$ is an isomorphism and so is
$v^\sharp:\Gamma(Z_0,i_0^{-1}F)\to\Gamma(Z_s,v^{-1}i_0^{-1}F)$.

*Step 3: assembly.* By the composition law
[lemma-weil-pbc-finite-pullback-composition], $a^\sharp$ followed by the
composition isomorphism $a^{-1}F\cong v^{-1}i_0^{-1}F$ is $v^\sharp\circ i_0^\sharp$,
an isomorphism by Steps 1 and 2.
