+++
kind  = "proof"
of    = "lem-sc-mult-n-homomorphism"
+++
We work on $R$-points, where the functor of points is faithful
([def-sc-group-scheme]); write $\cdot$ for the group law of
$G(R)$ and $e$ for its unit.

(a) By induction on $n$ one has $[n](R)(x)=x\cdot\ldots\cdot x$
($n$ factors): this holds for $n=0$ by the definition of $[0]$, for
$n=1$ because $[1]=m\circ(e\circ p,\mathrm{id}_G)$ is the identity,
and in general because $[n+1](R)(x)=[n](R)(x)\cdot x$. The map
$x\mapsto x\cdot\ldots\cdot x$ is a homomorphism of groups because
$G(R)$ is commutative, and $[n]$ is a morphism of schemes by
construction; hence $[n]$ is a homomorphism of group schemes in the
sense of [def-sc-group-scheme].

(b) Both identities follow from (a) on $R$-points:
$[n](x)\cdot[n'](x)=(n+n')x=[n+n'](x)$ and
$[n]([n'](x))=n(n'x)=(nn')x=[nn'](x)$.

(c) $[n](R)(e)=ne=e$ and
$[n](R)(i(x))=n(-x)=-(nx)=i([n](R)(x))$, again by (a).
