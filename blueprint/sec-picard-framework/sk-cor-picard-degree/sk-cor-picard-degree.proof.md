+++
kind  = "proof"
of    = "sk-cor-picard-degree"
uses = ["sk-thm-picard-main"]
+++
Degree is additive under tensor product, so $\deg$ is a homomorphism. Its
zero subgroup is $\operatorname{Pic}^0(C)=J(C)(k)$ by [sk-thm-picard-main],
and $\deg\cO_C(P)=1$ for $P\in C(k)$ (which exists since $k$ is
algebraically closed), so $\deg$ is surjective and $d\mapsto\cO_C(dP)$ is
a homomorphic section. The kernel and $\deg$ do not involve any choice;
the section does: for $g\geq1$ and $P\neq Q$ one has
$\cO_C(P)\not\cong\cO_C(Q)$, since an isomorphism would give a rational
function with a single simple pole, i.e. a degree-one morphism
$C\to\mathbf P^1$, forcing $C\cong\mathbf P^1$ and $g=0$.
