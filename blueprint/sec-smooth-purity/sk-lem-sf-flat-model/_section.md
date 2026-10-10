+++
id = "sk-lem-sf-flat-model"
kind = "section"
title = "Bounded flat model of finite Tor amplitude"
order = 1829
lean = ["AlgebraicGeometry.Etale.hasTorAmplitudeIn_iff_exists_flatModel"]
+++
*Lemma (sketch).*

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

## Proof

*(ii)$\Rightarrow$(i):* a bounded-above complex of flat sheaves is
K-flat, and $P\otimes_AM$ has terms only in degrees $[a,b]$.
*(i)$\Rightarrow$(ii):* choose a bounded-above free resolution
$P\to K$; testing with $M=A_T$ gives $H^q(P)=0$ for $q<a$; put
$Q=P^a/\mathrm{im}(P^{a-1}\to P^a)$ and compute
$\mathrm{Tor}^A_1(Q,M)=H^{a-1}(P\otimes_AM)=H^{a-1}(K\otimes^L_AM)=0$, so $Q$
is flat by the Tor form of the finite-relation criterion; then
$P'=[Q\to P^{a+1}\to\dots\to P^b]$ is the required model.
*Constructible variant:* build the bounded-above resolution $P\to K$
inductively in decreasing degree with terms finite direct sums of
$j_{V!}A_V$: the surjections needed at each step are onto the constructible
cohomology sheaves of $K$ and onto the constructible kernels and cokernels
that arise, and they exist by the key input, after refining each $V$ by a
finite affine étale cover so that the relevant sections lift
(SGA $4\frac12$, Rapport, 4.6–4.8). Then $Q=P^a/\mathrm{im}(P^{a-1}\to
P^a)$ is a cokernel of a map of constructible sheaves, hence constructible as
well as flat, and $P'$ is a bounded complex of flat constructible sheaves.
