+++
kind = "proof"
of = "sk-thm-properbasechange"
uses = ["sk-def-pbc", "sk-thm-p1", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison", "sk-def-pbc-conventions", "sk-thm-iff"]
+++
By Corollary [sk-cor-pe-classical-derived], we may write $K=\nu_X^*K_{\acute{e}t}$
with $K_{\acute{e}t}\in D^+(X_{\acute{e}t},\Lambda)$. The cohomology sheaves of $K_{\acute{e}t}$
are torsion, because $\nu_X^*$ is exact, commutes with colimits and is fully
faithful on sheaves, and therefore detects the condition $F=\varinjlim_nF[n]$
of Definition [sk-def-pbc]. It remains to show that the base change
map for $K_{\acute{e}t}$ is an isomorphism in $D^+(Y'_{\acute{e}t},\Lambda)$, and then to
pass to the pro-étale site.

We reduce to the rings $\Lambda/p\Lambda$, $p$ prime, which are killed by
$p$, so that $\mathrm{PBC}_{\Lambda/p\Lambda}(f)$ holds by
Propositions [sk-thm-p1] and [sk-thm-reduction]. A sheaf $F$ of
$\Lambda$-modules with $pF=0$ is a sheaf of $\Lambda/p\Lambda$-modules.
Restriction of scalars along $\Lambda\to\Lambda/p\Lambda$ is exact and
conservative, and it commutes with inverse images, derived direct images
and base change maps, since both derived direct images are computed on
underlying abelian sheaves (see the remark after
Convention [sk-def-pbc-conventions]). Hence the base change map for $F$ is an
isomorphism. If $nF=0$, we argue by induction on the number of prime
factors of $n$. For a prime $p\mid n$, the outer terms of
$0\to F[p]\to F\xrightarrow{p}pF\to0$ are killed by $p$ and by $n/p$, and
the five lemma applies to the long exact cohomology sequences. A torsion
sheaf is the filtered colimit $\varinjlim_nF[n]$, and
(4.6) applies to the qcqs morphisms $f$ and $f'$,
so the base change map is an isomorphism for every torsion sheaf of
$\Lambda$-modules. The truncation argument at the end of the proof of
Theorem [sk-thm-iff] passes to bounded below complexes with
torsion cohomology, in particular to $K_{\acute{e}t}$.

Finally we apply $\nu_{Y'}^*$. Since $f$ and $f'$ are proper, hence qcqs,
the comparison of direct images in
Theorem [sk-thm-pe-direct-image-comparison] applies. Using it together with the
comparison of inverse images $g_{\mathrm{pro}\acute{e}t}^*\nu_Y^*\simeq\nu_{Y'}^*g_{\acute{e}t}^*$, we
identify $\nu_{Y'}^*g^*Rf_*K_{\acute{e}t}$ and
$\nu_{Y'}^*Rf'_*g'^*K_{\acute{e}t}$ with $g^*Rf_*K$ and $Rf'_*g'^*K$ in
$D^+(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$. These comparisons respect the units and counits,
and hence the resulting isomorphism is the canonical pro-étale base change map.
