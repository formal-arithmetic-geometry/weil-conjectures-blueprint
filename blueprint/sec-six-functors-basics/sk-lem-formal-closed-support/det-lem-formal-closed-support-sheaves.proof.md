+++
kind  = "proof"
of    = "det-lem-formal-closed-support-sheaves"
uses = ["sk-prop-sf-open-closed-triangle", "sk-prop-sfb-cartesian-coefficients"]
+++
Since $X$ is Noetherian, $j$ is quasi-compact, and [sk-prop-sf-open-closed-triangle]
gives: $i^*$ is exact and preserves limits; $i_*$ is exact and fully faithful,
so $i^*i_*=\mathrm{id}$ (Stacks, Tags 09AA, 09BM); $j^*$ and $j_!$ are exact;
and every module $M$ sits in the exact sequence
$0\to j_!j^*M\to M\to i_*i^*M\to0$ (Stacks, Tag 09AH). Moreover $j^*j_*=\mathrm{id}$,
because $V_{\mathrm{proét}}$ is the localization of $X_{\mathrm{proét}}$ at $V$, so
$j_*$ is fully faithful; and $j^*i_*=0$ since $Z\times_XV=\emptyset$.

*(1)* Put $N=\ker(M\to j_*j^*M)$. As $j^*$ is exact and $j^*$ of the unit is
the identity of $j^*M$ (triangle identity and $j^*j_*=\mathrm{id}$), we get
$j^*N=\ker(\mathrm{id}_{j^*M})=0$. The localization sequence for $N$ then reads
$0\to0\to N\to i_*i^*N\to0$, so $N\xrightarrow{\sim}i_*i^*N=i_*\underline\Gamma_Z(M)$.
Naturality is clear since all maps are natural in $M$.

*(2)* Let $A$ be a $\Lambda_Z$-module and $\phi\colon i_*A\to M$. The composite
$i_*A\to M\to j_*j^*M$ is adjoint to $j^*\phi\colon j^*i_*A=0\to j^*M$, hence
is zero. So $\phi$ factors uniquely through
$N=i_*\underline\Gamma_Z(M)$, and by full faithfulness of $i_*$ the factorization
is $i_*$ of a unique morphism $\psi\colon A\to\underline\Gamma_Z(M)$.
Conversely every $\psi$ gives $\phi$ as the composite
$i_*A\xrightarrow{i_*\psi}i_*\underline\Gamma_Z(M)=N\hookrightarrow M$. These
constructions are inverse and natural in $A$ and $M$, which proves
$\Hom_X(i_*A,M)=\Hom_Z(A,\underline\Gamma_Z(M))$. A right adjoint preserves
limits, in particular kernels, so $\underline\Gamma_Z$ is left exact.

*(3)* The adjunction of (2) extends termwise to complexes and to homotopy
classes of maps: $\Hom_{K(Z)}(C,\underline\Gamma_ZI)=\Hom_{K(X)}(i_*C,I)$. If $C$ is
acyclic, so is $i_*C$ because $i_*$ is exact; if $I$ is K-injective the right
side vanishes, so $\underline\Gamma_ZI$ is K-injective. Similarly, for an injective
module $I$ the functor $\Hom_Z(-,\underline\Gamma_ZI)=\Hom_X(i_*(-),I)$ is exact, so
$\underline\Gamma_ZI$ is injective.
