+++
kind  = "proof"
of    = "sk-lem-formal-closed-support"
+++
We use three facts about the closed immersion $i$: $i^*$ is exact, preserves limits and
satisfies $i^*i_*=\mathrm{id}$ (\stacks{09AA}); $i_*$ is exact (\stacks{09BM}); and every sheaf
$M$ sits in the localization sequence $0\to j_!j^*M\to M\to i_*i^*M\to0$ (\stacks{09AH}). By
the last fact, a sheaf whose restriction to $V$ vanishes is of the form $i_*$ of a sheaf on
$Z$; this applies to $\ker(M\to j_*j^*M)$. The sheaf-level functor is
[def-exc-proetale-sections-with-support].

*Adjunction.* A map $i_*A\to M$ composes to zero with $M\to j_*j^*M$, because $j^*i_*A=0$. So
it factors through $\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$, and by full faithfulness of
$i_*$ it corresponds to a map $A\to\underline\Gamma_Z(M)$. Thus $\underline\Gamma_Z$ is right
adjoint to $i_*\colon\Mod(Z_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$. Since
$i_*$ is exact, $\underline\Gamma_Z$ preserves K-injective complexes, and K-injective
resolutions exist (\stacks{079P}). Hence $R\underline\Gamma_Z$ is computed on K-injective
complexes, and the adjunction passes to $R\operatorname{Hom}$. For finite coefficients this
is [lem-exc-proetale-closed-support]; the argument for all admissible $\Lambda$ is
[det-lem-formal-closed-support-adjunction].

*Fiber formula.* For an injective sheaf $I$ the unit $I\to j_*j^*I$ of the adjunction
$j^*\dashv j_*$ on $\Mod(X_{\mathrm{proét}},\Lambda)$ is surjective. Indeed, by injectivity the
inclusion $j_!j^*I\to I$ extends along $j_!j^*I\hookrightarrow j_*j^*I$ to a map
$s\colon j_*j^*I\to I$. The composite of $s$ with the unit is the identity after applying
$j^*$, hence is the identity, because $j_*$ is fully faithful. Now represent $K$ by a
K-injective complex $I^\bullet$ with injective terms (\stacks{079P}). Then $j^*I^\bullet$ is
K-injective, since the left adjoint $j_!$ of $j^*$ is exact, so $j_*j^*I^\bullet$ represents
$Rj_*j^*K$. The termwise exact sequences
$$
0\to i_*\underline\Gamma_Z(I^n)\to I^n\to j_*j^*I^n\to0
$$
give a distinguished triangle
$i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to i_*R\underline\Gamma_ZK[1]$ in
$D(X_{\mathrm{proét}},\Lambda)$. Applying $i^*$ and $i^*i_*=\mathrm{id}$ gives the fiber formula.
For finite coefficients this triangle is [lem-exc-proetale-support-triangle].

*The stratum formula.* Since $a_!=i_*u_!$, part (1), the adjunction $u_!\dashv u^*$ and the
identity $\cHom(L,-)=L^\vee\otimes-$ for the finite locally projective sheaf $L$ give
$R\operatorname{Hom}_X(i_*u_!L,K)=R\operatorname{Hom}_Z(u_!L,R\underline\Gamma_ZK)=R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$.
Details: [det-lem-formal-closed-support-stratum-hom].
