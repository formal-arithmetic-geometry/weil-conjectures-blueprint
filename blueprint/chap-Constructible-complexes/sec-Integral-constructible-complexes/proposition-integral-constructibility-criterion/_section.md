+++
id = "proposition-integral-constructibility-criterion"
kind = "proposition"
title = "The integral constructibility criterion"
order = 246
lean = ["AlgebraicGeometry.ProEtale.IntegralModelsStacks.internal_integral_criterion_forward", "AlgebraicGeometry.ProEtale.IntegralModelsStacks.internal_integral_criterion_reverse"]
uses = ["lemma-stability"]
+++
Let $X$ be Noetherian. The following conditions on
$K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ are equivalent:

1. $K\in\Dbc(X,\mathcal O_E)$;
2. $K$ is derived complete and $K_1\in\Dbc(X,\mathbf F_E)$;
3. there is a finite stratification of $X$ such that on each stratum
   $S$, pro-étale locally,
   $K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ for a
   bounded complex $P^\bullet$ of finite free $\mathcal O_E$-modules;
4. $K\in D^b_{\mathrm{ctf}}(X,\mathcal O_E)$.
