+++
kind  = "proof"
of    = "det-lem-formal-closed-support-adjunction"
+++
The proofs of [lem-exc-proetale-closed-support] and [lem-exc-proetale-support-triangle] use
only the following properties, which hold for modules over any sheaf of rings $\Lambda_X$
(pulled back to $Z$ and $V$ via [sk-prop-sfb-cartesian-coefficients]): $i_*$ and $j_!$ are
exact, $i_*$ and $j_*$ are fully faithful, $i^*i_*=\mathrm{id}$, $j^*i_*=0$, and the
localization sequence $0\to j_!j^*M\to M\to i_*i^*M\to0$ is exact ([sk-prop-sf-open-closed-triangle]).

(1) $N=\ker(M\to j_*j^*M)$ satisfies $j^*N=\ker(j^*M\xrightarrow{\mathrm{id}}j^*M)=0$, so by the
localization sequence $N\cong i_*i^*N=i_*\underline\Gamma_Z(M)$. For a morphism
$\phi\colon i_*A\to M$, the composite to $j_*j^*M$ is adjoint to $j^*\phi\colon j^*i_*A=0\to j^*M$,
hence zero; so $\phi$ factors uniquely through $N=i_*\underline\Gamma_Z(M)$, and by full
faithfulness of $i_*$ corresponds to a unique $A\to\underline\Gamma_Z(M)$. Left exactness: a
right adjoint is left exact.

(2) Since $i_*$ is exact, its right adjoint $\underline\Gamma_Z$ sends K-injective complexes to
K-injective complexes: $\Hom_{K}(C,\underline\Gamma_ZI)=\Hom_K(i_*C,I)=0$ for acyclic $C$. Choose
K-injective resolutions (\stacks{079P}); then
$\Hom_{D}(i_*A,K)=\Hom_K(i_*A,I)=\Hom_K(A,\underline\Gamma_ZI)=\Hom_D(A,R\underline\Gamma_ZK)$,
and the same with shifts and internal Hom complexes gives the $R\operatorname{Hom}$ form.

(3) $j_!j^*I\to j_*j^*I$ is a monomorphism (it is the identity on $V$, and its source is zero
on $Z$). By injectivity of $I$, the inclusion $j_!j^*I\hookrightarrow I$ (the counit) extends
to $s\colon j_*j^*I\to I$. Let $e=\eta\circ s\colon j_*j^*I\to j_*j^*I$, $\eta$ the unit. Then
$j^*e=\mathrm{id}$, since on $V$ all three maps are identities; by full faithfulness of
$j_*$, $e=\mathrm{id}$. So $\eta$ is a split epimorphism.

(4) Represent $K$ by a K-injective complex $I^\bullet$ with injective terms. $j^*I^\bullet$ is
K-injective (its left adjoint $j_!$ is exact), so $Rj_*j^*K=j_*j^*I^\bullet$. By (1), (3) the
sequences $0\to i_*\underline\Gamma_Z(I^n)\to I^n\to j_*j^*I^n\to0$ are exact; they form a
short exact sequence of complexes, hence a distinguished triangle whose first term is
$i_*\underline\Gamma_Z(I^\bullet)=i_*R\underline\Gamma_ZK$. Thus
$i_*R\underline\Gamma_ZK\cong\fib(K\to Rj_*j^*K)$, and applying the exact $i^*$ with
$i^*i_*=\mathrm{id}$ gives the formula. Naturality follows from functoriality of K-injective
resolutions in the homotopy category.
