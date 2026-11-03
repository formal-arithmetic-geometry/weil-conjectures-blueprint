+++
kind  = "proof"
of    = "det-lem-int-tensor-projection"
uses = ["sk-prop-sf-open-closed-triangle", "det-def-sfb-derived-tensor-hom", "sk-prop-sfb-cartesian-coefficients"]
+++
Throughout we use [sk-prop-sf-open-closed-triangle]: for an open immersion $j$
with closed complement $i$, the functors $j^*$, $j_!$, $i^*$, $i_*$ are exact,
$j^*j_!=\mathrm{id}$, $i^*i_*=\mathrm{id}$, $i^*j_!=0$, $j^*i_*=0$, and a morphism of
module sheaves on $X$ that becomes an isomorphism after $j^*$ and after $i^*$
is an isomorphism (apply the localization sequence to its kernel and
cokernel). Inverse images $j^*$, $i^*$ are compatible with tensor products,
since the coefficient sheaves are pulled back
([sk-prop-sfb-cartesian-coefficients]).

*Open immersions, sheaves.* Let $j\colon V\hookrightarrow Y$ be open, $M$ a
$\Lambda_V$-module and $N$ a $\Lambda_Y$-module. The identity of $M\otimes j^*N$,
viewed as a map $M\otimes j^*N\to j^*j_!M\otimes j^*N=j^*(j_!M\otimes N)$, is
adjoint under $j_!\dashv j^*$ to a natural map
$\theta\colon j_!(M\otimes j^*N)\to j_!M\otimes N$. After $j^*$ it is the identity;
after $i^*$ both sides vanish ($i^*(j_!M\otimes N)=i^*j_!M\otimes i^*N=0$). So $\theta$
is an isomorphism.

*Closed immersions, sheaves.* Let $i\colon T\hookrightarrow Y$ be closed, $M$ a
$\Lambda_T$-module and $N$ a $\Lambda_Y$-module. The unit of $i^*\dashv i_*$ gives
$i_*M\otimes N\to i_*i^*(i_*M\otimes N)=i_*(M\otimes i^*N)$. After $i^*$ it is the
identity of $M\otimes i^*N$, and after $j^*$ both sides vanish. So it is an
isomorphism.

*Derived version.* Represent $L$ by a K-flat complex $Q$ of $\Lambda_X$-modules
([det-def-sfb-derived-tensor-hom]). Inverse image along an open or closed
immersion preserves K-flatness: if $C$ is acyclic on the subscheme, then
$C\otimes j^*Q=j^*(j_!C\otimes Q)$, respectively $C\otimes i^*Q=i^*(i_*C\otimes Q)$ by the
sheaf formulas, and $j_!C$, $i_*C$ are acyclic. Applying the sheaf formulas
termwise to the double complexes gives
$j_!M\otimes Q\simeq j_!(M\otimes j^*Q)$ and $i_*M\otimes Q\simeq i_*(M\otimes i^*Q)$ for any
complex $M$; since $Q$, $j^*Q$, $i^*Q$ are K-flat and $j_!$, $i_*$ are exact, these
are the derived isomorphisms $j_!M\otimes^{\mathbf L}L\simeq j_!(M\otimes^{\mathbf L}j^*L)$ and
$i_*M\otimes^{\mathbf L}L\simeq i_*(M\otimes^{\mathbf L}i^*L)$.

*Locally closed immersions.* Combining,
$$
a_!M\otimes^{\mathbf L}L=i_*(u_!M)\otimes^{\mathbf L}L\simeq i_*\bigl(u_!M\otimes^{\mathbf L}i^*L\bigr)
\simeq i_*u_!\bigl(M\otimes^{\mathbf L}u^*i^*L\bigr)=a_!(M\otimes^{\mathbf L}a^*L).
$$
All maps are natural in $M$ and $L$.
