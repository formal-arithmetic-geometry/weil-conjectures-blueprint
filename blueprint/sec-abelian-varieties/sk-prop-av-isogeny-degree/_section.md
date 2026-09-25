+++
id = "sk-prop-av-isogeny-degree"
kind = "section"
title = "The degree of an isogeny is the degree of the kernel"
order = 559
uses = ["sk-def-av", "sk-def-av-group-scheme", "sk-def-av-isogeny", "sk-prop-av-mult-finite", "sk-prop-av-pqf-finite"]
+++
*Proposition (sketch).*

Let $f:A\to B$ be an isogeny of abelian varieties ([sk-def-av-isogeny])
with kernel $K$ of order $d=\dim_k\cO_K$. Then $f$ is finite and flat
and $f_*\cO_A$ is a locally free $\cO_B$-module of rank $d$: the
degree of the finite flat morphism $f$ equals the order of its kernel.

## Proof

$f$ is proper ($A$ is proper) and its fibres are translates $x+K$ of
the finite kernel, hence finite; so $f$ is finite by
[sk-prop-av-pqf-finite]. All fibres have the same length $d$, since the
fibre over $y=f(x)$ is $x+K\cong K$ over $\kappa(y)$ with
$\dim_{\kappa(y)}(\cO_K\otimes_k\kappa(y))=d$. A finite surjective
morphism with constant fibre length is flat and locally free of that
rank (blueprint lem:sc-finite-constant-length-flat), so
$f_*\cO_A$ is locally free of rank $d$.

Uses: [sk-def-av-group-scheme], [sk-def-av-isogeny], [sk-def-av], [sk-prop-av-mult-finite], [sk-prop-av-pqf-finite]
