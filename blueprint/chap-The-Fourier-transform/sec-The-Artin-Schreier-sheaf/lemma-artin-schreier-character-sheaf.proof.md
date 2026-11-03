+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf"
order = 1212
+++
We define $\mathcal L_\psi$ as an eigensheaf in the direct image of the
constant sheaf under an Artin–Schreier cover, and read off its
properties from the corresponding properties of the cover: addition of
roots for the first isomorphism, a fibrewise pairing for the second,
and the action of Frobenius on roots for the trace.

Fix a nontrivial character $\psi_0:\mathbf F_p\to E^\times$. Since the
trace pairing on $k_0$ is nondegenerate, there is $a\in k_0^\times$
such that $\psi(z)=\psi_0(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$.
The cover $u^p-u=ax$ of the affine line is finite étale, with group
of translations $\mathbf F_p$. Let $\mathcal L_\psi$ be the image of

$$
e_{\psi_0}=\frac1p\sum_{c\in\mathbf F_p}\psi_0(c)^{-1}\tau_c^*
$$

on the direct image of the constant sheaf $E$ under this cover. It is
lisse of rank one, since its stalk is the $\psi_0$-eigenspace in the
regular representation. The root $u=0$ over $x=0$ specifies the
trivialization at zero. Adding roots of two Artin–Schreier equations
identifies the contracted product of the two torsors with the torsor
for the sum. Passing to the character eigenspaces, we obtain the first
isomorphism. For the second, the pairing on the direct image given by
summing products over the fibres is perfect and invariant under the
translations. For an invariant pairing, the $\chi$- and
$\chi'$-eigenspaces of two characters are orthogonal unless
$\chi\chi'=1$. Hence our pairing pairs the $\psi_0$-eigenspace perfectly
with the $\psi_0^{-1}$-eigenspace. Since
$\psi^{-1}(z)=\psi_0^{-1}(\operatorname{Tr}_{k_0/\mathbf F_p}(az))$, the
$\psi_0^{-1}$-eigenspace of the same cover is $\mathcal L_{\psi^{-1}}$,
and we obtain $\mathcal L_\psi^\vee\simeq\mathcal L_{\psi^{-1}}$.

For a root $u$ above $x\in\mathbf F_{q^n}$ we have

$$
u^{q^n}=u+
\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(ax).
$$

Geometric Frobenius acts on functions on the torsor by pullback along
this map, and hence on the chosen eigenspace by
$\psi_0(\operatorname{Tr}(ax))$. By transitivity of field traces, this is
the asserted trace. Since these scalars are roots of unity, their images
under any field embedding have absolute value one.
