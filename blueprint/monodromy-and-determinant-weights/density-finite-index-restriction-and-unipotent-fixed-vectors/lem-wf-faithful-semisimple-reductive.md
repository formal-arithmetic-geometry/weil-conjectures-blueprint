+++
id = "lem-wf-faithful-semisimple-reductive"
kind = "lemma"
title = "The unipotent radical is trivial on a faithful semisimple module"
order = 4020
uses = ["def-wf-reductive-group", "def-wf-semisimple-module", "def-wf-simple-module", "def-wf-unipotent-radical", "lem-wf-unipotent-fixed-vector"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be connected and let $V$ be a
semisimple faithful $H$-module. Then $R_u(H)=1$, so $H$ is
reductive.

## Proof

Let $U\triangleleft H$ be any connected normal unipotent subgroup.
It is enough to prove $U=1$, by the characterization of the
unipotent radical in [def-wf-unipotent-radical]. By
[def-wf-semisimple-module], $V$ is a direct sum of simple
summands; let $S$ be one of them. By
[lem-wf-unipotent-fixed-vector], $S^U\ne0$. Since $U$ is
normal in $H$, for $h\in H$, $u\in U$, and $v\in S^U$ one has
$u(hv)=h(h^{-1}uh)v=hv$; hence $S^U$ is $H$-stable. Simplicity
in the sense of [def-wf-simple-module] gives $S^U=S$, so $U$
acts trivially on every simple summand and on
all of $V$. Faithfulness means that the only element acting trivially
on $V$ is the identity, hence $U=1$; this is precisely reductivity
as defined in [def-wf-reductive-group].
