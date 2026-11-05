+++
id = "lemma-sections-support-closed-subscheme"
kind = "lemma"
title = "Sections with closed support"
order = 277
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.formal_closed_support_derived", "AlgebraicGeometry.ProEtale.CondensedRing.formal_closed_support_adjunction"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality"]
+++
Let $\Lambda$ be admissible, let $i:Z\hookrightarrow X$ be a
closed immersion with open complement $j:V\hookrightarrow X$, and let
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Z_{\mathrm{pro}\acute{e}t},\Lambda)$ be the
local cohomology functor (Definition [definition-local-cohomology]),

$$
R\underline\Gamma_Z K=i^*\fib(K\longrightarrow Rj_*j^*K).
$$

For a sheaf $M$ of $\Lambda_X$-modules on $X_{\mathrm{pro}\acute{e}t}$, let
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$, the sheaf on $Z$ of
sections of $M$ with support in $Z$.

1. $R\underline\Gamma_Z$ is the right derived functor of
   $\underline\Gamma_Z$. Consequently the adjunction of
   Lemma [lemma-local-cohomology-right-adjoint] holds in the form
   $R\!\operatorname{Hom}_X(i_*N,K)=R\!\operatorname{Hom}_Z(N,R\underline\Gamma_ZK)$.
2. Let $a=i\circ u:S\hookrightarrow X$ with $u:S\hookrightarrow Z$ an
   open immersion, and let $L$ be a finite locally projective
   $\Lambda_S$-module with dual $L^\vee$. Then naturally in
   $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$
   $$
   R\!\operatorname{Hom}_X(a_!L,K)
   =R\Gamma\bigl(S,L^\vee\otimes u^*R\underline\Gamma_ZK\bigr).
   \tag{3.1}
   $$
