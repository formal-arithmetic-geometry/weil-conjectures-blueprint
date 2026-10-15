+++
kind  = "proof"
of    = "det-lem-formal-closed-support-stratum"
uses = ["det-lem-formal-closed-support-derived", "sk-prop-sf-open-closed-triangle"]
+++
*First isomorphism.* $a_!L=i_*(u_!L)$, and $i_*\dashv R\underline\Gamma_Z$ in the
$R\operatorname{Hom}$ form ([det-lem-formal-closed-support-derived] (1)).

*Second isomorphism.* On module sheaves $u_!$ is exact and left adjoint to the
exact functor $u^*$ ([sk-prop-sf-open-closed-triangle], applied on $Z$). As
in the proof of [det-lem-formal-closed-support-derived] (3), exactness of $u_!$
implies that $u^*$ preserves K-injective complexes. Representing
$R\underline\Gamma_ZK$ by a K-injective complex $J^\bullet$, we get
$R\operatorname{Hom}_Z(u_!L,J^\bullet)=\Hom^\bullet(u_!L,J^\bullet)=\Hom^\bullet(L,u^*J^\bullet)=R\operatorname{Hom}_S(L,u^*J^\bullet)$.

*Third isomorphism.* Locally on $S_{\mathrm{proét}}$, $L$ is a direct summand of
$\Lambda_S^m$. For such $L$ the natural map
$L^\vee\otimes_{\Lambda_S}N\to\mathcal Hom_{\Lambda_S}(L,N)$ is an isomorphism for
every $\Lambda_S$-module $N$: this is clear for $L=\Lambda_S^m$, it is
compatible with direct summands, and it may be checked locally. Both sides
are exact in $N$, since $L$ and $L^\vee$ are flat. Moreover
$\mathcal Hom(L,-)$ preserves K-injective complexes, because its left adjoint
$L\otimes-$ is exact. Hence for $N^\bullet=u^*J^\bullet$ (K-injective)
$$
R\operatorname{Hom}_S(L,N^\bullet)=R\Gamma\bigl(S,\mathcal Hom(L,N^\bullet)\bigr)=R\Gamma(S,L^\vee\otimes N^\bullet),
$$
and $L^\vee\otimes N^\bullet$ computes the derived tensor product since $L^\vee$
is flat.

Every step is natural in $K$ (through the K-injective resolution, natural up
to homotopy). Taking $H^q$ gives the last assertion.
