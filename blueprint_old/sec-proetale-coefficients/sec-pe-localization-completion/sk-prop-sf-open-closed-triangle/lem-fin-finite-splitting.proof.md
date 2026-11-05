+++
kind  = "proof"
of    = "lem-fin-finite-splitting"
+++
The morphism $f$ is finite in the sense of
[def-weil-pbc-scheme-conventions], hence affine. Given $(U,\bar u)$, replace
$U$ by an affine open neighbourhood of the image of $\bar u$ lying over an
affine open of $S$; we may assume $U=\operatorname{Spec}R$ and
$X\times_SU=\operatorname{Spec}C$ with $C$ a finite $R$-algebra. Let
$A=\mathcal O^{{\mathrm{sh}}}_{U,\bar u}$ be the strict henselization of
[def-weil-pbc-strict-henselization-limit], the filtered colimit of the rings
$A_V$ of the affine pointed etale neighbourhoods $(V,\bar v)$ of $(U,\bar u)$.
The ring $A$ is strictly henselian local (Stacks Project, Algebra, Lemma
10.155.10, Tag [04GQ](https://stacks.math.columbia.edu/tag/04GQ)), so the
finite $A$-algebra $B=C\otimes_RA=\varinjlim_VC\otimes_RA_V$ is a finite product
$B=B_1\times\cdots\times B_m$ of local rings (Algebra, Lemma 10.153.3 (10), Tag
[04GG](https://stacks.math.columbia.edu/tag/04GG)). The residue field of each
$B_k$ is finite over the separably closed residue field of $A$, hence purely
inseparable over it; as $\Omega$ is algebraically closed, each factor has
exactly one $\Omega$-point over $\bar s$. This gives a bijection between the
factors and the points $\bar x$ of the geometric fibre
[def-weil-pbc-geometric-fibre], the factor $B_{\bar x}$ being the one through
which $\bar x$ factors.

Let $e_{\bar x}\in B$ be the factor idempotents. Each comes from $C\otimes_RA_V$
for some $V$, and the finitely many relations $e_{\bar x}^2=e_{\bar x}$,
$e_{\bar x}e_{\bar x'}=0$ for $\bar x\ne\bar x'$, $\sum e_{\bar x}=1$ and
$\bar x^*(e_{\bar x'})=\delta_{\bar x\bar x'}$ hold after passing to a further
neighbourhood, since $B$ is the filtered colimit of the $C\otimes_RA_V$. Over
such a $V$ the basic opens of the idempotents decompose
$X\times_SV=\operatorname{Spec}(C\otimes_RA_V)$ into pairwise disjoint
open-and-closed pieces $X_{\bar x}$, with $(\bar v,\bar x)\in X_{\bar x}$. The
structure map $V\to U$ is the required morphism of pointed neighbourhoods.
Finally $X_{\bar x}\to V$ is finite, as a closed subscheme of the finite
$V$-scheme $X\times_SV$.
