+++
id = "det-av-final-etale"
kind = "lemma"
title = "Multiplication by an invertible integer is étale"
uses = ["sk-prop-av-mult-hom", "sk-prop-av-mult-finite", "sk-prop-av-mult-surjective", "sk-prop-av-isogeny"]
+++
Let $B$ be an abelian variety of dimension $g$ over a field $k$ and let
$n>0$ be invertible in $k$. Then:

1. the differential of $[n]$ at the identity,
$d[n]_e:T_eB\to T_eB$, is multiplication by $n$, hence an isomorphism;
1. for every point $x\in B(\bar k)$ the differential
$d[n]_x:T_xB_{\bar k}\to T_{nx}B_{\bar k}$ is an isomorphism;
1. $[n]:B\to B$ is étale; consequently $B[n]=[n]^{-1}(e)$ is a finite
étale $k$-group scheme, of rank $\deg[n]$.
