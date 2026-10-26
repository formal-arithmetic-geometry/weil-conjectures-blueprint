+++
id = "det-lem-int-ext-formula"
kind = "lemma"
title = "Reduction to extensions by zero and the Hom formula"
order = 2443
uses = ["sk-lem-int-integral-heart", "sk-lem-formal-closed-support"]
+++
1. Every $C\in\Dbc(X,\mathcal O_E)$ admits a finite filtration by
   distinguished triangles whose graded pieces are shifts of objects $a_!L$,
   where $a=i\circ u:S\hookrightarrow X$ is the inclusion of a stratum of a
   finite stratification, with $u:S\hookrightarrow Z$ open and
   $i:Z\hookrightarrow X$ closed, and $L\in\Cons(S,\mathcal O_E)$ is pro-étale
   locally the completion of a finitely generated $\mathcal O_E$-module; if
   $C\in\Cons(X,\mathcal O_E)$, the pieces may be taken in degree $0$.
2. For such $a$, $L$ and any $K\in D(X_{\mathrm{proét}},\mathcal O_E)$,
   $$
   R\operatorname{Hom}_X(a_!L,K)
   \simeq R\Gamma\bigl(S,L^\vee\otimes^{\mathbf L}_{\mathcal O_{E,S}}u^*R\underline\Gamma_ZK\bigr),
   \qquad L^\vee=\cHom_{\mathcal O_{E,S}}(L,\mathcal O_{E,S}),
   $$
   and $L^\vee\otimes^{\mathbf L}-$ has Tor amplitude $[0,1]$ and commutes with
   filtered colimits and with derived inverse limits.
