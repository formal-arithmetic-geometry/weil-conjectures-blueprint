+++
kind  = "proof"
of    = "sk-lem-as-properties"
+++
Fix a nontrivial character $\Psi:\mathbf F_p\to E^\times$. Since the
trace pairing on $k_0$ is nondegenerate, there is $a\in k_0^\times$
such that $\psi(z)=\Psi(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$.
The cover $u^p-u=ax$ of the affine line is finite étale, with group
of translations $\mathbf F_p$. Let $\mathcal L_\psi$ be the image of

$$
 e_\Psi=\frac1p\sum_{c\in\mathbf F_p}\Psi(c)^{-1}\tau_c^*
$$

on the direct image of the constant sheaf $E$ under this cover. It is
lisse of rank one, since its stalk is the $\Psi$-eigenspace in the
regular representation, and the root $u=0$ over $x=0$ specifies the
trivialization at zero. Adding roots of two Artin–Schreier equations
identifies the contracted product of the two torsors with the torsor
for the sum. Passing to the character eigenspaces, we obtain the first
isomorphism, together with its associativity and unit compatibilities.
Replacing the character by its inverse gives the isomorphism for the
dual.

For a root $u$ above $x\in\mathbf F_{q^n}$ we have

$$
 u^{q^n}=u+
 \operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(ax).
$$

Geometric Frobenius acts on functions on the torsor by pullback along
this map, and hence on the chosen eigenspace by
$\Psi(\operatorname{Tr}(ax))$. By transitivity of field traces, this is
the asserted trace. These scalars are roots of unity, so their images
under any field embedding have absolute value one.

(The blueprint defines $\mathcal L_\psi$ through the $k_0$-Artin–Schreier
map; the comparison of the two models, including the trivializations at
zero, is a step of the detail layer of this block.)
