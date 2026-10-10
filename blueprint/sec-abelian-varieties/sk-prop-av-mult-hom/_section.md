+++
id = "sk-prop-av-mult-hom"
kind = "section"
title = "The $n$-fold sum is a homomorphism"
lean = ["AlgebraicGeometry.isMonHom_npow_id"]
order = 493
uses = ["sk-cor-av-commutative", "sk-def-av-group-scheme", "sk-def-av-mult-n"]
+++
*Proposition (sketch).*

Let $G$ be a commutative group scheme over $k$ and $n\ge0$. Then the
$n$-fold sum map $[n]:G\to G$ (for $n=0$ the constant map to the unit
section) is a homomorphism of group schemes.

## Proof

For $n=0$ the map $[0]$ is the composite $G\to\Spec k\xrightarrow{e}G$
of the structure morphism and the unit section; on $R$-points it sends
every $x$ to the unit, which is a homomorphism of groups, so $[0]$ is a
homomorphism of group schemes.

For $n\ge1$ we have $[n]=m\circ([n-1],\mathrm{id}_G)$. The sum map
$m:G\times_kG\to G$ is a homomorphism when $G$ is commutative (the
group law of $G\times_kG$ is componentwise), and $([n-1],\mathrm{id}_G):
G\to G\times_kG$ is a homomorphism as soon as $[n-1]$ is one. By
induction on $n$, $[n]$ is a composite of homomorphisms, hence a
homomorphism.
