+++
id = "lem-sf-bounded-free-model"
kind = "lemma"
title = "Bounded free model over a finite coefficient ring"
order = 2337
uses = ["def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-etale-site", "lem-sf-stalk-free-model"]
+++
Let $A=A_{E,n}$ be the finite coefficient ring of
[def-weil-finite-torsion-constructibility], let $V$ be a bounded
complex of $A$-modules whose cohomology modules $H^r(V)$ are finite and
vanish outside $[a,b]$, and assume that $H^r(V\otimes^L_AN)=0$ for every
$A$-module $N$ and every $r\notin[a,b]$. Then $V$ is isomorphic in
$D(A)$ to a bounded complex $F$ of finite free $A$-modules with
$F^q=0$ for $q\notin[a,b]$.

## Proof

Put $\kappa_E=A/(\varpi_E)$ and let $V_{\Spec\kappa_E}$ be the constant
complex with value $V$ on the
small étale site of
$\Spec\kappa_E$. Its cohomology sheaves are the constant sheaves with the
finite values $H^r(V)$, hence constructible in the sense of
[def-weil-finite-torsion-constructibility]. It has
finite Tor amplitude in
$[a,b]$: choose a K-flat resolution $Q\to V$ of the module complex
$V$; each constant sheaf with a flat $A$-module value is a flat
$A$-module sheaf, tensoring it with an injection of $A$-module sheaves
being injective on sections and evaluation at an object being left exact, so
$Q_{\Spec\kappa_E}$ is K-flat, and for a sheaf $M$ of $A$-modules the
complex $Q_{\Spec\kappa_E}\otimes_AM$ has as its sections over an object
$U$ the complex $Q\otimes_AM(U)$, whose cohomology is
$H^r(V\otimes^L_AM(U))$ and therefore vanishes for $r\notin[a,b]$ by the
hypothesis applied to the $A$-module $M(U)$; this is the asserted Tor
amplitude of $V_{\Spec\kappa_E}\otimes^L_AM$. The scheme
$\Spec\kappa_E$ has a single geometric point $\bar t$, and the stalk of
a constant complex at $\bar t$ is its value $V$. The statement is
therefore [lem-sf-stalk-free-model] for the complex
$V_{\Spec\kappa_E}$ and the geometric point $\bar t$.
