+++
kind  = "proof"
of    = "sk-thm-picard-perfect"
+++
*The lemma from the general form.* $f_T:C_T\to T$ is proper and of
finite presentation (base change of the projective $C\to\Spec k$), and
$\cL$ is of finite presentation and flat over $T$ (invertible on the
$T$-flat $C_T$). Since $f_T$ is moreover quasi-compact and separated, the
base change map $La^*Rf_{T,*}\cL\to Rf_{T',*}\cL_{T'}$ is an isomorphism
in the derived category for every $a:T'\to T$
([lem-pc-relatively-flat-canonical-module-base-change]). If $T$ is locally Noetherian,
$Rf_{T,*}\cL$ is perfect on every affine open of $T$
([lem-pc-rf-perfect-base-change] (3)), that is, locally represented by a
bounded complex of finite locally free modules. This is proper coherent
base change for a flat finitely presented module, together with the
openness criterion for a perfect complex (Stacks Project, Tags 0B91 and
0B9S). Once such a local
model is available, openness is a matrix calculation: near a point where
the fibre has a single cohomology group of rank $1$, cancel the
differentials that are invertible on the fibre; the remaining complex is
a line bundle in degree $0$. Precisely, the locus in question is
$U_{0,1}$ of the general form (with $X=C_T$, $\cF=\cL$, $i=0$, $r=1$),
which is open; on it $R^qf_{T,*}\cL=0$ for $q\ne0$ (in particular
$R^1f_{T,*}\cL=0$), $f_{T,*}\cL$ is invertible, and
$Rf_{T,*}\cL\cong f_{T,*}\cL[0]$. For $a:T'\to U_{0,1}$ the derived base
change isomorphism then reads $f_{T',*}\cL_{T'}[0]\cong a^*f_{T,*}\cL[0]$,
since the derived pullback of a locally free module is its pullback; so the
formation of $f_{T,*}\cL$ commutes with arbitrary base change. No
Noetherian hypothesis enters the general form, which settles the case of
an arbitrary test scheme as well.

*The general form.* Upper semicontinuity ([det-thm-picard-semicon]) makes
each condition $h^q(t)=0$ ($q\neq i$) and $h^i(t)\le r$ open, and locally
only finitely many $q$ matter (the local complex below is bounded, so
$h^q=0$ near a point for $q$ outside its range), so $U_{i,\le r}$ is open.
Near a point $t\in U_{i,\le r}$ let $K^\bullet=[K^a\to\dots\to K^b]$ be the
bounded complex of finite free modules of [det-thm-picard-coherence] (a),
so that $H^q(g^*K^\bullet)\cong R^qf'_*\cF'$ for every base change $g$ into
that neighbourhood; for $g$ the inclusion of a point this gives
$H^q(K^\bullet\otimes\kappa(t))=H^q(X_t,\cF_t)$. At $t$ the complex
$K^\bullet\otimes\kappa(t)$ is exact outside degree $i$.
If $b>i$, then $d^{b-1}\otimes\kappa(t)$ is surjective, so by Nakayama
$d^{b-1}$ is surjective near $t$ and, its target being free, split:
$K^\bullet$ is locally homotopy equivalent to the shorter complex
$[K^a\to\dots\to\ker d^{b-1}]$ of finite free modules. If $a<i$, then
$d^a\otimes\kappa(t)$ is injective, so some maximal minor of $d^a$ is a
unit near $t$, $d^a$ is a split injection there, and $K^\bullet$ is
locally homotopy equivalent to $[\operatorname{coker}d^a\to\dots\to K^b]$.
After finitely many such steps $K^\bullet$ is, near $t$, homotopy
equivalent to a single finite free module $M$ placed in degree $i$; a
homotopy equivalence survives every pullback $g^*$. Hence, near $t$,
$R^qf'_*\cF'\cong H^q(g^*K^\bullet)$ vanishes for $q\neq i$ and
$R^if'_*\cF'\cong g^*M$ for every base change $g$ into that
neighbourhood (with $g$ the identity: $R^if_*\cF\cong M$ there), and
$h^i(t')=\operatorname{rk}M$ for all $t'$ near $t$. This gives the local
constancy of $h^i$ on $U_{i,\le r}$ (so $U_{i,r}$ is open and closed in
$U_{i,\le r}$), the vanishing of $R^qf_*\cF$ for $q\neq i$, and the local
freeness of $R^if_*\cF$ on $U_{i,r}$. For the base change of $R^if_*\cF$
along a morphism $g:T'\to U_{i,r}$ one needs an isomorphism defined on all
of $T'$, not only locally: the derived direct image $E$ of $\cF$ over
$U_{i,r}$ has cohomology sheaves $0$ outside degree $i$ and the finite
locally free $R^if_*\cF$ in degree $i$, so $E\cong R^if_*\cF[-i]$ and its
derived pullback is $g^*R^if_*\cF[-i]$; and, $\cF$ being flat over $T$,
the base change map $Lg^*E\to Rf'_*\cF'$ is an isomorphism
([lem-pc-relatively-flat-canonical-module-base-change],
[lem-pc-higher-direct-image-derived-model]; this is how the local complexes
of [det-thm-picard-coherence] (a) arise). Hence
$Rf'_*\cF'\cong g^*R^if_*\cF[-i]$, that is,
$R^if'_*\cF'\cong g^*R^if_*\cF$ and $R^qf'_*\cF'=0$ for $q\neq i$. For the functorial characterization:
if $R^qf_{T',*}\cF_{T'}=0$ for $q\neq i$ and $R^if_{T',*}\cF_{T'}$ is
finite locally free of rank $r$, then near each $t'\in T'$ the complex
$g^*K^\bullet$ is a bounded complex of finite free modules with that
cohomology, hence homotopy equivalent to the cohomology placed in degree
$i$, so its fibre at $t'$ has cohomology of dimension $r$ in degree $i$
only; that fibre computes $H^*(X_t,\cF_t)\otimes_{\kappa(t)}\kappa(t')$ for
$t$ the image of $t'$ (cohomology commutes with field extension), so
$T'\to T$ factors through the open $U_{i,r}$; the converse was shown
above. The detailed forms are [lem-pc-perfect-locus] and
[lem-pc-flat-rf-open].
