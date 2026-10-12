+++
id = "sk-lem-sf-flat-model"
kind = "lemma"
title = "Bounded flat model of finite Tor amplitude"
order = 2133
lean = ["AlgebraicGeometry.Etale.hasTorAmplitudeIn_iff_exists_flatModel"]
tags = ["sketch"]
+++
Let $A$ be a finite commutative ring (for instance $A=A_{E,n}$), let $T$ be a
scheme and let $K\in\Dbc(T_{\Et},A)$ be bounded constructible on the small
étale site. For integers $a\le b$ the following are equivalent: (i) $K$ has
Tor amplitude in $[a,b]$, i.e. $\mathcal H^r(K\otimes^L_AM)=0$ for every
sheaf $M$ of $A_T$-modules and every $r\notin[a,b]$; (ii) $K$ is isomorphic
to a bounded complex $P$ of *flat* $A_T$-module sheaves with $P^q=0$ for
$q\notin[a,b]$. The same holds with the corresponding conditions on the
small pro-étale site.
*Constructible variant:* if $T$ is Noetherian (for instance of finite
type over $k$) and $K\in\Dbc(T_{\Et},A)$ has finite Tor amplitude in
$[a,b]$, then $K$ is isomorphic to a bounded complex $P$ of flat
*constructible* $A_T$-module sheaves with $P^q=0$ for $q\notin[a,b]$;
in particular every object of $\Dctf(T_{\Et},A)$ has such a model.
The key input is that every constructible sheaf of $A$-modules on
$T_{\Et}$ is a quotient of a finite direct sum of sheaves $j_{V!}A_V$ with
$j_V:V\to T$ étale and $V$ affine, and that kernels and cokernels of maps of
constructible sheaves are constructible.
