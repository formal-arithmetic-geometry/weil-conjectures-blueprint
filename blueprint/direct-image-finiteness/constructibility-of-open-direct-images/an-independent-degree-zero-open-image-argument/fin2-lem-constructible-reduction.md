+++
id = "fin2-lem-constructible-reduction"
kind = "lemma"
title = "Reduction of the constructible case to lisse pieces"
order = 3217
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "fin2-lem-lisse-dense-open", "lem-fin-closed-immersion", "lem-weil-pbc-grothendieck-spectral-sequence", "lem-weil-pbc-proper-composition", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions", "thm-constructible-serre"]
+++
Let $V$ be the assertion: for every proper morphism $p:Y\to T$ with
$T$ of finite type over $k$, every
locally closed constructible
immersion $j:U\hookrightarrow Y$ and every
lisse $\Lambda$-sheaf
$G$ on $U_{{\mathrm{et}}}$ (the ring $\Lambda$ of
[sbc-def-coefficient-conventions]), the higher direct images
$R^qp_*(j_!G)$ of [def-weil-pbc-direct-image] are
constructible on
$T_{{\mathrm{et}}}$ for every $q\geq0$ and vanish for $q>2e$, where
$e$ bounds the dimensions of the
geometric fibres of $p$.
Assume $V$. Then the same holds without the lisse hypothesis: for
every proper $p:Y\to T$ with $T$ of finite type over $k$ whose
geometric fibres have dimension at most $d\in\mathbf Z_{\geq0}$ and
every constructible $\Lambda$-sheaf $F$ on $Y_{{\mathrm{et}}}$, the
sheaves $R^qp_*F$ are constructible on $T_{{\mathrm{et}}}$ for all
$q\geq0$ and vanish for $q>2d$.

## Proof

Assume the assertion $V$ in the statement. We prove the conclusion
by induction on the dimension of the Noetherian source $Y$,
simultaneously for all proper $p:Y\to T$, all fibre bounds $d$,
and all constructible sheaves $F$ on $Y$. If $Y$ is empty all
direct images are zero. Otherwise
[fin2-lem-lisse-dense-open] supplies an open immersion
$j:U\hookrightarrow Y$ such that $G=j^*F$ is lisse and the
reduced closed complement $i:Z\hookrightarrow Y$ has
$\dim Z<\dim Y$.

The inverse-image and extension-by-zero constructions of
[def-weil-pbc-inverse-image], [def-weil-pbc-extension-by-zero]
give a short exact sequence

$$
0\longrightarrow j_!G\longrightarrow F
\longrightarrow i_*i^*F\longrightarrow0.
$$

Indeed at a geometric point of $U$ this is
$0\to F_{\bar y}\xrightarrow{1}F_{\bar y}\to0\to0$;
at a geometric point of $Z$ it is
$0\to0\to F_{\bar y}\xrightarrow{1}F_{\bar y}\to0$.
Exactness follows from
[lemma-weil-pbc-geometric-stalk-conservative].

The assertion $V$ applies to $p$, the open (hence locally closed)
immersion $j$, and the lisse $G$. Thus
$A_q=R^qp_*(j_!G)$ is constructible for every $q$, and is zero
for $q>2d$.
The restriction $i^*F$ is constructible on $Z$: intersect the
finite lisse stratification of $F$ with $Z$.
The closed immersion $i$ is proper in the scheme conventions of
[def-weil-pbc-scheme-conventions], so $p\circ i$ is proper by
[lem-weil-pbc-proper-composition]. Each of its geometric fibres is
a closed subscheme of the corresponding fibre of $p$, hence has
dimension at most $d$.
The induction hypothesis therefore makes
$B_q=R^q(p\circ i)_*(i^*F)$ constructible and zero for $q>2d$.
The exactness of closed-immersion direct image in
[lem-fin-closed-immersion], together with
[lem-weil-pbc-grothendieck-spectral-sequence], identifies
$B_q$ with $R^qp_*(i_*i^*F)$.

Apply $Rp_*$ to the displayed short exact sequence. Its long
exact cohomology sequence gives the short exact sequence

$$
0\longrightarrow\operatorname{coker}(B_{q-1}\longrightarrow A_q)
\longrightarrow R^qp_*F
\longrightarrow\ker(B_q\longrightarrow A_{q+1})
\longrightarrow0,
$$

where $B_{-1}=0$.
Both the kernel and the cokernel are constructible: they are kernels
and cokernels of morphisms between constructible sheaves.
The weak-Serre property of [thm-constructible-serre]
then makes their extension $R^qp_*F$ constructible.
For $q>2d$ both outer terms are zero, whence the middle term is
zero as well. This completes the induction and proves the full
conclusion under the stated hypothesis $V$.
