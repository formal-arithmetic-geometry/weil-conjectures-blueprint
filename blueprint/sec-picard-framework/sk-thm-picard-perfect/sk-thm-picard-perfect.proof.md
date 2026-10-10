+++
kind  = "proof"
of    = "sk-thm-picard-perfect"
+++
Upper semicontinuity ([sk-thm-picard-semicon]) makes each condition
$h^q(t)=0$ ($q\neq i$) and $h^i(t)\le r$ open, and locally only finitely
many $q$ matter (the complex $K^\bullet$ below is bounded), so
$U_{i,\le r}$ is open. Over an affine open of $U_{i,\le r}$ let
$K^\bullet=[K^a\to\dots\to K^b]$ be the bounded complex of finite free
modules of the proof of [sk-thm-picard-semicon], whose formation
commutes with base change, so that
$H^q(K^\bullet\otimes\kappa(t))=H^q(X_t,\cF_t)$. At $t\in U_{i,\le r}$
the complex $K^\bullet\otimes\kappa(t)$ is exact outside degree $i$.
If $b>i$, then $d^{b-1}\otimes\kappa(t)$ is surjective, so by Nakayama
$d^{b-1}$ is surjective near $t$ and, its target being free, split:
$K^\bullet$ is locally quasi-isomorphic to the shorter complex
$[K^a\to\dots\to\ker d^{b-1}]$ of finite free modules. If $a<i$, then
$d^a\otimes\kappa(t)$ is injective, so some maximal minor of $d^a$ is a
unit near $t$, $d^a$ is a split injection there, and $K^\bullet$ is
locally quasi-isomorphic to $[\operatorname{coker}d^a\to\dots\to K^b]$.
After finitely many such steps $K^\bullet$ is, near $t$, quasi-isomorphic
to a single finite free module $M$ placed in degree $i$, and these
reductions commute with base change. Hence $h^i(t')=\operatorname{rk}M$
for all $t'$ near $t$, which gives the local constancy of $h^i$ on
$U_{i,\le r}$ (so $U_{i,r}$ is open and closed in $U_{i,\le r}$), the
local description $R^if_*\cF=M$, the vanishing of $R^qf_*\cF$ for
$q\neq i$, and the base-change isomorphisms. For the functorial
characterization: if $Rf_{T',*}\cF_{T'}\cong\mathcal E[-i]$ with $\mathcal E$ locally
free of rank $r$, then every $t'\in T'$ has $h^q(t')=r\,\delta_{q,i}$,
and $h^q(t')=h^q(t)$ for $t$ the image of $t'$ (cohomology commutes with
field extension), so $T'\to T$ factors through the open $U_{i,r}$; the
converse is base change. The detailed forms are Blueprint 50,
`lem-pc-perfect-locus` and `lem-pc-flat-rf-open`.
