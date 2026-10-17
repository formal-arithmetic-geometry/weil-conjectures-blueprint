+++
id = "def-weil-algebraically-closed-coefficients"
kind = "definition"
title = "Algebraically closed coefficient category"
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructibleAdic"]
order = 1821
uses = ["def-weil-finite-field-fiber", "def-weil-rationalization-karoubi", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-bounded-constructible", "sk-thm-sfb-qlbar-two-colimit"]
+++
Fix the global finite-field datum [def-weil-finite-field-fiber]
$(p,a,q,k_0,k)$, a prime $\ell\neq p$, and a scheme $Y$. Set
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and use
the rationalized category [def-weil-rationalization-karoubi] for every finite
coefficient field. Let $\mathcal E_\ell$ be the directed set of finite
extensions $E/\Ql$ contained in $\Qlb$. For $E\subset L$, the transition
functor is $K\mapsto K\otimes_E L$. Form a triangulated category $\mathcal
C_Y$ whose objects are pairs $(E,K)$ with $E\in\mathcal E_\ell$ and $K\in
D^b_c(Y,E)$, and whose morphisms between $(E,K)$ and $(E',K')$ are

$$
 \Hom_{\mathcal C_Y}((E,K),(E',K'))
 =\varinjlim_{\substack{L\in\mathcal E_\ell\\L\supset E,E'}}
 \Hom_{D^b_c(Y,L)}
 \bigl(K\otimes_E L,K'\otimes_{E'}L\bigr).
$$

Composition and distinguished triangles are represented over one common
finite extension.

The algebraically closed coefficient category is the condensed one:
$D^b_c(Y,\Qlb)\subseteq D(Y_{\mathrm{proét}},\Qlb)$ is the category of bounded complexes of
modules over $\overline{\mathbf Q}_{\ell,Y}=p_Y^*\underline{\Qlb}$ ([sk-def-sfb-qlbar-condensed],
[sk-def-sfb-pulled-back-coefficients]) with constructible cohomology sheaves
([sk-def-sfb-bounded-constructible]). For $Y$ of finite type over $k$, extension of scalars
$(E,K)\mapsto\overline{\mathbf Q}_{\ell,Y}\otimes_{E_Y}K$ is an equivalence

$$
 \mathcal C_Y\xrightarrow{\ \sim\ }D^b_c(Y,\Qlb),
$$

and it carries the triangles of $\mathcal C_Y$ to distinguished triangles
([sk-thm-sfb-qlbar-two-colimit] (4)). We identify the two categories along it and write

$$
 D^b_c(Y,\Qlb)=\mathcal C_Y.
$$

No Karoubi completion is taken: the notation $\mathcal C_Y$ denotes the
common-stage category displayed above, in which no idempotent is formally
adjoined. Every object, morphism, and distinguished triangle has a finite
coefficient field of definition, after enlarging that field if necessary.
