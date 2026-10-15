+++
kind = "proof"
of = "sk-prop-pe-comparison-morphism"
uses = ["def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-sections", "prop-weil-pbc-site-comparison-finite-level"]
+++
An étale morphism is weakly étale and an étale covering is a pro-étale
covering, so the inclusion is a continuous functor preserving finite limits and
defines $\nu_X$ ([def-weil-pbc-site-comparison-morphism]).

For the description of $\nu_X^*$, define the right hand side
$V\mapsto\Gamma(V_{\Et},h_{\Et}^*F)$ for every weakly étale $h\colon V\to X$.
Pro-étale coverings are fpqc coverings, so by fpqc descent for étale sheaves this
rule is a sheaf. Pulling back the restriction of a pro-étale sheaf $G$ to
$X_{\Et}$ gives the counit $\nu_X^*\nu_{X,*}G\to G$ in $\Sh(X_{\Proet})$; on an
étale object $V$ the rule gives $F(V)$, which is the unit
$F\to\nu_{X,*}\nu_X^*F$ in $\Sh(X_{\Et})$. The two adjunction identities follow by
restriction and pullback, so the rule is $\nu_X^*$ (Stacks Project, Tag 0GLZ).
In particular the formula describes the sheaf inverse image directly.

For an affine limit $U$, sections of an étale sheaf are continuous under affine
inverse limits, which gives $(\nu_X^*F)(U)=\varinjlim_iF(U_i)$ (Stacks Project,
Tag 099S); the detailed argument on the affine ind-étale basis is
[lem-weil-pbc-comparison-sections]. Exactness of $\nu_X^*$ on module sheaves,
together with the unit isomorphism on étale objects, is
[prop-weil-pbc-site-comparison-finite-level].
