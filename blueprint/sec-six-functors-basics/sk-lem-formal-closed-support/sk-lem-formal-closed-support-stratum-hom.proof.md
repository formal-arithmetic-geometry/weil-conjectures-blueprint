+++
kind  = "proof"
of    = "det-lem-formal-closed-support-stratum-hom"
+++
*First isomorphism.* $a_!=i_*u_!$ by definition, and $i_*\dashv R\underline\Gamma_Z$ in the
$R\operatorname{Hom}$ form ([det-lem-formal-closed-support-adjunction] (2)).

*Second.* $u_!$ is exact with exact right adjoint $u^*$ on module sheaves; exactness of $u_!$
makes $u^*$ preserve K-injective complexes, so the adjunction $u_!\dashv u^*$ passes to
$R\operatorname{Hom}$, with $u^*$ needing no deriving.

*Third.* Locally on $S$, $L$ is a direct summand of $\Lambda_S^n$. For such $L$ the natural map
$L^\vee\otimes_{\Lambda_S}N\to\mathcal Hom_{\Lambda_S}(L,N)$ is an isomorphism for every module
$N$ (true for $L=\Lambda_S^n$, and preserved under direct summands and locality), both
functors are exact in $N$ ($L$ and $L^\vee$ are flat), and $\mathcal Hom(L,-)$ preserves
K-injectives because its left adjoint $L\otimes-$ is exact. Hence
$\cHom(L,N)=L^\vee\otimes N$ for complexes $N$, and
$R\operatorname{Hom}_S(L,N)=R\Gamma(S,\cHom(L,N))=R\Gamma(S,L^\vee\otimes N)$ with
$N=u^*R\underline\Gamma_ZK$. Naturality in $K$ holds at each step.
