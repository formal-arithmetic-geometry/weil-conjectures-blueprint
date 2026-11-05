+++
kind = "proof"
of = "lemma-flat-models-generators--1"
order = 255004
uses = ["definition-constructible-sheaves"]
+++
Flat constructible sheaves lift along epimorphisms onto constructible
sheaves. Indeed, finitely many sections on affine étale schemes generate a
constructible sheaf. After finite affine étale refinements these sections
lift through the epimorphism, and the corresponding finite sum of free
sheaves is flat and constructible.

Since constructible sheaves are closed under kernels and cokernels, this
lifting property gives a resolution $P$ of $C$ by flat constructible
sheaves, zero above degree $b$. It is $K$-flat. Truncate it below degree
$a$, replacing $P^a$ by the cokernel of $P^{a-1}\to P^a$. This cokernel is
constructible. It is flat because
$H^{a-1}(P\otimes_A F)=H^{a-1}(C\otimes_A^{\mathbf L}F)=0$ for every
$A$-sheaf $F$. The truncation still represents $C$ and is zero outside
$[a,b]$.

Conversely, a bounded complex of flat sheaves is $K$-flat, so tensoring it
term by term with a sheaf computes the derived tensor product and preserves
the interval of nonzero terms. This proves the required Tor bound.
For the final assertion, choose a Tor interval and enlarge it if necessary
so that its endpoints satisfy $a\leq b$.
