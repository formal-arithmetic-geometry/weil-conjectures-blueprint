+++
kind = "proof"
of = "lemma-acyclicity-pulled-back-injectives--1"
order = 120002
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image"]
+++
Restrict $G=\nu_W^*I$ to the affine pro-étale site of $W$. By
[proposition-pro-etale-affines-form-basis], this restriction is an equivalence
of categories of sheaves. It preserves injectives and identifies global
sections with evaluation at the terminal object, so it also identifies their
right derived functors.

Let $f:V'\to V$ be a morphism of affine pro-étale $W$-schemes. Present $f$
as a cofiltered limit of morphisms $f_i:V'_i\to V_i$ of affine étale
$W$-schemes over a common index category. Finite fibre products commute with
these limits. The continuity formula of
[proposition-comparison-morphism-inverse-image] therefore identifies the Čech
complex of $G$ for $f$ with the filtered colimit of the Čech complexes at
these finite stages. On affine étale objects, the comparison unit is an
isomorphism by [theorem-classical-sheaves-essential-image], so the finite-stage
complexes are those of $I$.

For every object $a$ of $A$, applying $\Hom_A(a,-)$ to a finite-stage complex
gives the Čech complex of the abelian presheaf $\Hom_A(a,I(-))$. Injectivity
of $I$ makes this complex exact in positive degrees, and testing all $a$
gives exactness of the original complex in $A$. This holds for every $f_i$,
without a surjectivity hypothesis. Filtered colimits are exact in $A$, so the
Čech complex of $G$ for $f$ is exact in positive degrees.

In particular, this applies to all surjections $V'\to V$ on the affine
pro-étale site. The Čech acyclicity criterion then gives vanishing of the
higher derived functors of evaluation at the terminal object. Transporting
this vanishing along the restriction equivalence gives the assertion.
