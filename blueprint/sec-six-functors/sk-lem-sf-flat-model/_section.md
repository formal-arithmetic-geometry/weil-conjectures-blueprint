+++
id = "sk-lem-sf-flat-model"
kind = "section"
title = "Bounded flat model of finite Tor amplitude"
order = 2291
+++
*Lemma (sketch).*

Let $T$ be a scheme on which $\ell$ is invertible and let
$K\in\Dbc(T,A_{E,n})$ be bounded constructible on the small pro-étale site.
For integers $a\le b$ the following are equivalent: (i) $K$ has finite Tor
amplitude in $[a,b]$; (ii) $K$ is isomorphic to a bounded complex $P$ of
*flat* $A_T$-module sheaves with $P^q=0$ for $q\notin[a,b]$. The same
holds with the corresponding conditions on a small étale site.

## Proof

*(ii)$\Rightarrow$(i):* a bounded-above complex of flat sheaves is
K-flat, and $P\otimes_AM$ has terms only in degrees $[a,b]$.
*(i)$\Rightarrow$(ii):* choose a bounded-above free resolution
$P\to K$; testing with $M=A_T$ gives $H^q(P)=0$ for $q<a$; put
$Q=P^a/\mathrm{im}(P^{a-1}\to P^a)$ and compute
$\mathrm{Tor}^A_1(Q,M)=H^{a-1}(P\otimes_AM)=H^{a-1}(K\otimes^L_AM)=0$, so $Q$
is flat by the Tor form of the finite-relation criterion; then
$P'=[Q\to P^{a+1}\to\dots\to P^b]$ is the required model.

Uses: `def:weil-derived-tensor`, `def:weil-finite-tor-amplitude`, `lem:exc-constant-inverse-image-flat`
