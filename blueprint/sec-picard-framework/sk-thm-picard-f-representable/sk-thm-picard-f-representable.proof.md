+++
kind  = "proof"
of    = "sk-thm-picard-f-representable"
uses = ["sk-thm-picard-rr"]
+++
On $C\times H_g$, normalize the universal invertible sheaf as

$$
\cL_g=\cO(D_g)\otimes f_{H_g}^*\bigl(P_{H_g}^*\cO(D_g)\bigr)^{-1}.
$$

Let $W$ be the open locus where $Rf_{H_g,*}\cL_g$ is a line bundle in
degree $0$ ([sk-thm-picard-perfect]). The restriction of $\cL_g$ to
$C\times W$ lies in $F(W)$, so by Yoneda this gives a morphism $W\to F$.

Conversely, take a rigidified $\cL$ in $F(T)$ and put
$\cN=f_{T,*}\cL$. The evaluation map $f_T^*\cN\to\cL$ is a section $s$ of
$\cL\otimes f_T^*\cN^{-1}$. On each geometric fibre it is a nonzero
section of the unique one-dimensional space of sections. Its zero scheme
$D$ is thus a relative effective Cartier divisor
([det-lem-picard-zero-dictionary]). Riemann–Roch ([sk-thm-picard-rr],
[det-cor-picard-degree-g]) gives

$$
\deg\cL_t=\chi(\cL_t)-(1-g)=1-(1-g)=g.
$$

The divisor is proper with finite fibres and flat over $T$, hence finite
locally free of degree $g$. It defines $T\to H_g$. Since
$\cO(D)\simeq\cL\otimes f_T^*\cN^{-1}$, normalizing $\cO(D)$ along $P_T$
recovers $\cL$; in particular $T\to H_g$ factors through $W$.
Multiplication of a section by a base unit does not change its zero
divisor; the two constructions are consequently inverse and commute with
base change. This proves $W\simeq F$ (compare Stacks Project, Tag 0B9X),
and the composite $W\simeq F\subset\operatorname{Pic}_{C/k}$ sends a
divisor $D$ to the rigidified class of $\cO(D)$. Finally, $W$ is open in
$H_g$, which is smooth of dimension $g$ ([sk-thm-picard-hilb-curves]),
so $F$ is smooth of dimension $g$.
