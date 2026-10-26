+++
id = "lem-weil-bounded-finite-tor-perfect"
kind = "lemma"
title = "Bounded complexes of finite Tor amplitude are perfect"
lean = ["AlgebraicGeometry.Etale.exists_dense_open_exactPairing"]
order = 2390
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-site-perfect-complex"]
+++
Let $R$ be a Noetherian ring and let $K$ be a bounded complex of finite
$R$-modules with finite Tor amplitude in the sense of
[def-weil-finite-tor-amplitude]: there are integers $a\le b$ with
$\mathcal H^i(K\otimes^L_RM)=0$ for every $i\notin[a,b]$ and every
$R$-module $M$. Then $K$ is quasi-isomorphic to a bounded complex of
finite projective $R$-modules concentrated in degrees $[a,b]$. If
$R$ is local, projective is free, so $K$ is then site-perfect in the
sense of [def-weil-site-perfect-complex].
