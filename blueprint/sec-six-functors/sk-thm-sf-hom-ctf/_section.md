+++
id = "sk-thm-sf-hom-ctf"
kind = "section"
title = "Internal Hom with finite Tor amplitude"
order = 2302
uses = ["sk-prop-sf-finiteness"]
+++
*Theorem (sketch).*

Let $K,M$ be bounded constructible $A$-complexes on $X_{\Et}$ with finite Tor
amplitude in $[a,b]$ and in $[c,d]$. Then $\RHom_A(K,M)$ is bounded
constructible with finite Tor amplitude in $[c-b,d-a]$.

## Proof

Constructibility: every cohomology sheaf of $\RHom_A(K,M)$ is constructible,
because the $\mathcal Ext$-sheaves of two constructible complexes are
constructible on a common stratification. Interval: at a geometric point
$\bar x$ the stalk is $\RHom_A(K_{\bar x},M_{\bar x})$ and is concentrated in
$[c-b,d-a]$, the stalk of $\RHom$ being computed by $\RHom$ of the stalks
here, because the two variables can be replaced
there by finite free models in their Tor-amplitude intervals. Since stalks are
exact and conservative on the étale site, $\mathcal H^n(\RHom_A(K,M))=0$
outside $[c-b,d-a]$.

Uses: `\Cref{prop:sf-finiteness}`, `lem:weil-pbc-geometric-stalk-conservative`
