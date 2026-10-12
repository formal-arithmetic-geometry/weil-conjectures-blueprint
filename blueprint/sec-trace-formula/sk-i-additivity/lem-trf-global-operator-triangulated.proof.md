+++
kind  = "proof"
of    = "lem-trf-global-operator-triangulated"
+++
By [def-trf-global-operator] the global operator is the composite
of the counit of the adjunction $Rc_{2,!}\dashv Rc_2^!$, the
identification $R\Gamma_c(X,Rc_{2,*}Lc_2^*K)\cong R\Gamma_c(C,Lc_2^*K)$, the map $R\Gamma_c(C,u)$ and the
identification $R\Gamma_c(C,Rc_1^!K)\cong R\Gamma_c(X,Rc_{1,!}Rc_1^!K)$
with its counit. Each of these constructions is a natural
transformation of exact functors in the coefficient object: the
functors $Lc_2^*$, $Rc_1^!$, $Rc_{i,*}$, $Rc_{i,!}$,
$R\Gamma_c$ are exact (the admissibility of
[def-trf-admissibility] supplies the adjunctions and
[prop-trf-compact-support-perfectness] the perfectness needed for
the compact-support identifications), the units and counits of
adjunctions are natural, and the exchange identifications are
compatible with base change. Hence, the squares commuting by [lem-trf-global-operator-naturality], the composite is compatible with
distinguished triangles, which is the assertion.
