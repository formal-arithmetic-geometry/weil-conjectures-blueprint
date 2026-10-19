+++
kind  = "proof"
of    = "lemma-nagata-dense-flat-pullback"
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
We first prove the general statement and then deduce the first one. This is
Stacks Project, Tag 081I; the argument below uses only that $g$ is
quasi-compact.

**Step 1: the kernel over an affine open.** Let
$V=\operatorname{Spec}(A)\subseteq Y$ be an affine open. Since $g$ is
quasi-compact, $g^{-1}(V)$ is covered by finitely many affine opens
$T_k=\operatorname{Spec}(C_k)$, $k=1,\ldots,n$. Because $\mathcal O_T$ is a
sheaf, for every open $V_0\subseteq V$ the restriction map
$\Gamma(g^{-1}(V_0),\mathcal O_T)\to\prod_k\Gamma(T_k\cap g^{-1}(V_0),
\mathcal O_T)$ is injective. Hence the kernel of
$\mathcal O_V\to(g_*\mathcal O_T)|_V$ equals the kernel of
$\mathcal O_V\to\bigoplus_k(g_k)_*\mathcal O_{T_k}$, where
$g_k\colon T_k\to V$ is the restriction of $g$. Each $g_k$ is a morphism of
affine schemes, so $(g_k)_*\mathcal O_{T_k}$ is the quasi-coherent sheaf
associated with the $A$-module $C_k$. Therefore the kernel of
$\mathcal O_V\to(g_*\mathcal O_T)|_V$ is the quasi-coherent ideal associated
with

$$
I=\ker\Bigl(A\longrightarrow\prod_{k=1}^nC_k\Bigr).
$$

In particular this kernel is quasi-coherent, so by
[def-nagata-scheme-theoretic-image] and [lemma-nagata-scheme-image-ideal-qc]
it is $\ker(g)|_V$, and $\operatorname{SIm}(g)\cap V=\operatorname{Spec}(A/I)$.

**Step 2: flat base change over affine opens.** Let
$V'=\operatorname{Spec}(B)\subseteq q^{-1}(V)$ be an affine open; the ring
map $A\to B$ is flat. The base change $g'$ is quasi-compact, and
$g'^{-1}(V')=g^{-1}(V)\times_VV'$ is covered by the finitely many affine opens
$T_k\times_VV'=\operatorname{Spec}(C_k\otimes_AB)$. Step 1 applied to $g'$
and this cover gives

$$
\ker(g')|_{V'}=\ker\Bigl(B\longrightarrow\prod_{k=1}^n
C_k\otimes_AB\Bigr)^{\sim}.
$$

The sequence $0\to I\to A\to\prod_kC_k$ is exact and the product is finite,
so tensoring with the flat $A$-algebra $B$ gives an exact sequence
$0\to I\otimes_AB\to B\to\prod_k C_k\otimes_AB$. Hence the kernel above is
the image of $I\otimes_AB\to B$, that is, $IB$. On the other hand,
$\operatorname{SIm}(g)\times_YV'=\operatorname{Spec}(A/I)\times_{\operatorname{Spec}(A)}
\operatorname{Spec}(B)=\operatorname{Spec}(B/IB)$, so by
[def-nagata-extended-ideal] the ideal of the closed subscheme
$\operatorname{SIm}(g)\times_YY'\hookrightarrow Y'$ is also $IB$ on $V'$.

**Step 3: globalization.** The affine opens $V'$ as in Step 2, for $V$
running over the affine opens of $Y$, cover $Y'$. Two quasi-coherent ideal
sheaves of $\mathcal O_{Y'}$ that agree on every member of an open cover are
equal. Hence $\ker(g')$ equals the ideal sheaf of
$\operatorname{SIm}(g)\times_YY'$, which is the general statement.

**Step 4: the dense case.** Apply the general statement to $g=h$ and
$q\colon P\to X$. By hypothesis $\ker(h)=0$, i.e.
$\operatorname{SIm}(h)=X$, and the pullback of the closed subscheme $X$ of
$X$ along $q$ is $P$ itself, with ideal $0$. Hence the kernel of
$U\times_XP\to P$ is $0$, i.e. its scheme-theoretic image is $P$.
