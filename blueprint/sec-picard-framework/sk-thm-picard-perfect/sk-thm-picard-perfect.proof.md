+++
kind  = "proof"
of    = "sk-thm-picard-perfect"
uses = ["sk-thm-picard-coherence", "sk-thm-picard-semicon"]
+++
*The lemma from the general form.* $f_T:C_T\to T$ is proper and of
finite presentation (base change of the projective $C\to\Spec k$), and
$\cL$ is of finite presentation and flat over $T$ (invertible on the
$T$-flat $C_T$). So [sk-thm-picard-coherence] (a) represents
$Rf_{T,*}\cL$ locally by a bounded complex of finite free modules whose
formation commutes with every base change, i.e.
$La^*Rf_{T,*}\cL\simeq Rf_{T',*}\cL_{T'}$. This is proper coherent base
change for a flat finitely presented module, together with the openness
criterion for a perfect complex (Stacks Project, Tags 0B91 and 0B9S). One
way to obtain the complex is to use a projective embedding, sufficiently
large twists and a finite affine Čech complex; Serre vanishing supplies
finite locally free models. After such a model has been obtained,
openness is a matrix calculation: near a point where the fibre has a
single cohomology group of rank $1$, cancel the differentials that are
invertible on the fibre; the remaining complex is a line bundle in
degree $0$. Precisely, the locus in question is $U_{0,1}$ of the general
form (with $X=C_T$, $\cF=\cL$, $i=0$, $r=1$), which is open; on it
$R^qf_{T,*}\cL=0$ for $q\ne0$ (in particular $R^1f_{T,*}\cL=0$),
$f_{T,*}\cL$ is invertible, and, by the functorial characterization,
its formation commutes with arbitrary base change $T'\to U_{0,1}$. No
Noetherian hypothesis enters the general form, which settles the case of
an arbitrary test scheme as well.

*The general form.* Upper semicontinuity ([sk-thm-picard-semicon]) makes each condition
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
