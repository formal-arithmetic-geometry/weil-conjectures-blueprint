+++
kind = "proof"
of = "sk-thm-properbasechange"
uses = ["sk-def-pbc", "sk-thm-p1", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison", "sk-def-pbc-conventions", "sk-thm-iff"]
+++
By [sk-cor-pe-classical-derived], write $K=\nu_X^*K_{\mathrm{ét}}$ with
$K_{\mathrm{ét}}\in D^+(X_{\Et},\Lambda)$. The cohomology sheaves of
$K_{\mathrm{ét}}$ are torsion, because $\nu_X^*$ is exact, commutes with
colimits and is fully faithful on sheaves, and therefore detects the condition
$F=\varinjlim_nF[n]$ of [sk-def-pbc]. It remains to show that the exchange map
for $K_{\mathrm{ét}}$ is an isomorphism in $D^+(Y'_{\Et},\Lambda)$, and then to
pass to the pro-étale site.

*Filtered colimits.* The passage from sheaves killed by an integer to all
torsion sheaves uses continuity of étale cohomology. If $u:T\to S$ is
quasi-compact and quasi-separated, then

$$
\varinjlim_iR^qu_*F_i\xrightarrow{\ \sim\ }R^qu_*\bigl(\varinjlim_iF_i\bigr)
\qquad(q\geq0)
$$

for every filtered system of abelian étale sheaves, and the same holds after
any base change of $u$ (Stacks Project, Tag 09Z1). It suffices to check this
on affine étale $V\to S$. There $R^qu_*F$ is the sheafification of
$V\mapsto H^q(T\times_SV,F|)$, and the schemes $T\times_SV$ are quasi-compact
and quasi-separated, so their cohomology commutes with filtered colimits by
the usual argument with finite covers and finite hypercovers: in degree $q$,
a class and a witness that it dies involve only a finite $(q+1)$-skeleton, so
the cocycle and the finitely many equalities come from a single index.

*$\Lambda$-modules.* For a prime $p$, the ring $\Lambda/p\Lambda$ is torsion,
so $\mathrm{PBC}_{\Lambda/p\Lambda}(f)$ holds by [sk-thm-p1] and
[sk-thm-reduction]. For $f$ quasi-compact and quasi-separated,
$\mathrm{PBC}_\Lambda(f)$ follows from $\mathrm{PBC}_{\Lambda/p\Lambda}(f)$ for
all primes $p$. Restriction of scalars along $\Lambda\to\Lambda/p\Lambda$ is
exact and conservative, and compatible with inverse images, derived direct
images and the exchange maps, because both cohomologies agree with that of
the underlying abelian sheaves ([sk-def-pbc-conventions]). Hence the exchange
map is an isomorphism for every sheaf of $\Lambda$-modules killed by a prime
$p$, which is a sheaf of $\Lambda/p\Lambda$-modules. If $nF=0$, we argue by
induction on the number of prime factors of $n$: for a prime $p\mid n$, the
sequence $0\to F[p]\to F\xrightarrow{p}pF\to0$ has outer terms killed by $p$
and by $n/p$, and the five lemma applies to the long exact cohomology
sequences. A torsion sheaf is the filtered colimit $F=\varinjlim_nF[n]$ of its
subsheaves killed by $n$, and the filtered-colimit isomorphism above applies to
$f$ and $f'$, so the exchange map is an isomorphism for every torsion sheaf of
$\Lambda$-modules. Finally, the truncation argument at the end of the proof of
[sk-thm-iff] passes from sheaves to bounded below complexes with torsion
cohomology. Hence the exchange map for $K_{\mathrm{ét}}$ is an isomorphism in
$D^+(Y'_{\Et},\Lambda)$.

*Pro-étale site.* Finally apply $\nu_{Y'}^*$. Since $f$ and $f'$ are proper,
hence qcqs, the direct-image comparison [sk-thm-pe-direct-image-comparison]
applies. Together with the inverse-image comparison
$g_{\mathrm{proét}}^*\nu_Y^*\simeq\nu_{Y'}^*g_{\mathrm{ét}}^*$ it identifies
$\nu_{Y'}^*g^{-1}Rf_*K_{\mathrm{ét}}$ and
$\nu_{Y'}^*Rf'_*g'^{-1}K_{\mathrm{ét}}$ with $g^*Rf_*K$ and $Rf'_*g'^*K$ in
$D^+(Y'_{\mathrm{proét}},\Lambda)$. These comparisons respect the units and
counits, so the resulting isomorphism is the canonical pro-étale exchange
map.
