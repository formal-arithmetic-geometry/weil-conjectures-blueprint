+++
kind = "proof"
of = "sk-lem-sf-flat-model"
uses = ["sk-cor-pe-finite-tor-comparison", "sk-prop-sf-open-closed-triangle", "sk-lem-sf-determination"]
+++
By [sk-cor-pe-finite-tor-comparison], $C=\nu_X^*C_{\mathrm{ét}}$ with
$C_{\mathrm{ét}}\in\Dctf(X_{\mathrm{ét}},A)$, where
$\nu_X^*:D(X_{\mathrm{ét}},A)\to D(X_{\mathrm{proét}},A)$ is the comparison inverse
image. The complex $C_{\mathrm{ét}}$ has a bounded flat constructible model
(Stacks, Tag 0F4M, Lemma 59.77.3), and $\nu_X^*$, which is exact on sheaves,
pulls it back to a bounded flat constructible model on $X_{\mathrm{proét}}$.
Choose a common stratification on which its finitely many terms are locally
constant. A finite flat module over the Noetherian ring $A$ is finite
projective. For a flat constructible sheaf $F$, the successive open–closed
exact sequences express $F$ as a finite extension of the sheaves $a_!L$
attached to its strata, and the stupid filtration of the bounded flat complex
expresses $C$ as a finite extension of shifts of its *terms*. Each of these
operations preserves finite Tor amplitude. The same argument gives the
corresponding statement on $X_{\mathrm{ét}}$, which the compactness proof uses
before passing to the pro-étale site.

The lemma is phrased through flat models because the cohomology sheaves of
an object of $\Dctf$ need not have finite Tor amplitude. For example, the
complex $[A\xrightarrow{\ell}A]$ with $A=\mathbf Z/\ell^2\mathbf Z$ is perfect,
while its nonzero cohomology sheaves are copies of $\mathbf F_\ell$, which have
infinite projective dimension over $A$. Thus $\Dctf$ is a thick triangulated
category that is not the bounded derived category of an abelian category of
sheaves of finite Tor amplitude.

*The complement.* The generators lie in $\Dctf$: a lisse flat $L$ has Tor
amplitude $[0,0]$, and the extension by zero $j_!$ and the pushforward $Rg_*=g_*$
along the closed immersion $g$ are exact on sheaves and preserve
constructibility and flatness of stalks. Conversely, when $\Lambda$ is not a
field the truncations of an object of $\Dctf$ need not have finite Tor
amplitude, so one dévisses a flat model rather than the cohomology sheaves.
Every constructible sheaf is a quotient of a finite sum of the flat
constructible sheaves $j_{V!}\Lambda_V$, $V\to X$ affine étale (Stacks, Tag
095M), and kernels and cokernels of maps of constructible sheaves are
constructible; so, as in the first paragraph, $K\in\Dctf(X,\Lambda)$ is
isomorphic to a bounded complex $P$ of flat constructible sheaves. The
stupid-truncation triangles
$\sigma_{\ge q+1}P\to\sigma_{\ge q}P\to P^q[-q]\xrightarrow{+1}$ reduce the
claim to one flat constructible sheaf $F$: if a property $\mathcal P$ as in the
statement holds for every $P^q[-q]$, it holds for $P\cong K$, since
$\mathcal P$ is stable under shifts and extensions, contains $0$ and is closed
under isomorphisms.

For a flat constructible sheaf $F$ on a closed subscheme $W\subseteq X$, with
closed immersion $\iota:W\hookrightarrow X$, we show that $\mathcal P$ holds for
$\iota_*F$, by Noetherian induction on $W$ (the closed subsets of the
Noetherian space $X$ satisfy the descending chain condition); the case $W=X$
is the claim. If $W=\emptyset$ then $\iota_*F=0$. Otherwise, $W$ being
Noetherian and $F$ constructible, there is a dense open $U\subseteq W$ on which
$F$ is lisse; let $Z=W\setminus U$ with closed immersion $i:Z\hookrightarrow W$
and $j:U\hookrightarrow W$ the open immersion. The sequence
$0\to j_!(F|_U)\to F\to i_*i^*F\to0$ of [sk-prop-sf-open-closed-triangle] is a
distinguished triangle in $D(W,\Lambda)$, and $\iota_*$ is exact, so $\iota_*F$
is an extension of $\iota_*i_*i^*F$ by $\iota_*j_!(F|_U)$. Here $F|_U$ is lisse
with flat stalks, and since $U$ is dense in $W$ its closure in $X$ is $W$; so
$\iota_*j_!(F|_U)=Rg_*j_!L$ with $L=F|_U$, $g=\iota$, is a generator, for the
stratification of $X$ into the locally closed subsets $U$ and $X\setminus U$.
The sheaf $i^*F$ is flat constructible on the proper closed subset
$Z\subsetneq W$, so $\mathcal P$ holds for $\iota_*i_*i^*F$ by the induction
hypothesis. Hence $\mathcal P$ holds for $\iota_*F$. The generators produced
along the way are of the form $Rg_*j_!L$ for strata $U$ of stratifications of
$X$, and each extension used is a distinguished triangle.

Hence, by [sk-lem-sf-determination], a natural transformation of exact
functors on $\Dctf$ is invertible as soon as it is invertible on these
generators. For a single generator one may further pass to a finite étale
Galois cover $\pi:V\to U$ trivializing $L$, on which $\pi^*L$ is constant;
this reduction is local on $U$ and is not a dévissage, since $L$ need not be a
direct summand of $\pi_*\pi^*L$ when $\ell$ divides the order of the
monodromy. Constant coefficients alone do not generate: for $X=\mathbf G_m$,
$p\ne2$, $\Lambda=\mathbf F_3$, the complexes whose generic-stalk cohomology
has only trivial $\pi_1$-composition factors form a thick subcategory
containing every $Rg_*j_!\Lambda_U$ but not the order-$2$ Kummer sheaf.
