+++
kind  = "proof"
of    = "lem-sc-group-cd-one"
+++
For finite $M$, apply [lem-sc-sylow-module-filtration]: there is an
open subgroup $H$ of index prime to $\ell$ acting on $M$ through an
$\ell$-group, so that $M|_H$ is an iterated extension of trivial modules
$\mathbf F_\ell$. The long exact cohomology sequence, one filtration
step at a time, gives $H^2(H,M)=0$. Restriction to $H$ followed by
corestriction is multiplication by the index $[G:H]$ on $H^2(G,M)$.
As the index is prime to $\ell$ and $H^2(G,M)$ is killed by a power of
$\ell$ (since $M$ is), multiplication by it is invertible there. Hence
$H^2(G,M)=0$.

An arbitrary discrete $\ell$-primary module $M$ is the directed union
of its finite $G$-stable submodules. Indeed the orbit of each element
is finite, $G$ being compact and the stabilizer open, and a finite set
of finite-order elements generates a finite abelian group. Embed $M$
equivariantly in the coinduced module $C(G,M)$ of locally constant
functions $G\to M$ by $m\mapsto(g\mapsto gm)$, with $G$ acting by right
translation. In the abelian category of
[def-exc-continuous-cohomology] the coinduction functor from abelian
groups is right adjoint to the exact forgetful functor, so coinduced
modules of injective abelian groups are injective, and a short
computation shows that every coinduced module is acyclic. Hence
$H^2(G,M)=0$ can be expressed through the invariants of the iterated
cokernels $C(G,M)/M$ and $C(G,C(G,M)/M)/(C(G,M)/M)$. A locally
constant function on the compact space $G$ has finite image, so it
takes values in a finite $G$-stable submodule; these cokernels, and
their invariants, are therefore the directed unions of the
corresponding objects for the finite $G$-stable submodules. The
vanishing for finite modules therefore gives $H^2(G,M)=0$ without a
finiteness assumption.

Finally the cokernel of $M\to C(G,M)$ is again discrete
$\ell$-primary, and $C(G,M)$ is acyclic, so the long exact sequence
identifies $H^{q+1}(G,M)$ with $H^q(G,C(G,M)/M)$ for $q\geq1$.
Repeated dimension shifting reduces every degree at least two to the
vanishing of $H^2$ just proved.
