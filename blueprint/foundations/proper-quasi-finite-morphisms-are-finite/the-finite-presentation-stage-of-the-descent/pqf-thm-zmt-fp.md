+++
id = "pqf-thm-zmt-fp"
kind = "theorem"
title = "Zariski's main theorem: the finite-presentation refinement"
order = 2140
uses = ["def-weil-pbc-scheme-conventions", "pqf-def-quasifinite", "pqf-lem-limit-iso-descends", "pqf-lem-limit-qc-open-descends", "thm-pqf-immersion-descent", "thm-pqf-zmt-factorization"]
+++
Let $f:X\to S$ be a
separated morphism of finite
type which is everywhere
quasi-finite and
locally of finite
presentation, with $S$
quasi-compact and
quasi-separated. Then there exist a scheme $T$ and a quasi-compact
open immersion
$j:X\hookrightarrow T$ such that $T\to S$ is
finite and of
finite presentation over
$S$, and $f$ is the composite of $j$ with $T\to S$.
(*Stacks Project, More on Morphisms, Lemma 37.43.4, Tag
[0F2N](https://stacks.math.columbia.edu/tag/0F2N). Its input is the
finite scheme $T_0$ of clause (i) of
the interface of this chapter, and
the presentation of $T_0$ used in
the proof is Limits of Schemes, Lemma 32.9.8, Tag
[09YY](https://stacks.math.columbia.edu/tag/09YY); both statements are
quoted verbatim in the source note of this section.*)

## Proof

By [thm-pqf-zmt-factorization], applied to the everywhere
quasi-finite morphism $f$ of [pqf-def-quasifinite] over the
quasi-compact quasi-separated base $S$, there are a scheme $T_0$, a
quasi-compact open immersion $e:X\hookrightarrow T_0$ and a
[def-weil-pbc-scheme-conventions] finite morphism $p:T_0\to S$ with
$f=p\circ e$: this is the factorization of clause (i) of the interface
[thm-pqf-immersion-descent], whose proof supplies the displayed
factorization.

By Tag 09YY, quoted in the source note of this section and applied to the
*finite* morphism $p:T_0\to S$ over the quasi-compact
quasi-separated base $S$, the scheme $T_0$ is a directed limit
$T_0=\varprojlim_kT_k$ in which all transition morphisms
$T_{k'}\to T_k$ are closed immersions and every $T_k$ is finite and of
finite presentation over $S$. Each $T_k$ is then quasi-compact and
quasi-separated and locally of finite type over $S$ by the definitions
of [def-weil-pbc-scheme-conventions].

The open subscheme $e(X)\subset T_0$ is quasi-compact, because $e$ is a
quasi-compact open immersion; so [pqf-lem-limit-qc-open-descends]
applies to it: there are an index $k_1$ and a quasi-compact open
$U_{k_1}\subset T_{k_1}$ with $e(X)=T_0\times_{T_{k_1}}U_{k_1}$, and if
$U_k\subset T_k$ denotes the preimage of $U_{k_1}$ for $k\ge k_1$,
then clause (3) of the same lemma exhibits $e(X)$ as the filtered limit
$\varprojlim_{k\ge k_1}U_k$ with the projections of the limit.

For $k'\ge k\ge k_1$ the transition morphism $U_{k'}\to U_k$ is the
base change of the closed immersion $T_{k'}\to T_k$, hence is a closed
immersion, and $U_k$ is an open subscheme of $T_k$, hence
quasi-compact and locally of finite type over $S$ by
[def-weil-pbc-scheme-conventions]. The scheme $e(X)$ is isomorphic
to $X$, so $e(X)\to S$ is locally of finite presentation, $f$ being
locally of finite presentation. Therefore
[pqf-lem-limit-iso-descends] applies to the filtered limit
$e(X)=\varprojlim_{k\ge k_1}U_k$: the projection $e(X)\to U_{k_0}$ is
an isomorphism for some $k_0\ge k_1$.

Put $T:=T_{k_0}$, and let $j:X\hookrightarrow T$ be the composite of the
isomorphism $X\to e(X)$ inverse to $e$, the inverse of the isomorphism
$e(X)\to U_{k_0}$, and the open immersion
$U_{k_0}\hookrightarrow T_{k_0}$. This is a quasi-compact open
immersion, as a composite of isomorphisms with the quasi-compact open
immersion $U_{k_0}\hookrightarrow T_{k_0}$ of
[pqf-lem-limit-qc-open-descends](1), and $T=T_{k_0}\to S$ is finite
and of finite presentation over $S$ by the choice of the system
$\{T_k\}$. Finally $j$ followed by $T_{k_0}\to S$ equals
$f=p\circ e$: the projections of the limit $T_0=\varprojlim_kT_k$ are
compatible with the structure morphisms to $S$, and $X\to T_{k_0}$
followed by the projection $T_{k_0}\to T_0$ is the open immersion $e$.
