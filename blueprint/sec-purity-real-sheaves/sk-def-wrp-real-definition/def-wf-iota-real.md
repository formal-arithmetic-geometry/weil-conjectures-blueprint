+++
id = "def-wf-iota-real"
kind = "definition"
title = "$\\iota$-real and $\\iota$-realizable Weil sheaves"
lean = ["AlgebraicGeometry.WeilSheaf.IsRealizable"]
order = 3872
uses = ["def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "sk-lem-coefficient-heart"]
+++
Let $X_0$ be a separated finite-type $k_0$-scheme, fix
$\iota:\Qlb\xrightarrow{\sim}\mathbf C$ as in
[def-weil-punctual-weights], and let $\mathcal F$ be a
constructible
Weil sheaf on $X_0$, that is, $\mathcal F\in\Cons(X,\Qlb)$
([sk-lem-coefficient-heart]) with a Weil structure ([sk-def-sf-weil-complexes],
[def-weil-weil-sheaf-complex]), with the
stalk Frobenius modules $(V_x,F_x)$ of
[def-weil-punctual-weights]. The *local characteristic
factor* of $\mathcal F$ at a closed point $x$ is

$$
P_x(T):=\prod_{\alpha\in S_x}(1-\alpha T)=\det(1-TF_x\mid V_x),
$$

where $S_x$ is the spectrum of $F_x$ counted with multiplicity.
The sheaf $\mathcal F$ is *$\iota$-real* if
$\iota(P_x(T))\in\mathbf R[T]$ for every closed point $x\in|X_0|$;
equivalently, the multiset of complex Frobenius eigenvalues is stable
under complex conjugation at every closed point. The sheaf $\mathcal F$
is *$\iota$-realizable* if it is a direct summand (in the category
of Weil sheaves) of an $\iota$-real lisse Weil sheaf.
