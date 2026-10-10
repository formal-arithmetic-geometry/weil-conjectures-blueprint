+++
kind  = "proof"
of    = "sk-prop-av-mult-hom"
+++
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
