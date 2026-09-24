+++
id = "lem-a1-reduction-upper-weight"
kind = "lemma"
title = "Upper-weight bound for the transported complex"
order = 4284
uses = ["def-weil-complex-weights", "def-weil-punctual-weights", "lem-zl-finite-pushforward"]
+++
Let $C_0$ be a smooth geometrically connected affine curve, let
$C'_0$ be a smooth geometrically connected curve containing $C_0$
as a dense open with finite complement, let
$g:C'_0\to\mathbf A^1_{k_0}$ be a finite generically etale morphism,
let $j:C_0\hookrightarrow C'_0$, and let $\mathcal F$ be lisse and
punctually $\iota$-pure of weight $w$ on $C_0$. Put
$\mathcal K:=g_*j_!\mathcal F$. Then $\mathcal K$ lies in
$D_{\le w}(\mathbf A^1_{k_0})$, the upper-weight category of
[def-weil-complex-weights].

## Proof

$j_!\mathcal F$ is punctually pure of weight $w$ (its stalks
are those of $\mathcal F$ on $C_0$, and $0$ elsewhere), hence lies
in $D_{\le w}(C'_0)$ (the [def-weil-complex-weights] notion, the
punctual purity being [def-weil-punctual-weights]), and the
upper-weight preservation of the finite pushforward
[lem-zl-finite-pushforward] gives
$\mathcal K\in D_{\le w}(\mathbf A^1_{k_0})$.
