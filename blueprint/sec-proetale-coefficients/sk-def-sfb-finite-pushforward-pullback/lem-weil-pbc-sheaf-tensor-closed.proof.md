+++
kind  = "proof"
of    = "lem-weil-pbc-sheaf-tensor-closed"
uses  = ["det-def-sfb-sheaf-tensor-local-iso", "det-def-sfb-sheaf-tensor-structure", "det-def-sfb-sheaf-tensor-closed"]
+++
**1.** Sheafification is a left adjoint, so it is right exact. It is left exact:
it is computed by applying the plus construction twice, and each plus
construction is a filtered colimit, over covering sieves, of limits of the values
of the presheaf; finite limits commute with these limits, and with filtered
colimits because $\mathcal A$ is Grothendieck abelian. Colimits of sheaves are
the sheafified colimits of presheaves, and colimits of presheaves are computed
objectwise in $\mathcal A$; since $a$ is exact, filtered colimits of sheaves are
exact. If $G$ is a generator of $\mathcal A$, the presheaves
$V\mapsto\bigoplus_{\Hom(V,U)}G$, for $U$ in a small skeleton of $\mathcal C$,
generate $\mathrm{PSh}(\mathcal C;\mathcal A)$, and their sheafifications generate
$\mathrm{Sh}(\mathcal C,J;\mathcal A)$ because $\Hom(aP,F)=\Hom(P,\iota F)$. So
$\mathrm{Sh}(\mathcal C,J;\mathcal A)$ is Grothendieck abelian.

**2.** The stability of the morphisms inverted by $a$ under $\otimes_p$ is
[det-def-sfb-sheaf-tensor-local-iso], and the resulting symmetric monoidal
structure, with $a$ strong symmetric monoidal, is
[det-def-sfb-sheaf-tensor-structure]. Additivity in each variable follows from 3,
since a functor preserving colimits is additive.

**3.** This is [det-def-sfb-sheaf-tensor-closed].

For $\mathcal A=\Ab$: the tensor product of abelian groups is the tensor product
of $\mathbf Z$-modules, associative, unital with unit $\mathbf Z$, symmetric and
additive in each variable, and the tensor–hom adjunction
$\Hom(M\otimes_{\mathbf Z}N,P)\cong\Hom(N,\Hom(M,P))$ makes it closed; $\Ab$ is
Grothendieck abelian. So 1–3 apply, and the unit $a(\underline{\mathbf Z})$ is the
constant sheaf $\underline{\mathbf Z}$.
