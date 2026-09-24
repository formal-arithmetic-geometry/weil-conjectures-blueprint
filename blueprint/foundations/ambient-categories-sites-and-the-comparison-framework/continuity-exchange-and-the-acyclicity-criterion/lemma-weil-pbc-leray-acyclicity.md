+++
id = "lemma-weil-pbc-leray-acyclicity"
kind = "lemma"
title = "Leray acyclicity criterion"
order = 1317
uses = ["def-sp-acyclic", "def-weil-pbc-direct-image", "def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-kinjective-resolutions", "lem-sp-edge-collapse", "thm-sp-if-e1"]
+++
If a complex $I^\bullet$ consists of $f'_*$-acyclic sheaves, then the natural
map $\mathcal H^q(f'_*I^\bullet)\to R^qf'_*K$ is an isomorphism whenever
$K\to I^\bullet$ is a quasi-isomorphism.

## Proof

Resolve $K$ by a bounded-below Cartan–Eilenberg double complex
$J^{r,s}$ with vertical differential $d_v:J^{r,s}\to J^{r+1,s}$ resolving
$I^s$ and horizontal differential $d_h:J^{r,s}\to J^{r,s+1}$ lifting the
differential of $I^\bullet$. Set
$d_{\mathrm{tot}}=d_v+(-1)^r d_h$. Applying $f'_*$ and filtering the total
complex by $r$ gives

$$
E_1^{r,s}=R^rf'_*I^s,\qquad
E_2^{r,s}=R^rf'_*\mathcal H^s(K)\Longrightarrow
\mathcal H^{r+s}(Rf'_*K).
$$

The assumed acyclicity makes $E_1^{r,s}=0$ for $r>0$, so the edge map from
the $r=0$ column is the cohomology map of the ordinary complex
$f'_*I^\bullet$. The sign $(-1)^r$ makes the square with the horizontal
differential commute, and the edge morphism is therefore exactly the natural
map $\mathcal H^q(f'_*I^\bullet)\to R^qf'_*K$. Collapse of the first column
proves it is an isomorphism.

## Detailed form

Let $F\to I^\bullet$ be a resolution by $f'_*$-acyclic sheaves and let $v$ be
a left exact functor. If every $I^m$ is $v$-acyclic, then $Rv(F)$ is
represented by $v(I^\bullet)$. Applied to $v=f'_*$ and $g'^{-1}I^m$, this
identifies the cohomology of the target of exchange with the cohomology of
the termwise underived target.

## Proof

Resolve $K\to I^\bullet$ by a bounded-below Cartan--Eilenberg double complex
and apply $v$: filtering the total complex by the first degree gives the
spectral sequence

$$
 E_1^{r,s}=R^rv(I^s)\Longrightarrow\mathcal H^{r+s}(RvK).
$$

The assumed acyclicity collapses the first column, so the edge map identifies
$\mathcal H^q(vI^\bullet)$ with $R^qvK$, compatibly with the K-injective
presentation of [def-weil-pbc-kinjective-resolutions].

## Detailed form

Let $F\in\mathcal A$ and let $F\to I^\bullet$ be a resolution of $F$ by
$v$-acyclic [def-sp-acyclic] objects $I^m$. Then $Rv(F)$ is represented by
$v(I^\bullet)$:

$$
 R^nv(F)=\mathcal H^n\bigl(v(I^\bullet)\bigr)\qquad(n\in\mathbb Z).
$$

## Proof

Resolve $I^\bullet$ by a Cartan--Eilenberg double complex as in
[thm-sp-if-e1] and apply $v$: the $E_1$-page is $E_1^{r,s}=R^rv(I^s)=0$ for
$r>0$, since the $I^s$ are $v$-acyclic in the sense of
[def-sp-acyclic], so by [lem-sp-edge-collapse] the first column
($E_1^{0,s}=\mathcal H^0(v(A^{\bullet,s}))=v(I^s)$) survives and the edge map
identifies

$$
 \mathcal H^n\bigl(v(\operatorname{tot}A)\bigr)
\xrightarrow{\ \sim\ }\mathcal H^n\bigl(v(I^\bullet)\bigr).
$$

By [thm-sp-if-e1] the left hand side is $\mathcal H^n(Rv(F))$. (*The same
statement holds with $v=f'_*$ and the acyclic sheaves $g'^{-1}I^m$ in the
conventions of the etale site of this chapter; the topoi form of the Leray
spectral sequence and the acyclicity criterion are Stacks Project Lemmas
21.14.5/21.14.6 (Tags
[0732](https://stacks.math.columbia.edu/tag/0732)/[0733](https://stacks.math.columbia.edu/tag/0733)),
and for ringed spaces Lemmas 20.13.4/20.13.8 (Tags
[01F2](https://stacks.math.columbia.edu/tag/01F2)/[01F6](https://stacks.math.columbia.edu/tag/01F6)).*)
