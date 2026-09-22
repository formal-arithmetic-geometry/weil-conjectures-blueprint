+++
id = "lem-kun-flat-bounded-tor-amplitude"
kind = "lemma"
title = "Bounded complexes of flat sheaves have tor amplitude"
order = 6029
lean = ["AlgebraicGeometry.Etale.hasTorAmplitude_of_bounded_flat"]
uses = ["lem-kun-kflat-criteria", "def-kun-tor-amplitude", "def-kun-derived-tensor"]
+++
Let $T$ be a scheme, $\Lambda$ a commutative ring, $a,b\in\mathbf Z$ with
$a\le b$, and let $\mathcal E^\bullet$ be a bounded complex of flat
$\Lambda_T$-module sheaves supported in degrees $[a,b]$. Then
$\mathcal E^\bullet$, regarded as an object of $D(T_{\Et},\Lambda)$, has tor
amplitude in $[a,b]$ [def-kun-tor-amplitude].

## Proof

A bounded-above complex of flat $\Lambda_T$-module sheaves is K-flat, so by
[def-kun-derived-tensor] the derived tensor product
$\mathcal E^\bullet\otimes^{\mathbf L}_\Lambda\mathcal M$ is computed by the
ordinary tensor product $\mathcal E^\bullet\otimes_\Lambda\mathcal M$, whose
terms in degrees outside $[a,b]$ vanish. Hence
$H^i(\mathcal E^\bullet\otimes^{\mathbf L}_\Lambda\mathcal M)=0$ for every
$i\notin[a,b]$ and every $\Lambda_T$-module sheaf $\mathcal M$ placed in
degree zero, which is tor amplitude in $[a,b]$.
