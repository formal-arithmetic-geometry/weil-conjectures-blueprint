+++
id = "sk-lem-sf-open-ctf"
kind = "section"
title = "Extension by zero preserves the finite-Tor constructible category"
order = 2159
uses = ["sk-def-sf-operations"]
lean = ["AlgebraicGeometry.Etale.constructibleTorAmplitudeIn_rightDerivedLowerShriek"]
+++
*Lemma (sketch).*

Let $j:U\hookrightarrow Y$ be an open immersion admitting a compactification,
let $a\le b$ be integers, and let $K$ be a bounded constructible complex of
$\Lambda$-modules on $U$ with cohomology concentrated in $[a,b]$ and Tor
amplitude in $[a,b]$. Then $Rj_!K$ is bounded constructible on $Y$, with
cohomology concentrated in $[a,b]$ and Tor amplitude in $[a,b]$; in particular
$j_!$ carries $\Dctf(U,\Lambda)$ into $\Dctf(Y,\Lambda)$ without moving the
interval.

## Proof

$j_!$ is exact, so
$\mathcal H^r(j_!K)=j_!\mathcal H^r(K)$ and the range does not grow; a finite
stratification of $U$ witnessing constructibility, together with the closed
complement $Y\setminus U$, stratifies $Y$; and the amplitude is tested by
restricting an arbitrary sheaf on $Y$ to $U$.
