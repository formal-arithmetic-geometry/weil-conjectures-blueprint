+++
kind = "proof"
of = "sk-thm-picard-f-representable"
uses = ["sk-thm-picard-rr"]
+++
On $C\times H_g$, normalize the universal invertible sheaf as

$$
\mathcal L_g=\mathcal O(D_g)\otimes
f_{H_g}^*(P_{H_g}^*\mathcal O(D_g))^{-1}.
$$

Let $W$ be the open locus where $Rf_{H_g,*}\mathcal L_g$ is a line
bundle in degree $0$. Then $\mathcal L_g$ defines a morphism $W\to F$.

Conversely, let $\mathcal L$ be a rigidified class in $F(T)$ and set
$\mathcal N=f_{T,*}\mathcal L$; since $Rf_{T,*}\mathcal L\simeq\mathcal N'[0]$
for an invertible $\mathcal N'$, we have $\mathcal N\simeq\mathcal N'$. The
evaluation map $f_T^*\mathcal N\to\mathcal L$ is a section $s$ of
$\mathcal L\otimes f_T^*\mathcal N^{-1}$. Since the formation of
$\mathcal N$ commutes with base change
(Lemma [sk-thm-picard-perfect]), on each fibre
$C_{\kappa(t)}$, which is integral because $C$ is geometrically integral,
$s$ is a nonzero element of the one-dimensional space of sections. Its
zero scheme on the fibre is therefore an effective Cartier divisor, and
the zero scheme $D$ of $s$ is a relative effective Cartier divisor. The section is determined by $\mathcal L$ up to a unit on $T$,
which does not change $D$. For a point $t$ of $T$ we have
$h^0(\mathcal L_t)=1$ and $H^1(C_t,\mathcal L_t)=0$, so Riemann–Roch
gives

$$
\deg\mathcal L_t
=\chi(\mathcal L_t)-(1-g)=1-(1-g)=g.
$$

The divisor is proper with finite fibres and flat over $T$. Hence it is
finite locally free of degree $g$, and it defines a morphism $T\to H_g$.
Since $\mathcal O(D)\simeq\mathcal L\otimes f_T^*\mathcal N^{-1}$,
normalizing $\mathcal O(D)$ along $P_T$ recovers $\mathcal L$.
Consequently, the two constructions are inverse to each other,
and they commute with base change. This proves that $W\simeq F$ (see [Stacks, Tag 0B9X](https://stacks.math.columbia.edu/tag/0B9X)).
