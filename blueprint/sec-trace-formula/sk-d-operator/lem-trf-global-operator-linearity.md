+++
id = "lem-trf-global-operator-linearity"
kind = "lemma"
title = "Linearity of the global operator in the correspondence"
order = 2439
uses = ["def-trf-admissibility", "def-trf-coefficient-conventions", "def-trf-correspondence", "def-trf-global-operator"]
+++
Fix the coefficient
conventions and an
admissible cohomological
correspondence $c=(c_1,c_2):C\to X\times_sX$ whose ordinary leg
$c_2$ is proper, and let $K\in D^b_{ctf}(X,A)$. Then the global
operator of [def-trf-global-operator] is $A$-linear in the
correspondence: for correspondence morphisms $u,u':Lc_2^*K\to Rc_1^!K$ and $a\in A$ one has

$$
T_c(u+au')=T_c(u)+a\,T_c(u')
$$

in $\operatorname{End}_{D(A)}(R\Gamma_c(X,K))$.

## Proof

By [def-trf-coefficient-conventions] the compact-support
cohomology is an $A$-linear functor, so
$R\Gamma_c(C,-)$ is $A$-linear on morphisms and
$R\Gamma_c(C,u+au')=R\Gamma_c(C,u)+a\,R\Gamma_c(C,u')$. The four
remaining arrows of the composite defining $T_c(u)$ in
[def-trf-global-operator] — the unit and the counit of the two
adjunctions of [def-trf-admissibility] and the two structure
isomorphisms of the six-operations package — do not depend on $u$,
so that composing with them preserves the displayed $A$-linearity.
