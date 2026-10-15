+++
id = "det-lem-formal-closed-support-adjunction"
kind = "lemma"
title = "Sections with closed support: adjunction and fiber triangle for all coefficients"
uses = ["def-exc-proetale-sections-with-support", "lem-exc-proetale-closed-support", "lem-exc-proetale-support-triangle", "sk-prop-sf-open-closed-triangle"]
+++
Let $\Lambda$ be a condensed ring (in particular any admissible one), $i\colon Z\hookrightarrow X$
a closed immersion with quasi-compact open complement $j\colon V\hookrightarrow X$, and
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$ for $\Lambda_X$-modules $M$
(as in [def-exc-proetale-sections-with-support], with $\Lambda$ in place of a finite ring).

1. $\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$, and $\underline\Gamma_Z$ is right adjoint to
   $i_*$ on module sheaves; it is left exact.
2. $R\underline\Gamma_Z$, computed on K-injective complexes, is right adjoint to $i_*$ on
   $D(-_{\mathrm{proét}},\Lambda)$; equivalently
   $R\operatorname{Hom}_X(i_*A,K)\cong R\operatorname{Hom}_Z(A,R\underline\Gamma_ZK)$.
3. For an injective $\Lambda_X$-module $I$, the unit $I\to j_*j^*I$ is surjective.
4. There is a distinguished triangle
   $i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to i_*R\underline\Gamma_ZK[1]$, natural in $K$, and
   $R\underline\Gamma_ZK\cong i^*\fib(K\to Rj_*j^*K)$.
