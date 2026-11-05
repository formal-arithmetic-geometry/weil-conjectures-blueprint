+++
kind = "proof"
of = "lemma-local-cohomology-right-adjoint"
order = 206
+++
We first compute $R\underline\Gamma_Z$. Represent $K$ by a K-injective
complex $J$ with injective terms, so that $Rj_*j^*K$ is represented by
$j_*j^*J$. The unit $J\to j_*j^*J$ is surjective in each degree: for an
injective $\mathcal R$-module $I$ and an object $V$, a section of
$j_*j^*I$ over $V$ is a map $j_!j^*\mathcal R_V\to I$, and it extends along
the monomorphism $j_!j^*\mathcal R_V\to\mathcal R_V$. Hence the kernel of
$J\to j_*j^*J$, taken termwise, represents the fibre of the unit, and
applying the exact functor $i^*$ gives
$R\underline\Gamma_ZK\simeq i^*\fib(K\to Rj_*j^*K)$.

Let $F=\fib(K\to Rj_*j^*K)$. Since $j^*i_*M=0$, we have
$\operatorname{Hom}(i_*M,Rj_*j^*K)=\operatorname{Hom}(j^*i_*M,j^*K)=0$
in all degrees, so maps $i_*M\to K$ are the same as maps $i_*M\to F$.
The restriction $j^*F$ vanishes, because $j^*$ of the unit is an
isomorphism, so the localization sequence gives $F\simeq i_*i^*F$, and
$\operatorname{Hom}(i_*M,i_*i^*F)=\operatorname{Hom}(M,i^*F)$ since
$i_*$ is fully faithful.
