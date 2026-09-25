+++
id = "lem-sf-hom-stalk"
kind = "lemma"
title = "The internal Hom at a stalk for a site-perfect first variable"
order = 2321
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-site-perfect-complex", "lem-sf-flat-model", "lem-sf-hom-finite-projective"]
+++
Let $A=A_{E,n}$, let $K$ be site-perfect on $X_{\Et}$ with Tor
amplitude $[a,b]$, and let $M\in D^b_{ctf}(X_{\Et},A)$ have Tor
amplitude $[c,d]$. For every geometric point $\bar x\to X$,

$$
(R\mathcal Hom_A(K,M))_{\bar x}
\cong R\operatorname{Hom}_A(K_{\bar x},M_{\bar x}),
$$

and the right side has Tor amplitude in $[c-b,d-a]$.

## Proof

By [def-weil-site-perfect-complex], locally $K$ admits a bounded
finite projective model $P$, which can be chosen in $[a,b]$ by
truncating a perfect resolution at its Tor bounds. The finite projective
calculation of [lem-sf-hom-finite-projective] gives
$R\mathcal Hom_A(K,M)=P^\vee\otimes_A^LM$. Exact monoidal stalks
commute with this expression and with the finite projective dual.
The dual model lies in $[-b,-a]$; tensor it with the bounded flat
model of $M$ from [lem-sf-flat-model] to obtain the asserted bound.
No left adjoint to the geometric stalk functor is used.
