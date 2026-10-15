+++
kind  = "proof"
of    = "det-nagata-elimination-dense"
uses = ["def-nagata-elimination-indeterminacy", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-conrad-schematically-dense-blowup", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-admissible-blowup-comp"]
+++
*Step 1: make $U$ dense.* By [lemma-nagata-conrad-schematically-dense-blowup]
choose a finite-type ideal $\mathcal I_0$ with $V(\mathcal I_0)=T\setminus U$;
the blow-up $b_1:T_1=\operatorname{Bl}_{\mathcal I_0}(T)\to T$ is
$U$-admissible and $U_1=b_1^{-1}(U)\simeq U$ is a quasi-compact,
scheme-theoretically dense open of $T_1$. $T_1$ is qcqs, being proper over
$T$.

*Step 2: eliminate over $T_1$.* The strict transform $W_1\to T_1$ of $W$ is
a closed subscheme of $W\times_TT_1$, hence separated of finite type over
$T_1$, and it is an isomorphism over $U_1$ since $b_1$ is one over $U$.
Apply [lemma-nagata-elimination-indeterminacy] to $(T_1,U_1,W_1)$: there is a
$U_1$-admissible blow-up $b_2:T'\to T_1$ whose strict transform
$W'\to T'$ of $W_1$ is an open immersion (this is the construction of
[def-nagata-elimination-indeterminacy], whose first step is exactly Step 1).
The strict transform of $W_1$ under $b_2$ is the strict transform of $W$
under $b=b_1b_2$: both are the scheme-theoretic closure of the inverse image
of $U$ in $W\times_TT'$.

*Step 3: admissibility and density.* By
[lemma-nagata-admissible-blowup-comp], the composite $b=b_1\circ b_2$ is a
$U$-admissible blow-up of $T$. Since $U_1$ is quasi-compact and
scheme-theoretically dense in $T_1$ and $b_2$ is $U_1$-admissible,
[lemma-nagata-admissible-blowup-preserves-density] shows that
$b^{-1}(U)=b_2^{-1}(U_1)$ is scheme-theoretically dense in $T'$.
