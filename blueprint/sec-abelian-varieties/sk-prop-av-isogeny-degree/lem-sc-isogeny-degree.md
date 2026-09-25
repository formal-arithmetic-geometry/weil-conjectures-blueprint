+++
id = "lem-sc-isogeny-degree"
kind = "lemma"
title = "The degree of an isogeny"
order = 565
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-isogeny", "lem-sc-finite-constant-length-flat", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $f:A\to B$ be an isogeny of
abelian varieties over a field
$k$, with kernel $K=\ker f$ ([def-sc-group-scheme]), and
let $d:=\dim_k\mathcal O(K)$, the order of $K$, i.e. the
degree of $f$ in the sense of [def-sc-isogeny]. Then $f$
is finite and flat and $f_*\mathcal O_A$ is a locally free
$\mathcal O_B$-module of rank $d$: the degree of the finite
flat morphism $f$ is $d$.

## Proof

Since $f$ is an isogeny ([def-sc-isogeny]) it is a
surjective homomorphism of group schemes with finite kernel
$K=\ker f$ ([def-sc-group-scheme]), and $d=\dim_k\mathcal O(K)$ is its order. The morphism $f$ is proper, $A$ being
proper over $k$ ([def-sc-abelian-variety]), and its fibres
are finite: for a point $y=f(x)$ of $B$ the fibre
$f^{-1}(y)$ is the translate $x+K$ of the kernel, a finite
$k$-scheme. Hence $f$ is finite by
[thm-pqf-finite-iff-proper-finite-fibres] (the quasi-finite chapter).
Its fibre length is the constant $d$: over $y=f(x)$ the fibre
is $x+K$, which is isomorphic to $K$ over $\kappa(y)$, and
$\dim_{\kappa(y)}\bigl(\mathcal O(K)\otimes_k\kappa(y)\bigr)=d$.
By [lem-sc-finite-constant-length-flat], the finite
surjective morphism $f$ is flat and $f_*\mathcal O_A$ is
locally free of rank $d$.
