+++
kind = "proof"
of = "proposition-divisors-degree-g-open-chart"
order = 1538
+++
We construct mutually inverse maps: a divisor gives its invertible sheaf,
normalized along $P$, and a family in $F$ has, up to units on $T$, a
unique section in each fibre, whose zero scheme is a family of divisors of
degree $g$.

*From divisors to sheaves.* On $C\times \operatorname{Hilb}^{g}_{C/k}$,
normalize the universal invertible sheaf as

$$
\mathcal L_g=\mathcal O(D_g)\otimes
f_{\operatorname{Hilb}^g}^*(P_{\operatorname{Hilb}^g}^*\mathcal O(D_g))^{-1}.
$$

Let $W$ be the open locus where $Rf_{\operatorname{Hilb}^g,*}\mathcal L_g$ is a line
bundle in degree $0$; then $\mathcal L_g$ defines a morphism $W\to F$.

*From sheaves to divisors.* Let $\mathcal L$ be a rigidified class in
$F(T)$ and set $\mathcal N=f_{T,*}\mathcal L$. By assumption
$Rf_{T,*}\mathcal L\simeq\mathcal N'[0]$ for an invertible $\mathcal N'$,
so $\mathcal N\simeq\mathcal N'$ is invertible. The
evaluation map $f_T^*\mathcal N\to\mathcal L$ is a section $s$ of
$\mathcal L\otimes f_T^*\mathcal N^{-1}$. It is determined by $\mathcal L$
up to a unit on $T$, and such a unit does not change its zero scheme $D$.

This $D$ is a relative effective Cartier divisor. Indeed, the formation
of $\mathcal N$ commutes with base change
(Lemma [lemma-coherent-base-change-invertible-sheaves]). Hence on each
fibre $C_{\kappa(t)}$ the section $s$ is a nonzero element of the
one-dimensional space of sections. The fibre is integral because $C$ is
geometrically integral, so the zero scheme of $s$ on the fibre is an
effective Cartier divisor.
Moreover, the fibres of $D$ have degree $g$: for a point $t$ of $T$ we have
$h^0(\mathcal L_t)=1$ and $H^1(C_t,\mathcal L_t)=0$, so Riemann–Roch
gives

$$
\deg\mathcal L_t
=\chi(\mathcal L_t)-(1-g)=1-(1-g)=g.
$$

The morphism $D\to T$ is proper, since $D$ is closed in the proper scheme
$C_T$. It has finite fibres, and it is flat, as is every relative
effective Cartier divisor. A proper, flat, finitely presented morphism
with finite fibres is finite locally free. Its rank at $t$ is the degree
$g$ of the fibre $D_t$, the divisor of zeros of a section of
$\mathcal L_t$. Hence $D$ defines a morphism
$T\to \operatorname{Hilb}^{g}_{C/k}$.

*The constructions are inverse.* Normalizing $\mathcal O(D)$ along
$P_T$ recovers $\mathcal L$, because
$\mathcal O(D)\simeq\mathcal L\otimes f_T^*\mathcal N^{-1}$.
The two constructions are therefore inverse to each other,
and they commute with base change, which proves that $W\simeq F$ (see [Stacks, [0B9X](https://stacks.math.columbia.edu/tag/0B9X)]).
