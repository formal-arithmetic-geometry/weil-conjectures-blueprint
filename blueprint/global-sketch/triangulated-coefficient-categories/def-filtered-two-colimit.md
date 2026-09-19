+++
id = "def-filtered-two-colimit"
kind = "definition"
title = "Common-stage pair category and the symbol $2$-colimit"
order = 19
uses = ["def-qbar-ambient-finext-diagram", "def-qbar-finext-diagram"]
+++
For a scheme $Y$, fix a prime $\ell\neq p$, an algebraic closure
$\Qlb/\Ql$, and let $\mathcal B_E(Y)$ be either the constructible
diagram $\mathcal C_E(Y)$ of Definition [def-qbar-finext-diagram] or
the ambient diagram $\mathcal A_E(Y)$ of
Definition [def-qbar-ambient-finext-diagram], with its specified
transition functors; write $T_{L/E}$, $\eta_E$, and $a_{M,L,E}$ for
the transition functor, unit, and associativity isomorphism of the selected
diagram. An object is a pair $(E,K)$, where
$E\in\mathcal E_\ell$ and $K\in\mathcal B_E(Y)$. A morphism representative

$$
(M,u):(E,K)\longrightarrow(F,L)
$$

consists of a finite coefficient field $M$ containing $E$ and $F$
and a morphism

$$
u:T_{M/E}K\longrightarrow T_{M/F}L
\quad\text{in }\mathcal B_M(Y).
$$

If $M\subset N$, its transport $u_N$ is

$$
T_{N/E}K\xrightarrow[\sim]{a^{-1}_{N,M,E}}
T_{N/M}T_{M/E}K\xrightarrow{T_{N/M}(u)}
T_{N/M}T_{M/F}L\xrightarrow[\sim]{a_{N,M,F}}T_{N/F}L.
$$

Representatives $(M,u)$ and $(N,v)$ are equivalent when a finite
coefficient field $P\supset M,N$ satisfies $u_P=v_P$. Thus

$$
\Hom((E,K),(F,L))=
\varinjlim_{M\supset E,F}
\Hom_{\mathcal B_M(Y)}(T_{M/E}K,T_{M/F}L),
$$

where the filtered colimit is taken in abelian groups and the displayed
equivalence relation is its representative description.

The identity is represented by the identity at stage $E$, with the unit
isomorphism inserted. Given $[M,u]:(E,K)\to(F,L)$ and
$[N,v]:(F,L)\to(G,Q)$, choose $P\supset M,N$ and define

$$
[N,v]\circ[M,u]=[P,v_P\circ u_P].
$$

Addition is defined by transporting two representatives to one common
stage and adding them there. The zero object is $(\Ql,0)$; a biproduct of
$(E,K)$ and $(F,L)$ is represented over a common $M$ by
$(M,T_{M/E}K\oplus T_{M/F}L)$.

The resulting additive category is denoted

$$
\underset{E\in\mathcal E_\ell}{\operatorname{2-colim}^{\mathrm{pair}}}
\mathcal B_E(Y).
$$

In this lecture the symbol $\operatorname{2-colim}$ denotes this explicit
ordinary common-stage category. It is not an infinity-categorical colimit
and it is not a union of the object sets of the finite-stage categories.
